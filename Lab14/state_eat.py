from puppy_state import PuppyState
import state_asleep
import state_play

class StateEating(PuppyState):
    ''' Puppy in Asleep state'''
    def feed(self, puppy):
        ''' puppy's reaction to feeding when eating. Returns a string describing
            the puppy's reaction.
        '''
        puppy.inc_feeds()

        if puppy.feeds == 3:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\n" \
            "The puppy ate so much it fell asleep!"
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    
    def play(self, puppy):
        ''' puppy's reaction to playing when eating. Returns a string describing
            the puppy's reaction.
        '''
        puppy.change_state(state_play.StatePlaying())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."