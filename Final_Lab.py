"""
*******************************************************************************
Filename:      Final_Lab.py

Author:        Ankit Bombwal

Date:          2020.08.6

Modifications: 2020.08.6

Description:   This program determines the rate of success after ten thousand
               Trials with using the Monty Hall (AKA The Game Show Host) problem.
*******************************************************************************
"""
# The functions from the Random library that we will be needing.
from random import seed
from random import randint


def run_simulation():
    # Defining variables for recording wins and losses. As well as the number of closed doors
    win_count = 0
    fail_count = 0
    closed_doors = 3

    # Constant that refers to the number of times the simulation is run.
    TRIALS = 10000

    # Seeding the random number generator to receive truly random numbers.
    seed()

    # For loop to run the 10K trials.
    for tests in range(TRIALS):

        # The Car is hidden behind one of the three doors at random, and the player picks one
        door_value = randint(1, 3)
        player_choice = randint(1, 3)

        # AT THIS POINT, The host opens one of the doors and shows a Goat.
        while closed_doors > 2:
            # host chooses a door
            host_choice = randint(1, 3)

            # The host will never choose a door that has the car, nor the door the player picked
            if host_choice == door_value or host_choice == player_choice:
                continue

            # Host has opened one door, and therefore we exit the loop.
            closed_doors -= 1

        # AT THIS POINT, We have established which door the prize is behind, which door the player chose,
        # and which door the host chose. Now, the host offers a chance for the player to switch. For the sake
        # of the argument, we assume the player always switches doors.

        if player_choice == 1 and host_choice == 2:
            player_choice = 3
        elif player_choice == 1 and host_choice == 3:
            player_choice = 2
        elif player_choice == 2 and host_choice == 1:
            player_choice = 3
        elif player_choice == 2 and host_choice == 3:
            player_choice = 1
        elif player_choice == 3 and host_choice == 1:
            player_choice = 2
        elif player_choice == 3 and host_choice == 2:
            player_choice = 1

        # This is where the Door is opened
        if door_value == player_choice:
            win_count += 1
        else:
            fail_count += 1

        closed_doors = 3

    # If everything was done correctly, the win rate of the player should be somewhere around 66.7%
    total_win_rate = round((win_count / TRIALS) * 100, 1)
    print("The player, in " + str(TRIALS) + " trials got a car " + str(win_count) + " times, and got a goat "
          + str(fail_count) + " times. This resulted in a success rate of " + str(total_win_rate) + "%.")


run_simulation()

"""
"/Users/ankitbombwal/Documents/Python Projects/Lab/bin/python" "/Users/ankitbombwal/Documents/Python Projects/Lab/Final_Lab.py"
The player, in 10000 trials got a car 6650 times, and got a goat 3350 times. This resulted in a success rate of 66.5%.

Process finished with exit code 0
"""
