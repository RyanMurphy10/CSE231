class P11_Calendar():
    def __init__(self):
        '''Initialize the public attribute event_list (which is a list of events) to an empty list.'''
        self.event_list = []
        
    def add_event(self,e):
        '''Append event e to the list of events attribute if the event doesn’t conflict with any events already in the list. Return False if there is a conflict; return True otherwise. Hint: the event get_time_range() method was created to assist here. It returns the range of time for the event. Draw the ranges in a piece of paper and try to find the cases at which 2 different ranges can overlap.'''
        
        start, end = e.get_time_range()
        if not self.event_list:
          self.event_list.append(e)
          return True
        for s in self.event_list:
          strt, ed = s.get_time_range()
          if e.date == s.date:
            if (start in range(strt, ed+1)) or (end in range(strt, ed+1)): 
              return False
        self.event_list.append(e)
        return True

    def delete_event(self,date,time):
        '''Delete the event at the specified date and time.
Hint: find the index of the specified event and use the list del command.
Return False if unsuccessful, e.g. didn’t find an event at that date and time; return True otherwise.'''
        valid_event = False
        if valid_event not in range(self.event_list):
          return False
      
        return True

    
    def day_schedule(self,date):
        '''Return a sorted list of events on the date in the date parameter by time in ascending order. Return an empty list if the date is not well formatted.'''
      
      date_lst=[]
      for i in range(len(self.event_list)):
        for date in i:
          date_lst.append(i)

      return sorted(date_lst)
           
    def __str__(self):
        '''Return a string that has an event on each line. Have one header line: 'Events in Calendar:\n' Hint: str(e) where e is an event calls the event __str__() method Note that __str__ method should return a string. The newline character is '\n'''
        
        print("Events in Calendar:\n")
        for i in self.event_list:
          print(i[0])

    def __repr__(self):
        '''PROVIDED: returns True if all events are the same.'''
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True