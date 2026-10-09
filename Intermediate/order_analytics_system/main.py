from utils import analysis 
from utils import helper as hel
from rich import print
from rich.console import Console

console = Console()

def main():
    while(True):
        print("\n[bold #9A9AEB]========== Order Analytics System ==========[/bold #9A9AEB]")
        console.print("[not bold #E6E6E6]1. Sales analysis[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]2. Category analysis[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]3. Customer analysis[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]4. Time wise analysis[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]5. Search & Filter Orders[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]6. View Orders[/not bold #E6E6E6]")
        console.print("[not bold #E6E6E6]7. Exit[/not bold #E6E6E6]")
        try:
            with hel.Choice() as choice:
                if choice == 7:
                    print("[italic #FF5C5C]Existing System...[/italic #FF5C5C]")
                    break
                match choice:
                    case 1:
                        analysis.sales_analysis()
                    case 2:
                        analysis.category_analysis()
                    case 3:
                        analysis.customer_analysis()
                    case 4:
                        analysis.time_analysis()
                    case 5:
                        analysis.search()
                    case 6:
                        analysis.view_orders()
                    case _:
                        print("[italic #FF5C5C]Please, Enter a choice between (1 - 7).[/italic #FF5C5C]")
        except ValueError:
            print("[italic #FF5C5C]Please, Enter a valid choice.[/italic #FF5C5C]") 

if __name__ == "__main__":
    main()