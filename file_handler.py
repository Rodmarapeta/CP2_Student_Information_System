FILE_NAME = "students.txt"

def save_data(names, ages, courses, grades):
    file = open(FILE_NAME, "w")

    for i in range(len(names)):
        file.write(f"{names[i]},{ages[i]},{courses[i]},{grades[i]}\n")

    file.close()


def load_data():
    names = []
    ages = []
    courses = []
    grades = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                names.append(data[0])
                ages.append(int(data[1]))
                courses.append(data[2])
                grades.append(float(data[3]))

        file.close()

    except FileNotFoundError:
        pass

    return names, ages, courses, grades