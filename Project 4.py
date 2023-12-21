#######################################################
# DO NOT DELETE: added by instructor for grading
import sys
def input( prompt=None ):
    ''' Echo the input of the test to the output.
    If you delete this function you will not pass the test.
    Also, the starter code for Spyder should start from the import pylab
    statement.
    '''
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str
################################################################################
#your header goes here

import pylab  
def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
    
def open_file():
    '''You fill in the doc string'''
    while True:
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
        try:
            if not (int(year_str) <= 2015 and int(year_str) >= 1990) : raise ValueError
        except ValueError:
            print("Error in year. Please try again.")
            continue
        try:
            file = open("year" + year_str + ".txt")
            return file
        except FileNotFoundError:
            print(f"Error in file name: year{year_str}.txt  Please try again.")
            continue
        
def read_file(fp):
    '''You fill in the doc string'''
    lines = list(fp.readlines())
    return lines[2:]
        
def find_average(data_lst):
    '''You fill in the doc string'''
    noOfPeople = int(str(data_lst[-1].split()[4]).replace(",",""))
    sum = 0.0
    for x in data_lst:
        t = x.split()
        sum += float(t[6].replace(",", ""))
    return sum/noOfPeople
    
def find_median(data_lst):
    '''You fill in the doc string'''
    m = 9999999999
    avIncome = 0
    for x in data_lst:
        t = x.split()
        if abs(float(t[5]) - 50) < m:
            m = abs(float(t[5]) - 50)
            avIncome = float(t[7].replace(",", ""))

    return avIncome
        
def get_range(data_lst, percent):
    '''You fill in the doc string'''
    for x in data_lst:
      t = x.split()
      if float(t[5]) >= percent:
        return (float(t[0].replace(",", "")), float(t[2].replace(",", ""))), float(t[5]), float(t[7].replace(",", ""))
        

def get_percent(data_lst,salary):
    '''You fill in the doc string'''
    for x in data_lst[:-1]:
      t = x.split()
      if salary < float(t[2].replace(",", "")) and salary >= float(t[0].replace(",", "")):
        return (float(t[0].replace(",", "")), float(t[2].replace(",", ""))), float(t[5])
    return (float(t[0].replace(",", "")), float("inf")), float(t[5])
    

def main():
    file = open_file()
    year = int(file.name[4:8])
    data_list = read_file(file)
    avg = find_average(data_list)
    median = find_median(data_list)
    print("\nYear  Mean           Median         ")
    print(year," ${:<13,.2f}".format(avg),"${:<13,.2f}".format(median),"")

    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        x_vals = list()
        y_vals = list()
        for x in data_list[:40]:
            t = x.split()
            x_vals.append(float(t[5]))
            y_vals.append(float(t[0].replace(",", "")))
            do_plot(x_vals, y_vals, year)
    while True:
      choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: " )
      while choice != "r" and choice != "p" and choice != "":
        print("Error in selection.")
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: " )
      if choice == "r":
        percent = float(input("Enter a percent: "))
        if percent <= 100 and percent >= 0:
          print("\n{:4.2f}% of incomes are below ${:<13,.2f}.".format(percent, get_range(data_list, percent)[0][0]))
        else:
          print("Error in percent. Please try again")
      else:
        if choice == "p":
          income = float(input("Enter an income: "))
          if income >= 0:
            print("\nAn income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(income, get_percent(data_list, income)[1]))
          else:
            print("Error: income must be positive")

        elif choice == "":
          print("")
          break


if __name__ == "__main__":
    main()