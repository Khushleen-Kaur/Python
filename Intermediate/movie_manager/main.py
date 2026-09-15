# Main Controller of movie manager - By Khushleen kaur

# ====================================
#        🎬 MOVIE MANAGER
# ====================================

import movie_manager.movie as mov
import movie_manager.analyzer as ana
import movie_manager.storage 
from rich import print
def main():

    while(True):
        print("[#ade8f4 on #00072d bold]\n=============== Movie Manager ============[/#ade8f4 on #00072d bold]")
        print("1. Add Movie")
        print("2. View all Movie")
        print("3. Search Movie")
        print("4. Mark Movie as Watched")
        print("5. Rate Movie")
        print("6. Remove Movie")
        print("7. Movie statistics")
        print("8. Get Recommendation")
        print("9. Exit")

        choice = int(input("Enter choice: "))
        if choice == 9:
            print("[#ade8f4 bold]======= Exiting =======[/#ade8f4 bold]")
            break

        match ( choice):
            case 1:
                mov.add_movie()
            case 2:
                mov.view_all()
            case 3:
                mov.search_movie()
            case 4:
                mov.mark_watched()
            case 5:
                mov.rate_movie()
            case 6:
                mov.remove_movie()
            case 7:
                ana.movie_statistics()
            case 8:
                ana.smart_recommendation()

if __name__ == "__main__":
    main()