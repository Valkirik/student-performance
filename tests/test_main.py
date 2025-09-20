import pytest
from main import read_csv, calculate_average_score, sorting, result_table


# tmp_path let us create a temporary file CSV
def test_read_csv(tmp_path):
    file_path = tmp_path / "students.csv"
    file_path.write_text("student_name,grade\nAlice,5\nBob,4\n", encoding="utf-8")

    rows = read_csv([file_path])

    assert rows.keys() == {"Alice", "Bob"}
    assert rows["Alice"] == [5.0]
    assert rows["Bob"] == [4.0]


def test_calculate_average_score():
    data = {"Alice": [5, 4, 5], "Bob": [3, 4, 3]}
    result = calculate_average_score(data)
    assert result == {
        "Alice": round((5 + 4 + 5) / 3, 1),
        "Bob": round((3 + 4 + 3) / 3, 1),
    }


def test_sorting():
    data = {"Alice": 4.0, "Bob": 3.1, "Max": 5.0}
    result = sorting(data)
    assert result == {"Max": 5.0, "Alice": 4.0, "Bob": 3.1}


def test_result_table(tmp_path):
    file_path_1 = tmp_path / "students1.csv"
    file_path_1.write_text("student_name,grade\nAlice,5\nBob,4\n", encoding="utf-8")
    file_path_2 = tmp_path / "students2.csv"
    file_path_2.write_text("student_name,grade\nMax,3\nOlga,2\n", encoding="utf-8")

    out = result_table([file_path_1, file_path_2])
    lines = out.splitlines()

    assert "student_name" in lines[0] and "grade" in lines[0]
    assert "Alice" in lines[2]
    assert "Bob" in lines[3]
    assert "Max" in lines[4]
    assert "Olga" in lines[5]
