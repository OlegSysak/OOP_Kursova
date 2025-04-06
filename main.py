class Game:
    def __init__(self, name, genre, players, duration):
        self.name = name
        self.genre = genre
        self.players = players
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.genre}) - {self.players} гравців, {self.duration} хв"


class GameCatalog:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game_name):
        for game in self.games:
            if game.name.lower() == game_name.lower():
                self.games.remove(game)
                print(f"Гра '{game_name}' видалена з каталогу.")
                return
        print(f"Гра '{game_name}' не знайдена.")

    def edit_game(self, game_name, new_name=None, new_genre=None, new_players=None, new_duration=None):
        for game in self.games:
            if game.name.lower() == game_name.lower():
                if new_name:
                    game.name = new_name
                if new_genre:
                    game.genre = new_genre
                if new_players:
                    game.players = new_players
                if new_duration:
                    game.duration = new_duration
                print(f"Гра '{game_name}' оновлена.")
                return
        print(f"Гра '{game_name}' не знайдена.")

    def get_game(self, game_name):
        for game in self.games:
            if game.name.lower() == game_name.lower():
                return game
        return None

    def show_catalog(self):
        if not self.games:
            print("Каталог порожній.")
        else:
            print("Каталог настільних ігор:")
            for game in self.games:
                print(game)



class GameFilter:
    @staticmethod
    def filter_by_genre(games, genre):
        return [game for game in games if game.genre.lower() == genre.lower()]

    @staticmethod
    def filter_by_players(games, players):
        return [game for game in games if game.players == players]


class GameSorter:
    @staticmethod
    def sort_by_name(games):
        return sorted(games, key=lambda x: x.name)

    @staticmethod
    def sort_by_players(games):
        return sorted(games, key=lambda x: x.players)

    @staticmethod
    def sort_by_duration(games):
        return sorted(games, key=lambda x: x.duration)


class GameCatalogPrinter:
    @staticmethod
    def print_catalog(games):
        if not games:
            print("Каталог порожній.")
        else:
            print("Каталог настільних ігор:")
            for game in games:
                print(game)


class UserInterface:
    def __init__(self, game_catalog):
        self.catalog = game_catalog

    @staticmethod
    def display_menu():
        print(
              "\n------------------------------------"
              "\nМеню:\n"
              "1. Додати гру\n"
              "2. Видалити гру\n"
              "3. Редагувати гру\n"
              "4. Фільтрувати ігри за жанром\n"
              "5. Фільтрувати ігри за кількістю гравців\n"
              "6. Сортувати ігри\n"
              "7. Показати каталог\n"
              "8. Вихід\n"
        )

    def user_input(self):
        while True:
            self.display_menu()

            choice = input("Виберіть дію (1-8): ")

            if choice == "1":
                self.add_game()
            elif choice == "2":
                self.remove_game()
            elif choice == "3":
                self.edit_game()
            elif choice == "4":
                self.filter_by_genre()
            elif choice == "5":
                self.filter_by_players()
            elif choice == "6":
                self.sort_games()
            elif choice == "7":
                self.show_catalog()
            elif choice == "8":
                print("Дякуємо за використання нашої програми!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def add_game(self):
        name = input("Введіть назву гри: ")

        if self.catalog.get_game(name):
            print(f"Гра з назвою '{name}' вже існує в каталозі.")
            return

        genre = input("Введіть жанр гри: ")

        while True:
            try:
                players = int(input("Введіть кількість гравців: "))
                if players < 1:
                    print("Кількість гравців повинна бути більша за 0.")
                    continue
                break
            except ValueError:
                print("Будь ласка, введіть коректне число для кількості гравців.")

        while True:
            try:
                duration = int(input("Введіть тривалість партії в хвилинах: "))
                if duration <= 0:
                    print("Тривалість партії повинна бути більшою за 0 хвилин.")
                    continue
                break
            except ValueError:
                print("Будь ласка, введіть коректну тривалість партії.")

        game = Game(name, genre, players, duration)
        self.catalog.add_game(game)
        print(f"Гра '{name}' додана до каталогу.")

    def remove_game(self):
        game_name = input("Введіть назву гри для видалення: ")
        self.catalog.remove_game(game_name)

    def edit_game(self):
        game_name = input("Введіть назву гри для редагування: ")
        game = self.catalog.get_game(game_name)
        if not game:
            print(f"Гра '{game_name}' не знайдена.")
            return

        new_name = input(f"Введіть нову назву (або залиште порожнім для старої): ")
        if new_name:
            game.name = new_name

        new_genre = input(f"Введіть новий жанр (або залиште порожнім для старого): ")
        if new_genre:
            game.genre = new_genre

        new_players = input(f"Введіть нову кількість гравців (або залиште порожнім для старої): ")
        if new_players:
            while not new_players.isdigit():
                print("Будь ласка, введіть коректне число для кількості гравців.")
                new_players = input(f"Введіть нову кількість гравців (або залиште порожнім для старої): ")
            game.players = int(new_players)

        new_duration = input(f"Введіть нову тривалість партії (або залиште порожнім для старої): ")
        if new_duration:
            while not new_duration.isdigit():
                print("Будь ласка, введіть коректну тривалість партії.")
                new_duration = input(f"Введіть нову тривалість партії (або залиште порожнім для старої): ")
            game.duration = int(new_duration)

        print(f"Гра '{game.name}' оновлена.")

    def filter_by_genre(self):
        genre = input("Введіть жанр для фільтрації: ")
        filtered_games = GameFilter.filter_by_genre(self.catalog.games, genre)
        if filtered_games:
            print("Ігри за жанром:")
            for game in filtered_games:
                print(f"{game.name} ({game.genre}) - {game.players} гравців, {game.duration} хв")
        else:
            print("Ігор з таким жанром не знайдено.")

    def filter_by_players(self):
        while True:
            try:
                players = int(input("Введіть кількість гравців для фільтрації: "))
                filtered_games = GameFilter.filter_by_players(self.catalog.games, players)
                if filtered_games:
                    print("Каталог настільних ігор:")
                    for game in filtered_games:
                        print(f"{game.name} ({game.genre}) - {game.players} гравців, {game.duration} хв")
                else:
                    print("Ігор з такою кількістю гравців не знайдено.")
                break
            except ValueError:
                print("Будь ласка, введіть коректне число для кількості гравців.")

    def sort_games(self):
        print(
              "Як ви хочете сортувати ігри?\n"
              "1. За назвою\n"
              "2. За кількістю гравців\n"
              "3. За тривалістю партії\n"
        )
        criterion = input("Виберіть номер (1-3): ")

        games_list = []

        if criterion == "1":
            games_list = GameSorter.sort_by_name(self.catalog.games)
        elif criterion == "2":
            games_list = GameSorter.sort_by_players(self.catalog.games)
        elif criterion == "3":
            games_list = GameSorter.sort_by_duration(self.catalog.games)

        if games_list:
            GameCatalogPrinter.print_catalog(games_list)
        else:
            print("Невірний вибір для сортування.")

    def show_catalog(self):
        GameCatalogPrinter.print_catalog(self.catalog.games)



if __name__ == "__main__":
    catalog = GameCatalog()
    ui = UserInterface(catalog)
    ui.user_input()