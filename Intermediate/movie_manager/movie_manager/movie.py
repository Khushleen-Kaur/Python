# Module to Modify and perform the movie.txt file related operations

from . import storage
from . import analyzer
from rich import print
from rich.console import Console
console = Console()

def add_movie():
    print("[#9fc5e8 bold]\n--------- Add Movie Details ---------[/#9fc5e8 bold]")
    name = input("Enter movie name: ")
    genre = input("Enter genre: ")
    yr = input("Enter release year: ")
    status = input("Enter status (Watched/Unwatched): ")
    rating = input("Enter rating: ")

    storage.save_moive(f"\n{name}||{genre}||{yr}||{status}||{rating}")

    print("Movie Added Successfully!")

def view_all():
    print("[#9fc5e8 bold]\n------------ Movie List ------------[/#9fc5e8 bold]")
    if storage.is_empty():
        print("[red]No movies are included in the list.[/red]")
    else:
        list = storage.view()
        count = 0
        for line in list:
            count += 1
            arr = line.split("||")
            print(f"[cyan bold]{count}. {arr[0]}[/cyan bold]") 
            console.print(f"   Genre: {arr[1]}") 
            console.print(f"   Release Year: {arr[2]}", highlight=False) 
            console.print(f"   Status: {arr[3]}") 
            console.print(f"   Rating: {arr[4].strip()}", highlight=False) 
            analyzer.rate_analyzer(int(arr[4]))
            print()


def remove_movie():
    print("[#9fc5e8 bold]\n--------- Remove Movie Details ---------[/#9fc5e8 bold]")
    name = input("Enter movie name: ")
    storage.delete(name)
    print(f"{name} - Movie Removed Successfully!")

def search_movie():
    print("[#9fc5e8 bold]\n------------ Search Movie ------------[/#9fc5e8 bold]")
    if storage.is_empty():
        print("[red]No movies are included in the list.[/red]")
    else:
        name = input("Enter name of movie: ").lower().strip()
        list = storage.view()
        count = 0
        for line in list :
            if name in line.lower().strip():                    
                count += 1
                arr = line.split("||")
                print(f"[cyan bold]{count}. {arr[0]}[/cyan bold]") 
                console.print(f"   Genre: {arr[1]}") 
                console.print(f"   Release Year: {arr[2]}", highlight=False) 
                console.print(f"   Status: {arr[3]}") 
                console.print(f"   Rating: {arr[4]}", highlight=False) 

        if count == 0: print("[red]Movie not found![/red]")

def mark_watched():
    print("[#9fc5e8 bold]\n-------- Mark Movie as Watched --------[/#9fc5e8 bold]")
    name = input("Enter movie name: ")
    storage.update_watch(name)
    print(f"{name} Marked as Watched!")
    
def rate_movie():
    print("[#9fc5e8 bold]\n---------- Rate Movie ----------[/#9fc5e8 bold]")
    name = input("Enter movie name: ")
    rate = input("Enter movie rating: ")
    storage.update_rate(name, rate)
    analyzer.rate_analyzer(int(rate))
    print("Rating Modified!")





if __name__ == "__main__":
    print("I am movie.py - I Modify and perform movie.txt file related operations")
    view_all()
    # search_movie()
    # add_movie()
    # remove_movie()
    # mark_watched()
    # rate_movie()
    # view_all()
