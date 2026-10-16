def exercise_list(pathway):
    file = open(pathway, "r")
    exercise_list = file.read()
    file.close()
    return exercise_list
