class InvalidAgeLimitException(Exception):
    def __init__(self, message, age_limit):
        super().__init__(message)
        self.message = message
        self.age_limit = age_limit

    def display_exception(self):
        print(f"{self.message} : {self.age_limit}")

class InvalidGenreException(Exception):
    def __init__(self, message, genre):
        super().__init__(message)
        self.message = message
        self.genre = genre

    def display_exception(self):
        print(f"{self.message} : {self.genre}")

class InvalidTitleException(Exception):
    def __init__(self, message, title):
        super().__init__(message)
        self.message = message
        self.title = title

    def display_exception(self):
        print(f"{self.message} : {self.title}")

class InvalidYearException(Exception):
    def __init__(self, message, year):
        super().__init__(message)
        self.message = message
        self.year = year

    def display_exception(self):
        print(f"{self.message} : {self.year}")