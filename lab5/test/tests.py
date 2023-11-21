from src.main import max_experience
import unittest


class Testing(unittest.TestCase):
    def test1(self):
        with open('career1.in', 'r') as file:
            levels = int(file.readline())
            experience = [list(map(int, file.readline().split())) for _ in range(levels)]

        result = max_experience(levels, experience)

        with open("career1.out", "w") as file_out:
            file_out.write(str(result))

    def test2(self):
        with open('career2.in', 'r') as file:
            levels = int(file.readline())
            experience = [list(map(int, file.readline().split())) for _ in range(levels)]

        result = max_experience(levels, experience)

        with open("career2.out", "w") as file_out:
            file_out.write(str(result))

    def test3(self):
        with open('career3.in', 'r') as file:
            levels = int(file.readline())
            experience = [list(map(int, file.readline().split())) for _ in range(levels)]

        result = max_experience(levels, experience)

        with open("career3.out", "w") as file_out:
            file_out.write(str(result))
