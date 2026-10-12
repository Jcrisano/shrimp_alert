import sys
import time

def main():
    print("Welcome to Shrimp Alert!")
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

        continue_option = int(input())
        if continue_option == 1:
            continue
        if continue_option == 2:
            main()
        if continue_option ==3:
            sys.exit()


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
    verify_frequency = input(f"Shrimp check in {frequency} seconds? (y/n): ").strip().lower()
    while verify_frequency == "n":
            frequency = set_interval(input("Frequency of reminder (seconds): "))
            verify_frequency = input(f"Shrimp check in {frequency} seconds? (y/n): ").strip().lower()
    return frequency

if __name__ == "__main__":
    main()