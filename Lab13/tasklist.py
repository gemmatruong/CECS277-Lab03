from task import Task

class TaskList:
    '''A class that manages a list of Task objects'''

    def __init__(self):
        ''' Initialize the TaskList by loading tasks from 'tasklist.txt'.
            Loaded tasks are automatically sorted.
        '''
        self._tasklist = []
        # Read from file to the list
        with open("tasklist.txt", 'r') as infile:
            for line in infile:
                line = line.strip()
                if line:    # make sure the line is not empty
                    para_list = line.split(",")
                    self._tasklist.append(Task(para_list[0], para_list[1], para_list[2]))
        
        # Sort the list
        self._tasklist.sort()
    
    def add_task(self, desc, date, time):
        ''' Construct a new task using the parameters, list, then sort the list'''
        # Add a new task to the list
        self._tasklist.append(Task(desc, date, time))
        # Sort the tasklist
        self._tasklist.sort()
    
    def get_current_task(self):
        ''' Return the task at the beginning of the list '''
        if self._tasklist:
            return self._tasklist[0]
        return None
    
    def mark_complete(self):
        ''' Remove and return the current task from the tasklist'''
        if self._tasklist:
            return self._tasklist.pop(0)
        else:
            return None
    
    def save_file(self):
        ''' Write the contents of the tasklist to the file'''
        with open("tasklist.txt", 'w') as outfile:
            for task in self._tasklist:
                outfile.write(f"{repr(task)}\n")
    
    def __len__(self):
        ''' Return the number of items in the tasklist'''
        return len(self._tasklist)
    
    def __iter__(self):
        ''' Initializes attribute n and returns iterator'''
        self._n = -1
        return self
    
    def __next__(self):
        ''' Return next task in iteration until it reaches the end of the list'''
        self._n += 1
        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            return self._tasklist[self._n]