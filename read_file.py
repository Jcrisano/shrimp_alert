import json

def main():
    exercise_file = "exercises.json"
    ex_list = json.loads(exercise_list(exercise_file))
    ex_list_types = list(ex_list.keys())
    for exercise_type in ex_list_types:
        print(exercise_type.upper())
        for i in ex_list[exercise_type]:
            if len(list(i.keys())) > 1:
                print(f"EXERCISE: {i[list(i.keys())[0]]}, {list(i.keys())[1].upper()}: {i[list(i.keys())[1]]}")
            else:
                print(f"{i[list(i.keys())[0]]}")
        print()






def exercise_list(pathway):
    file = open(pathway, "r")
    exercise_list = file.read()
    file.close()
    return exercise_list

if __name__ == "__main__":
    main()