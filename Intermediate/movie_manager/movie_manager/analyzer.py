# Module to analyze the movie details

from . import storage
from rich import print
from rich.console import Console

movies = {}
def file_to_dic():
    data = storage.view()
    for line in data:
        arr = line.strip().split("||")
        movies[arr[0]] = {
            "Genre" : arr[1],
            "Release year" : arr[2],
            "Status" : arr[3],
            "Rating" : arr[4]
        }


def rate_analyzer(rating):
    if rating == 0:
        print('   No rating... you hate it that much?')
    elif rating < 3:
        print('   Oof... that was rough 😭')       
    elif rating < 5:
        print('   Could\'ve been much better 😬')     
    elif rating < 7:
      print('   Meh... just okay 😐')      
    elif rating == 7:
        print('   Pretty good! 👍')
    elif rating == 8:
        print('   Okayyy, that\'s a solid movie! 😎')
    elif rating == 9:
        print('   Wow, you really liked this one! 🔥')
    elif rating == 10:
        print('   Okay, this MUST be one of your favourites! ❤️🎬')


def total_movies():
    total = 0
    data = storage.view()
    for line in data:
        total+=1
    return total

def movie_status():
    watched = 0
    unwatched = 0
    for movie in movies:
        if movies[movie]["Status"] == "Watched":
            watched+=1
        else:
            unwatched+=1
    return watched,unwatched

def highest_rating():
    highest = 0
    name = ""
    for movie in movies:
        if int(movies[movie]["Rating"]) > highest :
            highest = int(movies[movie]['Rating'])
            name = movie
    return name,highest

def lowest_rating():
    lowest = 10
    name = ""
    for movie in movies:
        if int(movies[movie]["Rating"]) < lowest :
            lowest = int(movies[movie]['Rating'])
            name = movie
    return name,lowest

def avg_rating():
    avg = 0
    count = 0
    for movie in movies:
        count += 1
        avg += int(movies[movie]["Rating"])
    avg /= count
    return avg

def get_genres():
    gen = {}
    for movie in movies:
        if movies[movie]["Genre"] in gen:
            gen[movies[movie].get("Genre")] += 1
        else:
            gen[movies[movie]["Genre"]] = 1
    return gen

def smart_recommendation():
    print("[#9fc5e8 bold]\n-------- Smart Movie Recommendation --------[/#9fc5e8 bold]")

    g = input("Enter prefered genre: ").lower().strip()
    rec = []
    count = 0
    for movie in movies:
        if movies[movie]['Genre'].lower().strip() == g and (int(movies[movie]['Rating']) > 7 or movies[movie]["Status"] == 'Unwatched'):
            count+=1
            rec.append(movie)
    if count < 3:
        rec = []
        for movie in movies:
            if movies[movie]['Genre'].lower().strip() == g:
                count+=1
                rec.append(movie)
    count = 1
    for m in rec:
        print(f"{count}. {m}")
        count += 1

def movie_statistics():
    print("[#9fc5e8 bold]\n-------- Movie Statistics --------[/#9fc5e8 bold]")
    w,un = movie_status()
    print("Total Movies:", total_movies())
    print("Watched Movies:", w)
    print("Unwatched Movies:", un)

    name, rating = highest_rating()
    print(f"\nHighest Rated: {name} - {rating}")
    name, rating = lowest_rating()
    print(f"\nLowest Rated: {name} - {rating}")
    print("\nAverage Rated:", avg_rating())
    print("\nMovie by Genre:")
    genre_count = get_genres()
    for i in genre_count:
        print(f"{i} : {genre_count[i]}")

file_to_dic()

if __name__ == "__main__":
    print("I am analyzer.py - I analyze the movie details and statistics.")