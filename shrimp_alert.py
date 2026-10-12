import sys
import time

def main():
    print("Welcome to Shrimp Alert!")
    continue_options_list = [1, 2, 3]
    frequency = set_interval(input("Frequency of reminder (seconds): "))
    verified_frequency = verify_frequency(frequency)
    
    while True:  
        print(f"Checking Posture in {verified_frequency} seconds!")

        time.sleep(verified_frequency)

        print("Fix that Shrimp Spine, Nerd!\n")
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


if __name__ == "__main__":
    main()