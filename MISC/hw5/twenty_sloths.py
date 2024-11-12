#this program simulates a game where the user bets on the number of sloths they will draw
#if the user draws more than 20, they lose, same as if they have less than 14
#the user can choose to draw 1-8 sloths, 3-7 sloths, or hold

#This program has been updated for HW 5 to include a loop that allows the user to play again
# and keep track of the number of games played and net balance.
import random

#vars for the new features
games_played = 0
net_balance = 0
play_again = 'y'

while play_again.lower() == 'y':
    games_played += 1

    # user input loop, ensures bet is greater than or equal to 10
    while True:
        user_bet = float(input("Enter your bet: "))
        if user_bet >= 10:
            break
        else:
            print("Invalid bet. Please enter a bet greater than or equal to 10. ")
            continue

    # init vars
    sloths = 1
    winnings = 0
    # this is used to control game state
    end = False

    while end != True:
        # input for betting options
        print("\n Pick an option. ")
        print("1. Pick 1-8 sloths")
        print("2. Pick 4-7  sloths")
        print("3. Hold \n")

        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            sloths += random.randint(1, 8)
            print(f"\nTotal sloths: {sloths}")
        elif user_choice == 2:
            sloths += random.randint(4, 7)
            print(f"\nTotal sloths: {sloths}")
        elif user_choice == 3:
            end = True
            print(f"\nTotal sloths: {sloths}")
        else:
            print("Invalid input. Please enter a valid option. ")
            continue

        if sloths >= 20:
            end = True

    # logic for calculating winnings/losses
    if sloths <= 14 or sloths > 20:
        winnings = 0
    elif sloths == 15:
        winnings = user_bet * .25
    elif sloths == 16:
        winnings = user_bet * .5
    elif sloths == 17:
        winnings = user_bet
    elif sloths == 18:
        winnings = user_bet * 1.25
    elif sloths == 19:
        winnings = user_bet * 1.5
    elif sloths == 20:
        winnings = user_bet * 2
    else:
        print("An error occurred. ")

    print(f"\n \n \nTotal sloths: {sloths}")
    print(f"Your winnings are: {winnings:.2f}")

    if winnings > user_bet:
        print("You won! ")
    elif winnings == user_bet:
        print("You broke even. ")
    else:
        print("You lost. ")

    net_balance += (winnings - user_bet)
    print(f"\nGames played: {games_played}")
    print(f"Net gain/loss: ${net_balance:.2f}")

    #this is the new loop that asks the user if they want to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() in ['y', 'n']:
            break
        print("Please enter 'y' for yes or 'n' for no.")

#basic statistics
print(f"\nFinal Statistics:")
print(f"Total games played: {games_played}")
print(f"Final net gain/loss: ${net_balance:.2f}")
print("Thanks for playing!")