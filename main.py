import csv

from tabulate import tabulate

paths = ["files/students1.csv", "files/students2.csv"]

students_grade = {}

for path in paths:
    with open(path, "r", encoding="utf-8") as file:
        # with this we get dicts with keys and values.
        # It is easier for us to work with it
        reader = csv.DictReader(file)
        for i in reader:
            name = i["student_name"]
            grade = float(i["grade"])
            students_grade.setdefault(name, []).append(grade)

all_grades = students_grade.values()

# a list with average scores
average_score = []
for i in all_grades:
    i = sum(i) / len(i)
    average_score.append(i)

# a list with the names
names = list(students_grade.keys())

# we have transformed it into a dict
result = dict(zip(names, average_score))


sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))
reversed_dict = reversed(sorted_result)
descending_order = {key: sorted_result[key] for key in reversed_dict}

pairs = descending_order.items()

print(tabulate(pairs, headers=["students", "grade"], tablefmt="github"))
