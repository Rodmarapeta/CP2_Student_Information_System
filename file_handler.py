FILE_NAME = "students.txt"

def save_data(names, ages, courses, grades, ids):
    with open(FILE_NAME, "w") as file:
        for i in range(len(names)):
            file.write(f"{ids[i]},{names[i]},{ages[i]},{courses[i]},{grades[i]}\n")

def load_data():
    names, ages, courses, grades, ids = [], [], [], [], []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    ids.append(int(data[0]))
                    names.append(data[1])
                    ages.append(int(data[2]))
                    courses.append(data[3])
                    grades.append(float(data[4]))

    except FileNotFoundError:
        pass

    return names, ages, courses, grades, ids
