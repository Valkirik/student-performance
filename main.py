import csv

from tabulate import tabulate

paths = ["files/students1.csv", "files/students2.csv"]


# the function return a dict
def read_csv(list_paths: list) -> dict:
    students_grade = {}
    for path in list_paths:
        with open(path, "r", encoding="utf-8") as file:
            # with this we get dicts with keys and values.
            # It is easier for us to work with it
            reader = csv.DictReader(file)
            for i in reader:
                name = i["student_name"]
                grade = i["grade"]
                students_grade.setdefault(name, []).append(float(grade))
    return students_grade


# a list with average scores
def calculate_average_score(dct: dict) -> dict:
    average_score = []
    for i in list(dct.values()):
        i = sum(i) / len(i)
        r = round(i, 1)
        average_score.append(r)
    result = dict(zip(dct.keys(), average_score))
    return result


def sorting(dct: dict) -> dict:
    sorted_result = dict(sorted(dct.items(), key=lambda item: item[1]))
    reversed_dict = reversed(sorted_result)
    descending_order = {key: sorted_result[key] for key in reversed_dict}
    return descending_order


def result_table(files: list):
    data = read_csv(files)
    mid_score = calculate_average_score(data)
    pairs = sorting(mid_score).items()
    table = tabulate(pairs, headers=["student_name", "grade"], tablefmt="github")
    return table


if __name__ == "__main__":
    print(result_table(paths))
