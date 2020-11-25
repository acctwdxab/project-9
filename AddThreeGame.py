# Dan Wu
# 11/23/2020
# Create a game that allows two players to choose number from 1-9, If at any point exactly three of the player's numbers sum to 15, then that player has won.

class AddThreeGame :
    """Represents the game that allows two players to choose numbers and show game status and result"""

    def __init__(self) :
        """Create a player and the first and second choice of numbers"""
        self._pick_1 = 0
        self._pick_2 = 0
        self._played = []
        self._curstat = "UNFINISHED"

    def get_current_state(self):
        """ returns the current status"""
        return self._curstat

    def make_move(self, player, num):
        """ represents the move made by player"""
        if num in self._played:
            return False

        if num > 9 or num < 1:
            return False

        if player == "first":
            self._pick_1 = self._pick_1 + num
            self._played.append ( num )

        elif player == "second" :
            self._pick_2 = self._pick_2 + num
            self._played.append ( num )

        if self._pick_1 == 15 and self._pick_2 == 15 :
            self._curstat = "DRAW"

        elif self._pick_1 == 15 :
            self._curstat = "FIRST_WON"

        elif self._pick_2 == 15 :
            self._curstat = "SECOND_WON"

        if len ( self._played ) == 9 :
            self._curstat = "DRAW"
        return True


game = AddThreeGame ()
while True :
    num = int ( input ( "Player 1 please enter a number: " ) )
    while True :
        if game.make_move ( "first" , num ) == True :
            break
        else :
            num = int ( input ( "Invalid input! Player 1 please re-enter a number: " ) )
    num = int ( input ( "Player 2 please enter a number:" ) )
    while True :
        if game.make_move ( "second" , num ) == True :
            break
        else :
            num = int ( input ( "Invalid input! Player 2 please re-enter a number: " ) )

    playstatus = game.get_current_state ()
    if playstatus == "UNFINISHED" :
        print ( "No one reached 15. Get ready for next round.\n" )
    elif playstatus == "FIRST_WON" :
        print ( "First player won!!!\n" )
        break

    elif playstatus == "SECOND_WON" :
        print ( "Second player won!!!\n" )
        break
    elif playstatus == "DRAW" :
        print ( "Game ends in draw\n" )
        break
