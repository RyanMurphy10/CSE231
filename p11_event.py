from datetime import datetime
from datetime import timedelta

CAL_TYPE = ['meeting','event','appointment','other']

class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        '''All parameters are strings except duration (int) and self.
Initialize the public attributes: date, time, duration, cal_type, valid If a time is not well formed, assign None. If a date is not well formed, assign None. If duration is not a positive integer, assign None. If cal_type is not in CAL_TYPE, assign None. If any attributeabove is None, valid is False, otherwise it is True. Look at item 1 in the Data specifications for a valid data format.'''
        try:
          format_time = "%H:%M"
          self.valid = bool(datetime.strptime(time,format_time))
          self.time = time
        except ValueError:
          self.valid = False
          self.time = None
        if date is None:
          self.date = None
          self.valid = False
        else:
          if len(date.split('/')) != 3:
            self.valid = False
            self.date = None
          else:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if month in range(13) and day in range(32) and year in range(10000):
              self.date = date
            else:
              self.date = None
              self.valid = False
        if cal_type not in CAL_TYPE:
          self.cal_type = None
          self.valid = False
        else:
          self.cal_type = cal_type
        if not isinstance(duration, int) or duration < 0:
          self.duration = None
          self.valid = False
        else:
          self.duration  = duration
      
    def get_date(self):
        '''Return the date'''
        return self.date
      
    def get_time(self):
        '''Return the time '''
        return self.time    
      
    def get_time_range(self):
        '''Calculate the end time and return a tuple: (start_time, end_time). We assume that duration is in minutes, e.g, 60, 75, 120 minutes. Also, the start_time and end_time are both in minutes.'''
        format_time = "%H:%M"
        time = datetime.strptime(self.time, format_time)
        start = time.hour * 60 + time.minute
        final = start + self.duration

        return (start, final)

    def __str__(self):
        '''Return a string formatted as: 01/01/0101: start: 9:00; duration: 60 That is, a space after each semicolon and colon, except within the time. If any of the used attributes are None return the string ‘None’'''
        s = ""
        if self.date is None:
          s += "None"
        else:
          s += self.date
        s += ": start: "
        if self.time is None:
          s += "None"
        else:
          s += self.time
        s += "; duration: "
        if self.duration is None:
          s += "None"
        else:
          s += str(self.duration)
        return s
    
    def __repr__(self):
        '''PROVIDED'''
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        '''Return True if self’s time is less than e’s time; False otherwise. If either time is None, return False. Hint: convert time to an integer number of minutes, then compare and return the result. This function is necessary for sorting. We will assume that e is of type Event.'''
        if self.time is None or e.time is None:
          return False
        format_time = "%H:%M"
        time = datetime.strptime(self.time, format_time)
        total_time = time.hour * 60 + time.minute
        etime = datetime.strptime(e.time, format_time)
        total_etime = etime.hour * 60 + etime.minute
        if total_time < total_etime:
          return True
        return False
    
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and self.duration == e.duration and self.cal_type == e.cal_type # and self.status == e.status