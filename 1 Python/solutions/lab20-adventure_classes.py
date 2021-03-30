

# parent class which contains a location, character, and health
class Creature:

    def __init__(self, location_i, location_j, character, health):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character
        self.health = health

# player class (which inherits from creature)
# which defaults to having a smiley face as the character and 10 for the health
class Player(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☺', 10) # invoking the parent class's initializer

# enemy class (which inherits from creature)
# which defaults to having a squiggley as the character and 4 for the health
class Enemy(Creature):

    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '§', 4) # invoking the parent class's initializer
    

# board class which represents the board
class Board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.grid = [] # list of lists of strings
        self.creatures = []

        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(' ')
            self.grid.append(row)
    
    def add_creature(self, creature):
        self.creatures.append(creature)

    def print_board(self):
        print('  j ', end='')
        for j in range(self.width):
            print(j, end=' ')
        print()
        print('i  ' + '-'*self.width*2)
        # loop over the rows
        for i in range(self.height):
            print(str(i) + ' |', end=' ')
            # loop over the columns
            for j in range(self.width):
                # find out if there's a creature at the given location
                # if there is, print out its character
                # if there isn't, print out a space
                for creature in self.creatures:
                    if i == creature.location_i and j == creature.location_j:
                        print(creature.character, end=' ')
                        break
                else:
                    print(self.grid[i][j], end=' ')  # otherwise print the board square
            print('|')
        print('   ' + '-'*self.width*2)




board = Board(10, 10)

player = Player(2, 2)
board.add_creature(player)

enemy1 = Enemy(5, 6)
board.add_creature(enemy1)

enemy2 = Enemy(1, 3)
board.add_creature(enemy2)

enemy3 = Enemy(0, 0)
board.add_creature(enemy3)

enemies = [enemy1, enemy2, enemy3]








# REPL
while True:
    board.print_board()

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player.location_j -= 1  # move left
    elif command == 'right':
        player.location_j += 1  # move right
    elif command == 'up':
        player.location_i -= 1  # move up
    elif command == 'down':
        player.location_i += 1  # move down
    
    # does the player overlap with any enemy?
    for enemy in enemies:
        if player.location_i == enemy.location_i and player.location_j == enemy.location_j:
            print('You encountered an enemy!')
    
    




