
def storyboard():
    # gives story if split in this direction
    print('(first) storyboard in this genre')
    # gets choice for after the story
    userChoice = input('(first) choose 1,2,3')
    
    if userChoice == str(1):
        print('in first choice 1')
    elif userChoice == str(2):
        print('in first choice 2')
    elif userChoice == str(3):
        print('in first choice 3')
    else:
        print('(first) Not a valid input')