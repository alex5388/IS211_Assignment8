import random
import time



class Die():
    ''' Setup the game equipment '''
    def __init__(self):
        self.die_number = 0

    def roll(self):
        self.die_number = random.randint(1,6)

    def get_die_number(self):
        return self.die_number


class Player():
    ''' Player setup'''
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_score = 0
        self.turn = True


    def addtoFinal(self):
        ''' add turn score to the overall score'''
        self.score = self.score + self.turn_score

    def addtoTurn(self, points):
        ''' keep a running tally of turn score'''
        self.turn_score = self.turn_score + points

    def reset(self):
        ''' reset the turn score'''
        self.turn_score = 0

    def reset_turn(self):
        ''' reset who's turn it is'''
        self.turn = True


    def strategy(self, die):
            ''' main game setup. overall logic of the game '''
            while self.turn:    #run until the player ends their turn
                choose = input("Pick 'r' to roll the die or 'h' to hold.")
                if choose == 'r':
                    die.roll()
                    if die.get_die_number() == 1:
                        print("----{} rolled a {}.".format(self.name, die.get_die_number()))
                        print("You lost your TURN-SCORE points. Your OVERALL SCORE is {}. It's now the next player's turn...".format(self.score))
                        self.turn = False
                        self.reset()
                    elif die.get_die_number() > 1:
                        self.addtoTurn(die.get_die_number())
                        print("----{} rolled a {} and your TURN-SCORE is {}.".format(self.name, die.get_die_number(), self.turn_score))

                elif choose == 'h':
                    self.addtoFinal()
                    print("{} chose to hold, your OVERALL SCORE is currently {}. It's now the next player's turn...".format(self.name, self.score))
                    if self.score >= 100:
                        print("YOU'VE WON!!! game over...")
                        exit()
                    self.reset()
                    self.turn = False
                elif choose == 'I win!!':
                    print("Secret Cheat Code Entered...You win...")
                    exit()

class computer_player(Player):
    def __init__(self, name):
        Player.__init__(self, name)



    def strategy(self, die):
        '''automated computer playing strategy'''
        cpu_turn = 'r'
        while self.turn:  # run until the player ends their turn
            if cpu_turn == 'r':
                die.roll()
                if die.get_die_number() == 1:
                    print("Computer rolled a {}.".format(die.get_die_number()))
                    print(
                        "{} lost its TURN-SCORE points. Computer's OVERALL SCORE is {}. It's now the next player's turn...".format(self.name,
                            self.score))
                    self.turn = False
                    self.reset()
                elif die.get_die_number() > 1:
                    self.addtoTurn(die.get_die_number())
                    print("----{} rolled a {} and its TURN-SCORE is {}.".format(self.name, die.get_die_number(), self.turn_score))
                    if self.turn_score > 25 and self.turn_score < 100 - self.turn_score:
                        cpu_turn = 'h'
                    else:
                        print('Computer rolls again')

            elif cpu_turn == 'h':
                self.addtoFinal()
                print("{} chose to hold, its OVERALL SCORE is currently {}. It's now the next player's turn...".format(self.name, self.score))
                if self.score >= 100:
                    print("YOU'VE WON!!! game over...")
                    exit()
                self.reset()
                self.turn = False





class human_player(Player):
    def __init__(self, name):
        Player.__init__(self, name)




class player_factory:

    def get_player(player_type):
        if player_type == "human":
            return human_player(Player)
        if player_type == "computer":
            return computer_player(Player)

class TimedGameProxy():
    def __init__(self):

        self.start_time = time.time()
        self.end_time = time.time()

    def game_timer(self):
        if self.end_time - self.start_time == 60:
            print("time is up!")
            exit()









def main():
    die = Die()
    player1 = input("Enter player1 type: 'human' or 'computer'... ")
    if player1 == "human":
        player1 = player_factory.get_player("human")
    elif player1 == "computer":
        player1 = player_factory.get_player("computer")

    player2 = input("Enter player2 type: 'human' or 'computer'... ")
    if player2 == "human":
        player2 = player_factory.get_player("human")
    elif player2 == "computer":
        player2 = player_factory.get_player("computer")

    timer = input("Set a 1 min. timer: 'y' or 'n'...")
    if timer == 'y':
        timer = TimedGameProxy()
        timer.game_timer()
    elif timer == 'n':
        pass






    game = True
    while game:
        player2.strategy(die)
        player2.reset_turn()
        player1.strategy(die)
        player1.reset_turn()



if __name__=="__main__":
    main()