##########################################################################
#   Project 11 - Gomoku
#
#   class calander
#   class event
#   main
#       main function makes a calander and adds, deletes and lists events in which a person has on the calander
#       function prompts user to a menu 
#       function then makes the user select what they want to do to their calander
#       if the user adds a event it will appear on the calendar list and if the user deletes an event it will be removed from the list
#       the function is ended when the user selects quit
##########################################################################



from p11_calendar import P11_Calendar
from p11_event import P11_Event


CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    '''Return True if the time and duration are valid; return False otherwise. Note that a valid schedule time must start at 6AM at the earlier and end at 5PM at the latest (using 24-hour time). Note that time should be well formed.'''
    time_lst= ["6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]
    dur_lst=[10,20,30,40,50,60]
  
    if time in time_lst:
      if duration in dur_lst:
        return True 
      else:
        return False
    else:
      return False
    
            
def event_prompt():
    '''Prompt for an event; re-prompt until a valid event is entered. Return the event. Prompt for date, time, duration, and cal_type. Hint: the check_time function was created to help here to check if time and duration are valid. The event has an attribute valid to check if the event is valid'''
    event = input("Enter event type ['meeting','event','appointment','other']: ")
                
def main():
    '''This function would fire up the program by creating a Calendar and would present the user with five basic options to operate. You program should accept lower and upper case options.'''
    while True:
      print(MENU)
      menu = input("Select an option: ").lower()
      if menu.lower() == "a":
        date = input("Enter a date (mm/dd/yyyy): ")
        time = input("Enter a start time (hh:mm): ")
        duratation = input("Enter the duration in minutes (int): ")
        event = input("Enter event type ['meeting','event','appointment','other']: ")
        print("Add Event")
        

      
      if menu.lower() == "d":
        print("Delete Event")
        date = input("Enter a date (mm/dd/yyyy): ")
        time = input("Enter a start time (hh:mm): ")

      if menu.lower() == "l":
        print("List Events")
        date = input("Enter a date (mm/dd/yyyy): ")

      if menu.lower() == "q":
        break

      
    
      
if __name__ == '__main__':
     main()
        

        


      