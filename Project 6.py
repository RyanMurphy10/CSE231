########################################################################
# Computer project 6 
#
# Lists & data analysis 
#
# prompts user for .csv file
# .cvs file is then turned into a master list
# user chooses from list of prompts what to do
# A. displays christmas songs
# B. display songs by peak rank
# C. display songs by weeks on the charts
# D. display scores by calculated rank
# Q. terminates the program
#
########################################################################

import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
a,b,c,d = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program\n "

#the prompt to ask the user for an option
PROMPT = "\nEnter one of the listed options: "

def get_option():
    '''This function prompts the user with a menu of options'''
    while True:
      print(OPTIONS) #prints prompt statement above
      options = input("\nEnter one of the listed options: ")
      while options.lower() != "a" and options.lower() != "b" and options.lower()       != "c" and options.lower() != "d" and options.lower() != "q":
        print("Invalid option!")
        print("Try again")
        options = input("\nEnter one of the listed options: ")
      if options.lower() == 'a':
        return "a" #Christmas songs
      if options.lower() == 'b':
        return "b" #peak rank
      if options.lower() == 'c':
        return "c" #weeks on chart
      if options.lower() == 'd':
        return "d" #scores by calculated rank
      elif options.lower() == 'q':
        return "q" #quits program
          
    pass

def open_file():
    '''this function continuously prompts the user for a file name and returns the file.'''
    while True: #prompts the user to input a file
      try:
        file_name = input("\nEnter a file name: ")
        fp = open(file_name)
        return fp
      except FileNotFoundError:
        print("\nInvalid file name; please try again.")
    return fp

def read_file(fp):
    '''This function reads the csv file that was opened and formats it'''
    master_list = []
    reader = csv.reader(fp)
    next(reader)

    for row in reader:
      list_to_add = []
      for item in range(6): #needs to be 6 so it prints correctly
        if item < 2:
          list_to_add.append(row[item])
        else:
          try:
            list_to_add.append(int(row[item]))
          except:
            list_to_add.append(-1)
      master_list.append(list_to_add)
    return master_list
        
def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    '''This function sorts the christmas songs from the master list'''
    # Keywords used to find christmas songs in get_christmas_songs()
    return_list = []
    for song_list in master_list:
      song_name = song_list[0].lower()
      for words in CHRISTMAS_WORDS:
        if words in song_name:
          return_list.append(song_list)

    return_list.sort()
    return return_list 
        
def sort_by_peak(master_list):
    '''This function returns a sorted version of the master list by peak rank'''
    new_list = [i for i in master_list if i[4] != -1]
    new_list.sort(key=itemgetter(4)) 
    return new_list

def sort_by_weeks_on_list(master_list):
    '''This function returns a sorted version of the master list by weeks on the top 100'''
    new_list = [i for i in master_list if i[5] != -1]
    new_list.sort(key=itemgetter(5))
    new_list.reverse() #prints in reverse order
    return new_list
        
def song_score(song):
    '''ranks songs by how long they have been on the chart, their peak rank, their current rank, and rank delta '''
    peak_rank = 100 - song[4]
    current_rank = 100 - song[2]
    weeks_on_chart = song[5]
    rank_delta = song[2] - song[3]
    if song[4] == -1:
      peak_rank = -100
    if song[2] == -1:
      current_rank = -100
      
    return a * peak_rank + b * rank_delta + c * weeks_on_chart + d * current_rank

def sort_by_score(master_list):
    '''This function returns a sorted version of the master_list ranked by the value returned by the score_song function in descending order'''
    master_list.sort(key=song_score)
    master_list.reverse()
    return master_list
    
def main():
    '''It opens and reads a file and then it calls the other functions in a loop.Using get_option it gets an option that indicates which function to call.'''
    print("\nBillboard Top 100")
    fp = open_file()
    master_list = read_file(fp)
    print_data(master_list)
    options_selected = get_option()
    while options_selected != "q":
      if options_selected == "a":
        christmas_songs = get_christmas_songs(master_list) 
        print_data(christmas_songs)
        percentage = len(christmas_songs) / len(master_list)
        percentage = percentage * 100
        percentage = int(percentage)
        if percentage == 0:
          print('None of the top 100 songs are Christmas songs.')
        else:
          print("")
          print(f'{(percentage)}% of the top 100 songs are Christmas songs.') #formats so it prints correctly
      elif options_selected == "b":
        print_data(sort_by_peak(master_list))
      elif options_selected == "c":
        print_data(sort_by_weeks_on_list(master_list))
      elif options_selected == "d":
        print_data(sort_by_score(master_list))
      options_selected = get_option()
    print("\nThanks for using this program!\nHave a good day!\n")

    pass

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main() 