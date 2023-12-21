########################################################################
# Computer project 8
#
# Lists & dictionary analysis 
#
# prompts user for .csv file
# .cvs file is then turned into a read file
# file output prints the data for diabetes in each region and the the countrys within the region
# The file then proceeds to print the max and minimum of each regions lowest and highest country
# After printing the max and min the file then terminates with closing statements
#
########################################################################

import csv
import pprint
from operator import itemgetter

def open_file():
    '''Prompts for a file name and continues to prompt until a file is correctly opened.'''
    while True:
      try:
        file_name = input("Input a file: ") #prompts to open the file
        fp = open(file_name, encoding='utf-8')
        return fp
      except FileNotFoundError:
        print("Error: file does not exist. Please try again.")
    return fp

def max_in_region(D,region):
    '''Find the maximum per-capita diabetes in the region.'''
    lists = D[region] 
    sorted_l = sorted(lists, key=itemgetter(3,0))
    max_country = sorted_l[-1][0]
    max_capita = sorted_l[-1][3]
    return (max_country, max_capita)

def min_in_region(D,region):
    '''Find the minimum per-capita diabetes in the region.'''
    lists = D[region]
    sorted_l = sorted(lists, key=itemgetter(3,0))
    i = 0
    while sorted_l[i][3] <= 0:
        i += 1 #incriments i by one
    min_country = sorted_l[i][0]
    min_capita = sorted_l[i][3]
    return (min_country, min_capita)

def read_file(fp):
    '''. Read the file referenced by the parameter. Use the csv module’s reader method. Each line of the file is data for a region or country. The dictionary key will be the region (a string); the value will be a list of list of data; put the country’s information into a list and then assign that list to your master dictionary. Remember to initialize the master dictionary to empty before the loop.'''
    reader = csv.reader(fp)
    next(reader)
    d = {} #empty string for master dictionary
    for row in reader: 
      region = row[1] #region values are in row one
      country = row[2]
      diabetes = row[9].replace(',','') #makes sure to replace the comma with an empty space
      population = row[5].replace(',','')
      if diabetes == "-":
        continue
      if population == "-":
        continue
      info = [country, float(diabetes), float(population)]
      if region in d:
        d[region] += [info]
      else:
        d[region] = [info]
      d[region] = sorted(d[region])
    return d

def add_per_capita(D):
    '''Calculate diabetes per capita for each country and region by simply dividing the diabetes value by the population value (they are both in the same units—thousands). Append the per-capita value onto each country’s list'''
    for region in D:
      final_list = []
      lists = D[region]
      for list in lists:
        diabetes = list[1]
        population = list[2]
        if population == 0:
          list.append(0.0)
        else:
          list.append(diabetes/population)
        final_list.append(list)
      D[region] = final_list
    return D #returns the dictionary

def display_region(D,region):
    '''Display the summary data for the region (string) followed by a table with the data for each country. The summary data is in the list of country data—its “country name” is the region name.'''
    lists = D[region]
    sorted_D = sorted(D[region], key=itemgetter(1), reverse = True)
    lst = sorted_D[0]
    
    print("Type1 Diabetes Data (in thousands)")
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format(*lst))
    print()
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))

    sorted_lists=sorted(D[region], key=itemgetter(3),reverse=True)
    for lst in sorted_lists:
        if lst[0] == region:
            continue # makes sure to continue if condition is true
        print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(*lst))
    pass

def main():
    '''It’s the main driver of the program. It doesn’t have any parameters. It opens and reads a file and then it calls the other functions.'''
    fp = open_file() #opens the file 
    md = add_per_capita(read_file(fp)) 
    for region in md: #for loop repeats the information below until program terminates 
      display_region(md, region) 
      print("\nMaximum per-capita in the {} region".format(region))
      print("{:<37s} {:>11s}".format("Country","Per Capita"))
      print("{:<37s} {:>11.5f}".format(*max_in_region(md,region)))
      print("\nMinimum per-capita in the {} region".format(region))
      print("{:<37s} {:>11s}".format("Country","Per Capita"))
      print("{:<37s} {:>11.5f}".format(*min_in_region(md,region)))
      print("-"*72)
    print("\n Thanks for using this program!") #ending program statements
    print("Have a good day!") 
      
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute. 
      
if __name__ == "__main__":

    main()