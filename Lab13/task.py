class Task:
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date
        self._time = time
    
    @property
    def date(self):
        return self._date
    
    def __str__(self):
        # String representation of task - user facing
        return f"{self._description} - Due: {self.date} at {self._time}"
    
    def __repr__(self):
        # String representation of a task - file facing
        return f"{self._description},{self.date},{self._time}"
    
    def __lt__(self, other):
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
    