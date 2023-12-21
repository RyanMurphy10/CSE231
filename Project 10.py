###################################
#     Computer Project #10
#
#     Streets and Alleys Game
#      setup game
#      ask for moves
#      error check
#      show game board after each move
#      end if won or "q" is hit
####################################

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
                
def initialize():
    '''That function has no parameters. It creates and initializes the tableau and foundation, and then
returns them as a tuple, in that order. This corresponds to rule 1 in the game rules:'''
    stock = cards.Deck()    #creates a deck of cards
    stock.shuffle()  #shuffels the deck of cards
    foundation = [[],[],[],[]]
    tableau = [[],[],[],[],[],[],[],[]]   
    for i in range(7):
            tableau[0].append(stock.deal())
    for i in range(6):
        tableau[1].append(stock.deal())
    for i in range(7):
            tableau[2].append(stock.deal())
    for i in range(6):
        tableau[3].append(stock.deal())
    for i in range(7):
            tableau[4].append(stock.deal())
    for i in range(6):
        tableau[5].append(stock.deal())
    for i in range(7):
            tableau[6].append(stock.deal())
    for i in range(6):
        tableau[7].append(stock.deal())  
    return  tableau, foundation
  
def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    #To get the left bars to line up we need to
    #find the length of the longest even-indexed tableau list,
    #i.e. those in the first, leftmost column
    #The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    #display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    #display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] #even index
        right_lst = tableau[2*i + 1] #odd index
        #first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  #index
        for c in left_lst:  #cards in even-indexed pile
            s += "{} ".format(c)
        #display the even-indexed cards; the "+3" is for the index, colon and space
        #the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        #so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        #next print the foundation
        #get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        #print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  #end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d):
    '''makes sure it is valid to move from one tableua deck to another tableua deck'''
    if 1 <= int(s) <= 4:
        if 1 <= int(d) <=4:
            if len(tableau[int(d) - 1]) == 0 and len(tableau[int(s) - 1]) != 0:
                return True    #makes sure to column is empty and from column isn't empty
    return False
      
def move_tableau_to_tableau(tableau,s,d):
    '''add docstring here'''
    m = valid_tableau_to_tableau(tableau,s,d)#calls the validate move function to make sure that the move is valid.
    if m == True:#checks for a valide move
        card_move=tableau[s].pop()#pops the card out of the list of cards
        tableau[d].append(card_move)#appends the poped card to its new list of cards.
        return True
    else:
        return False


def valid_foundation_to_tableau(tableau,foundation,s,d):
   '''makes sure that it is ok to move a card from the foundation deck to the tableau deck'''
   try:
        cards_move = foundation[s]
        cards_dest = tableau[d][-1]
        if len(foundation[s]) == 0:
            if cards_move.rank() == 1:
                return True
        if cards_move.suit() == tableau[d][-1].suit():
            if tableau[d][-1].rank() + 1 == cards_move.rank():
                return True
   except:
        return False
   return True

def move_foundation_to_tableau(tableau,foundation,s,d):
    '''moves a card in the foundation deck to a card in one of the tableau decks'''
    cards = []
    m = valid_foundation_to_tableau(tableau,foundation,s,d)# must call the check sequence to make sure that the line can be put into the foundantion when the code detects it should .
    if m == True:#checks for a valide move
        card_move=foundation[s].pop()#pops the card out of the list of cards
        tableau[d].append(card_move)#appends the poped card to its new list of cards.
        return True
    else:
        return False
    

def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''makes sure if a card can be moved from the tableau deck to the foundation deck'''
    try:
        cards_move=tableau[s][-1]
        cards_dest=foundation[d]
        if len(foundation[d])==0:
            if cards_move.rank() == 1:
                return True
        if cards_move.suit() == foundation[d][-1].suit(): 
                if foundation[d][-1].rank() + 1 == cards_move.rank():
                    return True
    except IndexError:
        return False
   
    return False
    
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''function moves cards from the 8 tableau decks to one of the 4 foundation decks'''
    cards = []
    m = valid_tableau_to_foundation(tableau,foundation,s,d)# must call the check sequence to make sure that the line can be put into the foundantion when the code detects it should .
    if m == True:#checks for a valide move
        card_move=tableau[s].pop()#pops the card out of the list of cards
        foundation[d].append(card_move)#appends the poped card to its new list of cards.
        return True
    else:
        return False
       
def check_for_win(foundation):
    '''That function checks to see if the foundation is full. It returns True, if the foundation is full and
False, otherwise. '''
    if len(foundation[0])+len(foundation[1])+len(foundation[2])+len(foundation[3]) == 52:
     print("You won!\n")
     return True
    else:
     return False

def get_option(s,d):
    '''That function takes no parameters. It prompts the user for an option and checks that the input
supplied by the user is of the form requested in the menu. Valid inputs for options are described
in item (bullet) 1 of the specifications. If the input is not of the required form, the function prints
an error message "Error in option:" followed by the option entered by the user and
returns None.'''
    s = []
    d = []
    while True:
     print(MENU)
     menu = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): ")
     while menu != (f"MTT, {s} {d}") and menu != ("MTF",{s}, {d}) and menu != ("MFT",{s}, {d}) and menu.lower() != "u" and menu.lower() != "r" and menu.lower() != "h" and menu.lower() != "q": #repeats if wrong input
       print("Incorrect choice.  Please try again.")
       print(MENU)
       menu = input("\n    Choice: ")
       menu = input("\nEnter one of the listed options: ")
     if menu.lower() == ("MTT",{s}, {d}):
      return ("MTT",{s}, {d}) 
     if menu.lower() == ("MTF",{s}, {d}):
       return ("MTF",{s}, {d}) 
     if menu.lower() == ("MFT",{s}, {d}):
      return ("MFT",{s}, {d})
     if menu.lower() == 'u':
       return "u" 
     if menu.lower() == 'r':
       return "r"
     if menu.lower() == 'h':
       return "h"
     elif menu.lower() == 'q':
       return "q"      
       
def main(): 
    '''add docstring here'''
    s = []
    d = []
    print("\nWelcome to Streets and Alleys Solitaire.")
    tab,found=initialize()
    print()
    display(tab,found)
    options_selected = get_option("s","d")
    while options_selected != "q":
     if options_selected == (f"MTT, {s} {d}"):
       display(tab,found)
     if options_selected == (f"MTF, {s} {d}"):
       display(tab,found)
     if options_selected == (f"MFT, {s} {d}"):
       display(tab,found)
     if options_selected == "u":
       display(tab,found)
     if options_selected == "r": 
       display(tab,found)
     if options_selected == "u":
       display(tab,found)
     if options_selected == "h":
       print(MENU)
    print("\nThank you for playing.") #closing statement 

if __name__ == '__main__':
     main()