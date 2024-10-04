from aspose_compressor import AsposeCompressor

file_path = str(input("Enter the file path: "))
file_name = str(input("Enter the file name: "))


ac = AsposeCompressor()
file = ac.compress_video(file_path)
file.save(file_name)