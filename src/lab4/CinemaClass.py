from collections import Counter



"""
    Counter нам нужен для того, чтобы понять, какой фильм наиболее просматриваемый
    среди всех пользователей
"""


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
    print(dictionary[index])


class Cinema:

    """
        Проинициализируем файл с фильмами, которые посмотрели пользователи
         и массив с фильмами, который посмотрел текущий юзер (рекомендацию для которого мы и делаем!!!)
    """

    def __init__(self, history, current_user):
        self.current_user = current_user
        self.data = {}
        self.read_file(history)

    def read_file(self, history):
        with open(history) as films:
            movies = films.readlines()
            for user, movie in enumerate(movies, start=1):
                self.data[user] = [int(i) for i in movie.strip().split(',')]

    def print_database(self):
        for user, movies in self.data.items():
            print(f'Юзер {user} посмотрел фильмы {movies}')

    def recommendation(self) -> str:

        all_films = [film for sublist in self.data.values() for film in sublist]
        most_common_movies = Counter(all_films)

        recommendation_users = {}
        set_2 = set(self.current_user)

        for user in self.data.keys():
            set_1 = set(self.data.get(user))

            same = set_1.intersection(set_2)

            if len(same) >= len(set_1) / 2:
                recommendation_users[user] = [int(i) for i in self.data.get(user)]
        perhaps_rect = list(set(sum(list(recommendation_users.values()), [])).difference(set_2))

        min_distance = float('inf')
        rec_film = ''

        for sym1 in perhaps_rect:
            for sum2 in list(most_common_movies.keys()):
                distance = abs(perhaps_rect.index(sym1) - list(most_common_movies.keys()).index(sum2))
                if distance < min_distance:
                    min_distance = distance
                    rec_film = str(sym1)

        return rec_film


if __name__ == "__main__":
    eagle = Cinema("/Users/viktorivanov/cs102/src/lab4/history.txt", [2, 4])
    find_film_name(str(eagle.recommendation()))