import sys
import time
import json
import random
from read_file import exercise_list

def main():
    print("Welcome to Shrimp Alert!")

    continue_options_list = [1, 2, 3]
    frequency = set_interval(input("Frequency of reminder (seconds): "))
    verified_frequency = verify_frequency(frequency)
    exercise_file = "exercises.json"

    ex_list = json.loads(exercise_list(exercise_file))
    ex_list_types = list(ex_list.keys())

    exercises = []
    stretches = []
    postureChecks = []
    movement_selector = random.randint(0, 1)

# Separates the movements from the JSON ex_list into specific corresponding lists based on type
    for exercise_type in ex_list:
        if exercise_type == "exercises":
            for exercise in ex_list[exercise_type]:
                exercises.append(exercise)
        elif exercise_type == "stretches":
            for exercise in ex_list[exercise_type]:
                stretches.append(exercise)
        elif exercise_type == "postureChecks":
            for exercise in ex_list[exercise_type]:
                postureChecks.append(exercise)

# Removes postureChecks from types since a posture cue will be used with every alert
# and randomly selects a movement category to be used in the alert
    ex_list_types.remove("postureChecks")
    random_movement_category = ex_list_types[movement_selector]    

# Using the random_movement() function, selects a random movement either in the stretches or exercises list
    randomly_selected_movement = random_movement(random_movement_category, exercises, stretches)
    reps_or_duration = list(randomly_selected_movement.keys())[1]


    while True:  
        print(f"Checking Posture in {verified_frequency} seconds!")

        time.sleep(verified_frequency)

        print("Fix that Shrimp Spine, Nerd!\n")
        print(f"{random_movement_category}: ")
        print(f"{randomly_selected_movement["name"]}")
        print(f"{reps_or_duration}: {randomly_selected_movement[reps_or_duration]}\n")
        print("CHOOSE FROM BELOW (1, 2, OR 3)")
        print("1. Reset with same interval")
        print("2. Reset and change interval")
        print("3. Exit program")

        while True:
            try:
                continue_option = int(input().strip())
            except ValueError:
                print("Must choose 1, 2, or 3.")
                continue
            break
        if continue_option in continue_options_list:
            if continue_option == 1:
                continue
            elif continue_option == 2:
                frequency = set_interval(input("Frequency of reminder (seconds): "))
                verified_frequency = verify_frequency(frequency)
            elif continue_option == 3:
                sys.exit()
        else:
            print("Must choose 1, 2, or 3.")

    


def set_interval(user_input):
    frequency = (user_input)
    while True:
        try:
            frequency = int(frequency)
        except ValueError:
            frequency = input("Must input a positive integer: ")
            continue
        if frequency > 0:
            break
        else:
            frequency = input("Must input a positive integer: ")
    return frequency

def verify_frequency(frequency):
    verify_options = ["y", "n"]
    while True:
        verify_frequency = input(f"Shrimp check in {frequency} seconds? (y/n): ").strip().lower()
        if verify_frequency in verify_options:
            if verify_frequency != "y":
                frequency = set_interval(input("Frequency of reminder (seconds): "))
                continue
            if verify_frequency == "y":
                break
        else:
            print("Must choose 'y' or 'n': ")
    return frequency

def random_movement(category, exercise_list, stretch_list):
    if category == "exercises":
        random_exercise = exercise_list[random.randint(0,len(exercise_list))]     
    elif category == "stretches":
        random_exercise = stretch_list[random.randint(0,len(stretch_list))]
    return random_exercise



if __name__ == "__main__":
    main()