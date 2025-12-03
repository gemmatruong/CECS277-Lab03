from puppy_state import PuppyState
import state_asleep

class StatePlaying(PuppyState):
    ''' Puppy in Asleep state'''
    def feed(self, puppy):
        ''' puppy's reaction to feeding when playing. Returns a string describing
            the puppy's reaction.
        '''
        return "The puppy is too busy playing with the ball to eat right now."
    
    def play(self, puppy):
        ''' puppy's reaction to playing when playing. Returns a string describing
            the puppy's reaction.
        '''
        puppy.inc_plays()

        if puppy.plays == 3:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it.\n" \
            "The puppy played so much it fell asleep!"
        return "You throw the ball again and the puppy excitedly chases it."