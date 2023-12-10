class GridWorld2:
    def __init__(self, size=(2, 2),trap=None,goal=(1,1),start=(0,0)):
        self.size = size
        self.board = [[' ']*size[1] for _ in range(size[0])]
        self.position = start  # Start at the top-left corner
        if trap != None:
            self.board[trap[0]][trap[1]] = '-'  # Trap
        self.trap_position = trap
        self.goal_position = goal
        self.board[goal[0]][goal[1]] = '+'  # Goal

    def display(self):
        board_copy = [row.copy() for row in self.board]
        board_copy[self.position[0]][self.position[1]] = 'P'  # Show player's position
        return board_copy

    def move(self, direction)->bool:
        if direction == 'up' and self.position[0] > 0:
            self.position = (self.position[0]-1, self.position[1])
            return True
        elif direction == 'down' and self.position[0] < self.size[0]-1:
            self.position = (self.position[0]+1, self.position[1])
            return True
        elif direction == 'left' and self.position[1] > 0:
            self.position = (self.position[0], self.position[1]-1)
            return True
        elif direction == 'right' and self.position[1] < self.size[1]-1:
            self.position = (self.position[0], self.position[1]+1)
            return  True
        else:
            return False

    def calculate_reward(self):
        if self.position == self.goal_position:  # Win position
            return 10
        elif self.position == self.trap_position:  # Trap position
            print(self.position)
            return 0
        else:
            return -1
    def play(self):
        '''
        Play the game interactively.
        '''
        while True:
            for i in self.display():
                print(i)
            direction = input("Enter direction (up/down/left/right): ")
            self.move(direction)
            reward = self.calculate_reward()
            print("Reward:", reward)
            if reward == 10 or reward == -10:
                break

if __name__ == '__main__':
    game = GridWorld2()
    game.play()
