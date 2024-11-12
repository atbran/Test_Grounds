from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv

pv.global_theme.allow_empty_mesh = True

class ConformationalAnalysisTool:
    def __init__(self):
        self.mol = None
        self.conformers = []
        self.energies = []

    def input_molecule(self, mol_input, input_format=1):
        if input_format == 1:
            self.mol = Chem.MolFromSmiles(mol_input)
        elif input_format == 2:
            self.mol = Chem.MolFromMolFile(mol_input)
        elif input_format == 3:
            self.mol = Chem.MolFromPDBFile(mol_input)
        elif input_format == 4:
            # Debug mode: use a hardcoded molecule
            self.mol = Chem.MolFromSmiles("CC(C)(C)C1CCC(=O)CC1")
        elif input_format == 5:
            self.mol = Chem.MolFromSmiles("CC(CC1=CC=CC=C1)NC")
        else:
            raise ValueError("Unsupported input format")

        if self.mol is None:
            raise ValueError("Failed to parse molecule")

        self.mol = Chem.AddHs(self.mol)

    def generate_conformers(self, num_conformers=50):
        params = AllChem.ETKDGv3()
        params.randomSeed = 42
        params.numThreads = 0  # Use all available CPUs
        self.conformers = AllChem.EmbedMultipleConfs(
            self.mol, numConfs=num_conformers, params=params
        )
        if not self.conformers:
            raise ValueError("Failed to generate conformers")

    def calculate_energies(self):
        self.energies = []
        mmff_props = AllChem.MMFFGetMoleculeProperties(self.mol)
        for conf_id in self.conformers:
            ff = AllChem.MMFFGetMoleculeForceField(self.mol, mmff_props, confId=conf_id)
            if ff is None:
                print(f"Warning: Could not create force field for conformer {conf_id}")
                continue
            ff.Minimize(maxIts=500)
            energy = ff.CalcEnergy()
            self.energies.append((conf_id, energy))

    def visualize_2d(self):
        img = Draw.MolToImage(self.mol, size=(300, 300), kekulize=True, wedgeBonds=True)
        img.save('molecule_2d.png')

    def visualize_3d(self, conformer_ids):
        if not self.mol or not self.conformers:
            print("Error: Molecule is not initialized or no conformers generated.")
            return

        plotter = pv.Plotter()
        plotter.set_background('white')

        atom_colors = {1: 'white', 6: 'gray', 7: 'blue', 8: 'red', 16: 'yellow'}  # H, C, N, O, S

        # Create dictionaries to store actors
        atom_actors = {}
        bond_actors = {}
        label_actors = {}
        text_actor = None

        def update_display(conformer_index):
            nonlocal text_actor
            conformer_index = int(conformer_index)
            conf_id = conformer_ids[conformer_index]
            conf = self.mol.GetConformer(conf_id)

            points = np.array([conf.GetAtomPosition(i) for i in range(self.mol.GetNumAtoms())])

            # Update atom positions
            for i, atom in enumerate(self.mol.GetAtoms()):
                atomic_num = atom.GetAtomicNum()
                color = atom_colors.get(atomic_num, 'gray')
                sphere = pv.Sphere(radius=0.2, center=points[i])
                if i not in atom_actors:
                    atom_actors[i] = plotter.add_mesh(sphere, color=color, smooth_shading=True)
                else:
                    plotter.remove_actor(atom_actors[i])
                    atom_actors[i] = plotter.add_mesh(sphere, color=color, smooth_shading=True)

            # Update bond positions
            for bond in self.mol.GetBonds():
                bond_id = (bond.GetBeginAtomIdx(), bond.GetEndAtomIdx())
                start = points[bond.GetBeginAtomIdx()]
                end = points[bond.GetEndAtomIdx()]
                if bond_id in bond_actors:
                    plotter.remove_actor(bond_actors[bond_id])
                cylinder = pv.Cylinder(center=(start + end) / 2, direction=end - start, radius=0.05,
                                       height=np.linalg.norm(end - start))
                bond_actors[bond_id] = plotter.add_mesh(cylinder, color='lightgray', smooth_shading=True)

            # Update atom labels
            for j, atom in enumerate(self.mol.GetAtoms()):
                label = plotter.add_point_labels([points[j]], [atom.GetSymbol()], point_size=1, font_size=10)
                if j in label_actors:
                    plotter.remove_actor(label_actors[j])
                label_actors[j] = label

            energy = next(e for cid, e in self.energies if cid == conf_id)
            if text_actor:
                plotter.remove_actor(text_actor)
            text_actor = plotter.add_text(f"Conformer {conformer_index + 1}\nEnergy: {energy:.2f} kcal/mol",
                                          position='upper_left', font_size=10)

            plotter.reset_camera()

        # Add a slider to switch between conformers
        slider = plotter.add_slider_widget(update_display, [0, len(conformer_ids) - 1],
                                           title="Conformer", style='modern')

        # Initial display
        update_display(0)

        plotter.show()

    def plot_energy_diagram(self):
        if not self.energies:
            print("Warning: No energy data to plot")
            return

        plt.figure(figsize=(10, 6))
        conf_ids, energies = zip(*self.energies)
        plt.bar(conf_ids, energies)
        plt.xlabel('Conformer ID')
        plt.ylabel('Energy (kcal/mol)')
        plt.title('Conformer Energy Diagram')
        plt.savefig('energy_diagram.png')
        plt.close()

    def run_analysis(self, mol_input, input_format=1, num_conformers=50):
        self.input_molecule(mol_input, input_format)
        self.generate_conformers(num_conformers)
        self.calculate_energies()
        self.visualize_2d()
        self.plot_energy_diagram()

        if self.energies:
            sorted_conformers = sorted(self.energies, key=lambda x: x[1])
            top_5_conformers = [conf_id for conf_id, _ in sorted_conformers[:5]]
            self.visualize_3d(top_5_conformers)

            print(f"Analysis complete. Generated {len(self.conformers)} conformers.")
            print(f"Lowest energy: {sorted_conformers[0][1]:.2f} kcal/mol")
            print(f"Highest energy: {sorted_conformers[-1][1]:.2f} kcal/mol")
        else:
            print("Warning: No energy data available")

if __name__ == "__main__":
    tool = ConformationalAnalysisTool()

    while True:
        try:
            input_format = int(input("Enter input format (1: smiles, 2: mol, 3: pdb, 4: debug, 5: breaking bad): "))
            if input_format not in [1, 2, 3, 4,5]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    mol_input = input("Enter a SMILES string or file path: ") if input_format != 4 and input_format != 5 else ""

    try:
        tool.run_analysis(mol_input, input_format)
        print("2D structure saved as 'molecule_2d.png'")
        print("Energy diagram saved as 'energy_diagram.png'")
    except Exception as e:
        print(f"An error occurred: {e}")