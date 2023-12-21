########################################################################
# Computer project 7 
#
# Lists & data analysis 
#
# prompts user for .csv file
# .cvs file is then turned into a read file
# user chooses from list of prompts what to do
# (1) Display regime history
# (2) Display allies
# (3) Display chaotic regimes 
# Q. terminates the program
#
########################################################################

import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
#key words 

MENU='''\nRegime Options: 
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''
#MENU prompts the options of the program.

def open_file():
    '''this function continuously prompts the user for a file name and returns the file.'''
    while True: #prompts the user to input a file
      try:
        file_name = input("Enter a file: ")
        fp = open(file_name)
        return fp
      except FileNotFoundError:
        print("File not found. Please try again.")
    return fp

def read_file(fp):
    '''This function reads the csv file that was opened and formats it.'''
    reader = csv.reader(fp)
    next(reader) #skips the header line
    country_name = ""
    regime = []
    countries, regimes = [], []

    for row in reader:
      if country_name == "":
        country_name = row[1] 
        regime.append(int(row[4]))
      elif country_name != row[1]:
        countries.append(country_name)
        regimes.append(regime)
        regime = []
        country_name = row[1]
        regime.append(int(row[4]))
      else:
        regime.append(int(row[4]))
    countries.append(country_name)
    regimes.append(regime)
    
    return countries, regimes 
    
def history_of_country(country,country_names,list_of_regime_lists):
    '''This function wants to figure out the dominant regime in a country.'''
    for x in range(len(country_names)):
      if country == country_names[x]:
        regime = list_of_regime_lists[x]
        regime_list = [regime.count(0),regime.count(1),regime.count(2),regime.count(3)]
        ans = regime_list.index(max(regime_list))
        return REGIME[ans]

def historical_allies(regime,country_names,list_of_regime_lists):
    '''which countries are historical allies in that they have the same political ideology that is the most dominant in their history'''
    ret = []
    
    for x in range(len(country_names)):
      if regime == history_of_country(country_names[x], country_names, list_of_regime_lists):
        ret.append(country_names[x])
        
    return ret

def top_coup_detat_count(top, country_names,list_of_regime_lists):       
    '''which countries had the most coups in their history.'''
    ret = []

    for x in range(len(country_names)):
      country = country_names[x]
      regimes = list_of_regime_lists[x]
      current_regime = regimes[0]
      coups = 0 #sets value at 0
      for r in regimes:
        if current_regime != r:
          coups += 1 #incriments coups by 1
          current_regime = r
      ret.append((country,coups))
    ret = sorted(ret, key=lambda x: (-x[1],x[0]))
    return ret[:top]
              
def main():
    '''This function is the starting point of the program. The program starts by opening the file and creating the two main lists then print the menu. Afterward, in an endless loop, the user is prompted for options.'''
    fp = open_file() #opens file from the open file function
    countries, regimes = read_file(fp)
    while True: # repeats the options in the main function
      print(MENU)
      options = input("Input an option (Q to quit): ")
      if options.lower() == '1': #first option
        country = input("Enter a country: ")
        while country not in countries: # repeats until a valid country is entered from the csv files
          print("Invalid country. Please try again.")
          country = input("Enter a country: ")
        regime = history_of_country(country, countries, regimes)
        vowels = ['A','E','I','O','U']
        if regime[0] in vowels: #makes sure to use an "a" or "an" in print statement 
          print("\nHistorically",country,"has mostly been an", regime)
        else:
          print("\nHistorically",country,"has mostly been a", regime)
      if options.lower() == '2': #second option
        regime = input("Enter a regime: ")
        while regime not in REGIME:
          print("Invalid regime. Please try again.")
          regime = input("Enter a regime: ")
        allies = historical_allies(regime,countries,regimes)
        str = ""
        for country in allies:
          str += country + ", "
        str = str[:-2]
        print("\nHistorically these countries are allies of type:",regime)
        print("")
        print(str)
      if options.lower() == '3': #third option
        coups = input("Enter how many to display: ")
        while not coups.isnumeric() or int(coups) < 1: #makes sure input is a number and also makes sure it is a integer
          print("Invalid number. Please try again.")
          coups = input("Enter how many to display: ")
        overthrown = top_coup_detat_count(int(coups), countries,regimes) 
        print("\n{: >25} {: >8}\n".format("Country", "Changes"))
        for country in overthrown:
          print("{: >25} {: >8}".format(country[0],country[1]))
      elif options.lower() == 'q': #quit option, terminates program
        print("The end.")
        break
        
if __name__ == "__main__": 
    main() 