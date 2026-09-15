# Module for Reading/Writing from/to File

from rich import print
from rich.console import Console
console = Console()

def is_empty():
    with open("data/movie.txt", "r") as f:
        data = f.read()
    if data == "":
        return True
    return False

def save_moive(x):
    with open("data/movie.txt", "a") as movie_file:
        movie_file.write(x)

def view():
    with open("data/movie.txt", "r") as movie_file:
        data = movie_file.readlines()
    return data

def delete(name):
    data = view()
    with open("data/movie.txt", "w") as file:
        for line in data:
            if not line.lower().startswith(name.lower().strip()):
                file.write(line)

def update_watch(name):
    data = view()
    with open("data/movie.txt", "w") as file:
        for line in data:
            if not line.lower().startswith(name.lower().strip()):
                file.write(line)
            else:
                list = line.split("||")
                list[3] = "Watched"
                file.write("||".join(list))

def update_rate(name, rate):
    data = view()
    with open("data/movie.txt", "w") as file:
        for line in data:
            if not line.lower().strip().startswith(name.lower().strip()):
                file.write(line)
            else:
                movie = line.strip().split("||")
                movie[4] = rate
                file.write("||".join(movie) + "\n")




if __name__ == "__main__":
    print("I am storage.py - I handle the reading/writing of file")
    print(view())
