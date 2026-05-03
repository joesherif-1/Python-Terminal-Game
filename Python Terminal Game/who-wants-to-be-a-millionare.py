import random

questions = {
    "Which of these is a knitted garment? ": "Sweater", 
    "What do Bees gather in order to make Honey?": "Nectar", 
    "Which Disney character famously leaves a glass slipper behind at a royal ball": "Cinderella", 
    "According to a common phrase, a person who takes chances is going out on a what?": "Limb",
    "Which color would you get if you mix blue and yellow?": "Green",
    "Which North American animal has a distinctive black mask and striped tail?": "Raccoon",
    "In The Harry Potter stories, what kind of creature is Firenze?": "Centaur",
    "In the Medical Field, what does the 'C' in 'CPR' stand for?": "Cardiopulmanory",
    "Which author wrote the 'Harry Potter' book series?": "J.K Rowling",
    "What is the capital city of France?": "Paris",
    "Which of these chemical elements has the symbol of 'Au'?": "Gold",
    "In Which year did the Titanic sink?": "1912",
    "Who is the Greek god of the sea?": "Poseidon",
    "What is the name of the longest river in the world?": "Nile",
    "Which artist painted the Mona Lisa?": "Leonardo da Vinci",
    "How many hearts does an octopus have?": "Three",
    "Which US President is featured on the 50$ bill?": "Ulysses S. Grant",
    "Which of these African countries was formerly known as Abyssinia": "Ethiopia",
    "The Earth's atmopshere is composed of approximately 78% of which gas?": "Nitrogen",
    "In The Great Gatsby, what is Jay Gatsby's real name?": "James Gatz"
}

choices = [
    ["A: Skirt", "B: T-shirt", "C: Sweater", "D: Belt"],
    ["A: Water", "B: Nectar", "C: Leaves", "D: Leaves"],
    ["A: Pochahontas", "B: Sleeping Beauty", "C: Elsa", "D: Cinderella"],
    ["A: Bridge", "B: Limb", "C: Boat", "D: Roof"],
    ["A: Green", "B: Orange", "C: Yellow", "D: Purple"],
    ["A: Grizzly Bear", "B: Raccoon", "C: Bald Eagle", "D: Coyote"],
    ["A: Centaur", "B: Elf", "C: Goblin", "D: Dragon"],
    ["A: Cardiac", "B: Cardio", "C: Cardiopulmonary", "D: Circulation"],
    ["A: J.R.R Tolkein", "B: Roald Dahl", "C: J.K Rowling", "D: C.S Lewis"],
    ["A: Rome", "B: Monaco", "C: Madrid", "D: Paris"],
    ["A: Gold", "B: Iron", "C: Magnesium", "D: Argon"],
    ["A: 1908", "B: 1922", "C: 1918", "D: 1912"],
    ["A: Zeus", "B: Apollo", "C: Poseidon", "D: Hermes"],
    ["A: Amazon", "B: Nile", "C: Yangtze", "D: Mississippi"],
    ["A: Vincent van Gogh", "B: Pablo Picasso", "C: Leonardo da Vinci", "D: Claude Monet"],
    ["A: One", "B: Two", "C: Three", "D: Four"],
    ["A: Andrew Jackson", "B: Alexander Hamilton", "C: Benjamin Franklin", "D: Ulysses S. Grant"],
    ["A: Ethiopia", "B: Ghana", "C: Kenya", "D: Nigeria"],
    ["A: Nitrogen", "B: Oxygen", "C: Carbon Dioxide", "D: Argon"],
    ["A: James Gatz", "B: Jordan Baker", "C: George Wilson", "D: Meyer Wolfsheim"]
]

life_lines = ["phone a friend", "50/50", "ask the audience"]

def startGame():
    life50 = False
    question_index = random.randint(1,15)
    counter = 0
    prize = 0
    while counter <= 15:
        if counter == 5:
             print("Good Job, you have reached milestone 1, no matter what from now on you get 1,000$. Your current prize money is {prize}".format(prize=prize))
        elif counter == 10:
             print("Amazing effort! you now are at milestone 2, no matter what from now on you walk away with 32,000$. Your current prize money is {prize}".format(prize=prize))
        print(list(questions.keys())[question_index])
        if life50 == True:
            print(choices[question_index][0], "B: " + list(questions.values())[question_index])
            life50 = False
        else:
            print(choices[question_index])
        answer = input("Your answer:")
        if answer in life_lines:
             life_lines.remove(answer)
             for life_line in life_lines:
                  if answer.lower() == "phone a friend":
                       print("Your friend said the answer was " + list(questions.values())[question_index])
                  elif answer == "50/50":
                        life50 = True
                  elif answer.lower() == "ask the audience":
                       print("The Audience voted for " + list(questions.values())[question_index] + "  being the answer")
        elif answer.lower() == "check":
             print(life_lines, "Your current prize pool is {prize}$".format(prize=prize))
        elif answer.lower() == list(questions.values())[question_index].lower():
             counter += 1
             if prize <= 0:
                  prize += 100
             else:
                  prize = prize*2
             question_index = random.randint(1,15)
        else:
             print("Better luck next time!")
             break
    if counter >= 15:
          print("Congratulations! you won a million dollars!")
        
def introduce():
     print("Welcome to WHO WANTS TO BE A MILLIONARE!")
     name = input("What is your name!?: ")
     print("Let us all welcome {name} to WHO WANTS TO BE A MILLIONARE!".format(name=name))
     print("The Rules of the game are simple. You have 15 questions through out this whole game.")
     print("You start at 100 dollars, and for each question you answer, your prize pool doubles!")
     print("You have 3 life lines, Phone a friend, Ask the Audience, or 50/50")
     print("Whenever you want to use a life line, just type in the life line you would like to use")
     print("You have 2 milestones through out the game, questions 1 through 5, and 10 through 15")
     print("If you get any question wrong in between milestone 1, you walk with nothing. However after reaching milestone 1 you have 1000$ to keep no matter what")
     print("If you reach milestone 2 you have a safety net if 32,000$ incase you get a question wrong from 11-15")
     print("If you do not get any question wrong through out the 15, you get the grand prize of 1,000,000$!")
     print("If at any point you want to check your life lines and prize money, just type 'check' ")
     state = input("Good Luck {name}. Ready when you are, just input start when you want to start. ".format(name=name))
     if state.lower() == "start":
          startGame()

introduce()