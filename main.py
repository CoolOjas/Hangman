
import spacy
nlp = spacy.load("en_core_web_sm")
import random
class Hangman: 
  def __init__(self):
   limbs = 0
   self.limbs = limbs
  def draw(self):
    hangmandrawing = (" |")
    if self.limbs >= 1:
      hangmandrawing += ("\n O")
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
  def dead(self):
    return self.limbs == 6

class Game:
  def __init__(self):
    self.hangman = Hangman()
    wordset = nlp.vocab.strings
    word = random.choice (list(wordset))
    self.word = word.lower()
    lettersguessed = []
    self.lettersguessed = lettersguessed
  
  def showword(self):
    for i in range (0,len(self.word),1):
     if self.word[i] in self.lettersguessed:
       print(self.word[i], end = "")
     else:
       print("_", end = "")
    print("\n")
    
  def getinput(self):
   b = (input("guess a singular letter "))
   self.lettersguessed.append(b)
   if b not in self.word:
      self.hangman.limbs += 1
  def singularloop(self):
    self.getinput()
    self.showword()
    self.hangman.draw()
  def completelyguessedword(self):
    for i in range (0,len(self.word),1):
      if self.word[i] not in self.lettersguessed:
        return False
    return True
  def fullgameloop(self):
    self.showword()
    while not self.hangman.dead() and not self.completelyguessedword():
      self.singularloop()
    self.finish()
  def finish(self):
    if self.hangman.dead():
      print(f"you lost {self.word}")
    else: 
      print ('nice you won')
game1 = Game()
game1.fullgameloop()

