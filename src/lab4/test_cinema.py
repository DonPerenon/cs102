import unittest

from CinemaClass import Cinema


def find_film_name(index: str):
    with open("/Users/viktorivanov/cs102/src/lab4/films.txt", encoding='utf-8') as films:
        lines = films.readlines()

        dictionary = {}

        for line in lines:
            parts = line.strip().split(',')
            number = parts[0]
            title = parts[1]
            dictionary[number] = title

        # Вывод словаря
    return dictionary[index]


class CinemaTest(unittest.TestCase):

    def test_rec(self):
        cinema = Cinema("/Users/viktorivanov/cs102/src/lab4/history.txt", [2, 4])
        self.assertEqual(cinema.recommendation(), '3')

    def test_ans(self):
        cinema = Cinema("/Users/viktorivanov/cs102/src/lab4/history.txt", [2, 4])
        self.assertEqual(find_film_name(cinema.recommendation()), "Дюна")


if __name__ == "__main__":
    unittest.main()