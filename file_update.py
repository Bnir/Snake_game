class Fileupdate:
    def __init__(self):
        with open("Snake_highscore.txt", "r") as file:
            self.score = file.read()

    def check_high(self, current_score):
        if current_score > int(self.score):
            with open("Snake_highscore.txt", "w") as file:
                file.write(str(current_score))

