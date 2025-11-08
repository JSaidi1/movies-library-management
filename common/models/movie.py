class Movie:
    id = 30

    def __init__(self, title:str, production_year:int, genre:str, age_limit:int):
        self.title = title
        self.production_year = production_year
        self.genre = genre
        self.age_limit = age_limit

        Movie.id += 1

    def __str__(self):
        return f"Movie: identifier: {self.id} - title: {self.title} - production year: {self.production_year} - genre: {self.genre} - age limit: {self.age_limit}"
    


if __name__=="__main__":
    print("in /write/movie.py")