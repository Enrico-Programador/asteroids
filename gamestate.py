
class GameState():
    def __init__(self):
        self.points = 0
        self.difficulty_counter = 0

    def pointcounter(self):
        self.points += 1
        self.difficulty_counter += 1
        print(f"Points: {self.points}")
        