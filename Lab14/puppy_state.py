import abc

class PuppyState(abc.ABC):
    '''Interface'''
    @abc.abstractmethod
    def feed(self, puppy):
        pass

    @abc.abstractmethod
    def play(self, puppy):
        pass