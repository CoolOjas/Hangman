import time
import random
#import stuff lol

with open("Words.txt", "r")as file:
    ro = file.read()
splitro = ro.split("\n")
#made the words 


class Hangman:
    def __init__(self):
        limbs = 0
        self.limbs = limbs
#made the hangman class, made the limbs ez
    def draw(self):
        hangmandrawing = " |"
        if self.limbs >= 1:
            hangmandrawing += "\n O"
        if self.limbs >= 4:
            hangmandrawing += "\n/|\\"
        elif self.limbs >= 3:
            hangmandrawing += "\n/|"
        elif self.limbs >= 2:
            hangmandrawing += "\n |"
        if self.limbs >= 5:
            hangmandrawing += "\n/"
        if self.limbs >= 6:
            hangmandrawing += " \\"
        print(hangmandrawing)
# too much work
    def dead(self):
        return self.limbs == 6
#he dead

class Game:
    def __init__(self):
        self.hangman = Hangman()
        wordset = splitro
        word = random.choice(list(wordset))
        self.word = word.lower()
        lettersguessed = []
        self.lettersguessed = lettersguessed
#omg too much work
    def showword(self):
        for i in range(0, len(self.word), 1):
            if self.word[i] in self.lettersguessed:
                print(self.word[i], end="")
            else:
                print("_", end="")
        print("\n")
#making the word
    def getinput(self):
        b = input("guess a singular letter ")
        if b not in self.word and b not in self.lettersguessed:
            self.hangman.limbs += 1
        self.lettersguessed.append(b)
#getting the input lol
    def singularloop(self):
        self.getinput()
        self.showword()
        time.sleep(0.5)
        self.hangman.draw()
#creating a loop
    def completelyguessedword(self):
        for i in range(0, len(self.word), 1):
            if self.word[i] not in self.lettersguessed:
                return False
        return True
#What would happen if they guessed the word???
    def fullgameloop(self):
        self.intro()
        self.showword()
        while not self.hangman.dead() and not self.completelyguessedword():
            self.singularloop()
        self.finish()
#the full game
    def finish(self):
        if self.hangman.dead():
            print(f"you lost {self.word}")
        else:
            print("nice you won")
        self.calculatescore()
    def intro(self):
        print("hello, welcome to my hangman, in hangman you have to guess the word, keep on guessing letters until you lose or win!!!! This is Ojas Hangman!!!!!!!")
#finished, finally
    def calculatescore(self):
        score = 0
        if self.completelyguessedword():
            score += 10
        correctlyguessedletter = 0
        for i in range(0, len(self.word), 1):
#Caclulating 
            if self.word[i] in self.lettersguessed:
                correctlyguessedletter += 1
        skibidi = correctlyguessedletter
        score += skibidi*100
        print(f" you got {score} points")

        with open("Score.txt", "r") as file:
            highscore = float(file.read())

        looksmaxxing = max(highscore,score)
#literally looksmaxxing

        with open("Score.txt", "w") as file:
            file.write(str(looksmaxxing))

        print(f" your highscore is {looksmaxxing}")

#alost done
rizz = input('how many games do you want to play????????')
for i in range(0,int(rizz),1):
    game37490573495 = Game()
    game37490573495.fullgameloop()

game1 = Game()
#omg took too many lines of code
