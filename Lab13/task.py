class Task:
    ''' A class that represents a single task with a description, due date, and due time'''

    def __init__(self, desc, date, time):
        '''assign the parameters to the attributes'''
        self._description = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        '''date: due date of the task. A string in the format: MM/DD/YYYY'''
        return self._date
    
    def __str__(self):
        ''' Returns a string used to display the task information to the user'''
        return f"{self._description} - Due: {self.date} at {self._time}"
    
    def __repr__(self):
        ''' Returns a string used to write the task to the file'''
        return f"{self._description},{self.date},{self._time}"
    
    def __lt__(self, other):
        ''' Returns true if the self task is less than the other task'''
        # Compares by year, then month, then day
        # then hour, then minute,
        # then description
        # MM/DD/YYYY
        # Compare Year

        # Extract date components
        month = int(self._date[0:2])
        day = int(self._date[3:5])
        year = int(self._date[6:10])

        other_month = int(other._date[0:2])
        other_day = int(other._date[3:5])
        other_year = int(other._date[6:10])

        # Extract time components
        hour = int(self._time[0:2])
        minute = int(self._time[3:5])

        other_hour = int(other._time[0:2])
        other_minute = int(other._time[3:5])

        return (year, month, day, hour, minute, self._description) < \
                (other_year, other_month, other_day, other_hour, other_minute, other._description)
    