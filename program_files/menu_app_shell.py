"""
Application shell for menu driven app
"""
import sys

def display_menu():
    print(
        """
    StockTracker Menu
    1. Track Watchlist
    2. Add Watchlist 
    3. Delete Watchlist
    4. Edit Watchlist
    5. Exit   
        """
    )

def track():
    pass

def add_list():
    pass

def edit_list():
    pass

def delete_list():
    pass            


actions = {'1' : track, '2' : add_list, '3' : delete_list, '4' : edit_list}

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice in '1234':
            actions[choice]()
        elif choice == '5':
            print("Thank you for using stonktracker!")
            sys.exit(0)
        else:
            print("Please make a valid choice")        




if __name__ == "__main__":
    main()