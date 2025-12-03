from puppy_state import PuppyState
import state_eat

class StateAsleep(PuppyState):
    ''' Puppy in Asleep state'''
    def feed(self, puppy):
        ''' puppy's reaction to feeding when sleeping. Returns a string describing
            the puppy's reaction.
        '''
        puppy.change_state(state_eat.StateEating())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        ''' puppy's reaction to playing when sleeping. Returns a string describing
            the puppy's reaction.
        '''
        return "The puppy is asleep. It doesn't want to play right now."