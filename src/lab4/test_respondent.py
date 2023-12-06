import unittest
from RespondentClass import Respondent, sort_respondents, group_respondents


class TestRespondent(unittest.TestCase):

    def test_sort_respondents(self):
        respondents = [
            Respondent("Alice", 25),
            Respondent("Bob", 30),
            Respondent("Charlie", 20)
        ]
        sorted_respondents = sort_respondents(respondents)
        self.assertEqual(sorted_respondents[0].full_name, "Bob")
        self.assertEqual(sorted_respondents[1].full_name, "Alice")
        self.assertEqual(sorted_respondents[2].full_name, "Charlie")

    def test_group_respondents(self):
        respondents = [
            Respondent("Alice", 25),
            Respondent("Bob", 30),
            Respondent("Charlie", 20)
        ]
        age_groups = [(0, 20), (21, 25), (26, 30)]
        grouped_respondents = group_respondents(respondents, age_groups)
        self.assertEqual(len(grouped_respondents), 3)


if __name__ == '__main__':
    unittest.main()