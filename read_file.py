import json

def main():
    exercise_file = "exercises.json"







def exercise_list(pathway):
    file = open(pathway, "r")
    exercise_list = file.read()
    file.close()
    return exercise_list

if __name__ == "__main__":
    main()