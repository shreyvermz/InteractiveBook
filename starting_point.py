import sys
sys.path.append(r"C:\Users\Shrey.Verma\stuff")
from interactive_book.InteractiveBook.first import storyboard

def menu():
    
    quit_holder = False
    moved_on = False
    
    print('Welcome to Shrey\'s Interactive Story')
    
    print('(starting point) tell story')
    # choose scenario
    choice = input('(starting point) Choose scenario 1, 2, or 3: ')
    # sends us to one genre
    if choice == str(1):
            storyboard()
    elif choice == str(2):
            pass
    elif choice == str(3):
            pass
    else:
            print('(starting point) Goodbye')
###########################################################            
menu()