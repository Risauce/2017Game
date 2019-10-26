#-----------------------------------------------#
# Riley Roberts & Anna Jinneman                 #
# Joy and Beauty of Data, Final Assignment      #
# Last Updated: May 30th, 2017                  #
#-----------------------------------------------#
# This program will generate cards for the user #
# to read. They will present a problem that the #
# user will be able to choose options for. The  #
# game will run until the user gets 25 points   #
# or will end if the user gets 0 points.        #
#-----------------------------------------------#

import numpy as np
import pandas as pd
import random
import turtle

#------------------------------------------------------------------------------
class Quest:             #THE QUEST CLASS TO RULE THEM ALL
    def __init__(self):  #Instanciate the variables
        self.title = 0
        self.story = 0
        self.option1 = 0
        self.option2 = 0
        self.option3 = 0
        self.points1 = 0
        self.points2 = 0
        self.points3 = 0
        self.art = 0
        self.seq = 0
        self.seqStory = 0
        self.doneList = []

    def showOptions(self, quest, text, option1, option2, option3): #Shows the options/menu
    
        print(str(self.title),"\n", str(self.story))
        print()
        print("1. ", str(self.option1))
        print("2. ", str(self.option2))
        print("3. ", str(self.option3))
        print()

    def selectQuest(self, collection):   #Set the variables to a random quest title in the CSV
        done = False
        while done == False:
            randomSelection = random.randrange(0, len(collection))
            self.title = collection.ix[randomSelection, 0]
#We want to make sure that cards aren't repeated. So we check if they have been, if so look for another card:
            if self.title not in self.doneList: 
                self.story = collection.ix[randomSelection, 1]
                self.option1 = collection.ix[randomSelection, 2]
                self.option2 = collection.ix[randomSelection, 3]
                self.option3 = collection.ix[randomSelection, 4]
                self.points1 = collection.ix[randomSelection, 5]
                self.points2 = collection.ix[randomSelection, 6]
                self.points3 = collection.ix[randomSelection, 7]
                self.art = collection.ix[randomSelection, 8]
                self.seq = collection.ix[randomSelection, 9]
                self.seqStory = collection.ix[randomSelection, 10]

                done = True

        self.doneList.append(self.title)
        self.showOptions(self.title, self.story, self.option1, self.option2, self.option3)
#----------------------------------------------------------------------------------------------
####TURTLE GRAPHICS STUFF BELOW######
card = turtle.Turtle()
wn = turtle.Screen()
wn.setup(1000, 1000)
wn.bgpic("annarileybgpic.gif")
wn.title("Space Adventure Game")

elli = turtle.Turtle()
elli.hideturtle()

silver = "#E5E4E2"

def cardFill(color):    #Creates inner rectangle and colors it
    wn.delay(0)
    card.penup()
    card.goto(-187.5,237.5)
    card.pendown()
    card.fillcolor(color)
    card.begin_fill()
    for Loop in range(2):
        card.color(color)
        card.speed(0)
        card.forward(375)
        card.right(90)
        card.forward(475)
        card.right(90)
    card.end_fill()
    card.penup()
    card.pensize(4)

def button(color, x, y, distance): #Makes the little buttons.
    wn.delay(0)
    card.penup()
    card.goto(x,y)
    card.pendown()
    card.fillcolor(color)
    card.begin_fill()
    for Loop in range(2):
        card.color(color)
        card.speed(0)
        card.forward(distance)
        card.right(90)
        card.forward(60)
        card.right(90)
    card.end_fill()
    
def backCard(): #Creates the basic card shape
    wn.delay(0)
    card.penup()    
    card.goto(-200,250)
    card.pendown()
    card.fillcolor("#848482")
    card.begin_fill()
    for Loop in range(2):
        card.color("#848482")
        card.speed(0)
        card.forward(400)
        card.right(90)
        card.forward(500)
        card.right(90)
    card.end_fill()
    card.penup()
    card.pensize(4)

def spaceShip():         #Draws the Spaceship art!
    global shipColor
    wn.delay(0)
    card.goto(-20,130)
    card.begin_fill()
    for Loop in range(2):
        card.color(shipColor)
        card.speed(0)
        card.forward(50)
        card.right(90)
        card.forward(87.5)
        card.right(90)
    card.end_fill()
    card.backward(5)
    card.fillcolor("black")
    card.begin_fill()
    card.color("black")
    card.left(60)
    card.forward(60)
    card.right(120)
    card.forward(60)
    card.right(120)
    card.forward(60)
    card.end_fill()
    card.penup()
    card.backward(5)
    card.left(90)
    card.forward(87.5)
    card.pendown()
    card.begin_fill()
    card.right(20)
    card.forward(37.5)
    card.right(160)
    card.forward(35)
    card.right(90)
    card.forward(13)
    card.end_fill()
    card.penup()
    card.forward(50)
    card.pendown()
    card.begin_fill()
    card.right(70)
    card.forward(37.5)
    card.left(161)
    card.forward(35)
    card.left(91.2)
    card.forward(13)
    card.end_fill()
    card.penup()
    card.right(90)
    card.forward(72.5)
    card.left(90)
    card.forward(23)
    card.begin_fill()
    card.circle(15)
    card.end_fill()
    card.seth(0)
    card.hideturtle()

def alien(x, y):        #Draws the Alien Art!
    wn.delay(0)
    color = (random.random(), random.random(), random.random())
    card.goto(x, y)
    card.fillcolor(color)
    card.color(color)
    card.begin_fill()
    card.circle(40)
    card.end_fill()
    card.right(90)
    card.forward(40)
    card.right(150)
    card.begin_fill()
    card.forward(65)
    card.right(120)
    card.forward(64)
    card.right(120)
    card.forward(65)
    card.end_fill()
    card.right(180)
    card.left(30)
    card.forward(75)
    card.left(90)
    card.forward(15)
    card.fillcolor("black")
    card.begin_fill()
    card.color("black")
    card.circle(12)
    card.end_fill()
    card.left(90)
    card.forward(24)
    card.left(90)
    card.penup()
    card.forward(30)
    card.pendown()
    card.begin_fill()
    card.circle(12)
    card.end_fill()
    card.hideturtle()
    
def witch(): #Draws the Witch!
    alien(0, 25)
    card.penup()
    card.goto(0,85)
    card.begin_fill()
    card.pendown()
    card.forward(50)
    card.left(90)
    card.forward(5)
    card.left(90)
    card.forward(100)
    card.left(90)
    card.forward(5)
    card.left(90)
    card.forward(50)
    card.end_fill()
    card.begin_fill()
    card.left(90)
    card.forward(90)
    card.left(180)
    card.right(20)
    card.forward(95)
    card.setheading(0)
    card.forward(32.5)
    card.left(90)
    card.forward(90)
    card.left(180)
    card.left(20)
    card.forward(95)
    card.setheading(180)
    card.forward(70)
    card.end_fill()
    card.setheading(0)
    

def planet():          #Draws the Planet art!
    wn.delay(0)
    card.goto(0,20)
    color2 = (random.random(), random.random(), random.random())
    color1 = (random.random(), random.random(), random.random())
    card.fillcolor(color1)
    card.color(color1)
    card.begin_fill()
    card.circle(70)
    card.end_fill()
    card.left(90)
    card.forward(40)
    card.color(color2)
    card.fillcolor(color2)
    card.begin_fill()
    card.right(90)
    card.forward(30)
    card.right(90)
    card.forward(20)
    card.left(90)
    card.forward(10)
    card.left(90)
    card.forward(20)
    card.right(90)
    card.forward(10)
    card.left(90)
    card.forward(30)
    card.left(90)
    card.forward(15)
    card.right(90)
    card.forward(20)
    card.left(90)
    card.forward(25)
    card.left(90)
    card.forward(15)
    card.right(90)
    card.forward(30)
    card.left(90)
    card.forward(25)
    card.left(90)
    card.forward(20)
    card.right(90)
    card.forward(10)
    card.end_fill()
    card.penup()
    card.backward(40)
    card.right(90)
    card.forward(40)
    card.pendown()
    card.begin_fill()
    for i in range(4):
        card.forward(15)
        card.right(90)
    card.end_fill()
    card.seth(0)
    card.hideturtle()
    
def ellipse(h, l, color, x, y): #Used to draw the ufo
    wn.delay(0)
    elli.penup()
    elli.goto(x, y)
    elli.color(color)
    elli.fillcolor(color)
    elli.begin_fill()
    elli.shape("circle")
    elli.shapesize(h ,l ,1)
    elli.end_fill()
    elli.stamp()
    elli.hideturtle()

def ufoShip(): #Draws the ufo
    wn.delay(0)
    color1 = (random.random(), random.random(), random.random())
    ellipse(4, 12, color1, 0, 100)
    ellipse(3, 5, "black", 0, 125)

def coin(): #Draws the coin card
    card.penup()
    card.pensize(1)
    card.color("#D4A017")
    card.goto(0,20)
    card.pendown()
    card.fillcolor("gold")
    card.begin_fill()
    card.circle(70)
    card.end_fill()
    card.penup()
    card.left(90)
    card.forward(10)
    card.right(90)
    card.color("#D4A017")
    card.pendown()
    card.circle(60)
    card.penup()
    card.goto(0,35)
    card.write("$", True, align="center", font=('Times', 70, "normal"))
    card.hideturtle()


def losingCard():         #Draws the losing card
    wn.delay(0)
    backCard()
    cardFill(silver)
    card.penup()
    card.goto(0,-45)
    card.color("black")
    card.write("You Lose", True, align="center", font=('Times', 60, "bold"))
    card.penup()
    card.hideturtle()
    
def winCard():   #Draws the you win card
    wn.delay(0)
    backCard()
    cardFill(silver)
    card.penup()
    card.goto(0,-45)
    card.color("#D4A017")
    card.write("You Win", True, align="center", font=('Times', 60, "bold"))
    card.penup()
    card.hideturtle()

def quitCard():   #Draws the you win card
    wn.delay(0)
    backCard()
    cardFill(silver)
    card.penup()
    card.goto(0,-45)
    card.color("black")
    card.write("Goodbye!", True, align="center", font=('Times', 60, "bold"))
    card.penup()
    card.goto(0,-160)
    card.write("Thanks for playing.", True, align="center", font=('Times', 18, "normal"))
    card.hideturtle()

#This function is the only intense math in the program. It is used to place and move words in the story text
#to fit the shape of the card. It finds a SPACE that is nearing the end of the allowed width.
def loopForText(text, k): # 30 for Text, 6 for op2, 5 for op3
    newString = ""
    for i in range(len(text)):
        newString += text[i]
        if text[i]==" " and (text.find(" ", i+1)-i)+i%k>=k:                #i%35
            newString += "\n" 
    
    return newString

def resultCard(seqStory): #This card is responsible for showing the result text after a certain choice is selected
    wn.delay(0)
    cardFill(silver)
    card.penup()
    card.goto(0,-45)
    card.color("black")

    seqStory = loopForText(seqStory, 30)
    card.write(seqStory, True, align="center", font=('Times', 18, "bold"))
    card.penup()

    wn.delay(5700)
    card.hideturtle()
    

def cardInfo(title, text, option1, option2, option3, points):    #Will write the name, info and options on the card
    wn.delay(0)
    card.penup()
    card.goto(0,180)
    card.color("black")
    card.write(title, True, align="center", font=('Times', 24, "bold"))
    card.penup()
    
    card.goto(0,-160)
    text = loopForText(text, 30)
    card.write(text, True, align="center", font=('Times', 18, "normal"))
    
    card.penup()
    card.goto(-125,-218)
    card.write(option1, True, align="center", font=('Times', 12, "normal"))
    card.penup()
    
    card.goto(0,-218)
    option2 = loopForText(option2, 6)
    card.write(option2, True, align="center", font=('Times', 12, "normal"))
    card.penup()
    
    card.goto(125,-218)
    option3 = loopForText(option3, 5)
    card.write(option3, True, align="center", font=('Times', 12, "normal"))
    card.goto(0, 210)
    
    card.write("Points: " + str(points) + " / 25", True, align="center", font=('Times', 14, "normal"))
    card.hideturtle()
    
def createCard(quest, points):  #Creates the card. Determines whether to use alien etc by CSV
    #wn.tracer(0,0)
    wn.delay(0)
    backCard()
    cardFill(silver)
    button("#52D017",-175,-170,100) #Height = 60
    button("#1589FF",-50,-170,100)
    button("red",75,-170,100)
    cardInfo(quest.title, quest.story, "Ignore", quest.option2, quest.option3, points)
##Determines what art to show from the CSV file
    if quest.art == 1:
        spaceShip()
    elif quest.art == 2:
        alien(0, 90)
    elif quest.art == 3:
        planet()
    elif quest.art == 4:
        ufoShip()
    elif quest.art == 5:
        witch()
    else:
        coin()
    wn.update()




def shipColorF(): #Making the ship color within color bounds was fairly complicated. This makes it so the user can error without crashing the program.
    global shipColor
    it = False
    while it == False:
        try:
            card.penup()
            backCard()
            cardFill(silver)
            card.goto(0,0)
            card.color("red")
            card.write("Enter ship color", True, align="center", font=('Times', 20, "bold"))
            card.hideturtle()
            shipColor = str(input("What color do you want your ship to be? "))
            card.fillcolor(shipColor)
            it = True
        except:
            print("That is an invalid entry, please try again. ")
            

def playAgain(): #Prompts the user to restart game if they want
    card.goto(0,-160)
    wn.delay(0)
    card.write("(Press R to play Again)", True, align="center", font=('Times', 18, "normal"))
    answer = str(input(("Do you want to play again? ")))
    if answer == "R" or answer == 'r' or answer == 'yes' or answer == 'y':
        main()
    else:
        quitCard()
        print("Goodbye!")
        
            
#--------------------------------------------------------------------------
#The main function. This takes in all the above code and calls it in a orderly manner.
#The section before the while loop creates all the variables needed, as well as the starting points
#theQuest is an instance of the Quest class, which takes in all the information from the CSV
#The while loop IS the game, changing the cards and reading the choices.
#There are several ways the game ends, if you hit 0 points, 25 points, or run out of cards. (also pushing 4)
    
def main():
    global shipColor
    print("Space Adventure Game!")
    print("-------------------------")
    cardCollection = pd.read_csv("allCards.csv")
    
    theQuest = Quest()

    choice = 0
    points = 15
    shipColorF()
    done = False
 
    while choice != 4 and done == False:
        
        theQuest.selectQuest(cardCollection)  #To start a "round" use Quest to select a piece of data out of the CSV
        createCard(theQuest, points)  #Create the Art of the Card
        
        try: #A try and except block is the easiest way to allow for user error.
            choice = int(input("Enter choice: "))
        except:
            print("Please try again.")
        
        if choice == 1:
            print("Points gained/lost: " + str(theQuest.points1))
            points += theQuest.points1
            if choice == theQuest.seq:
                resultCard(theQuest.seqStory)
                print(str(theQuest.seqStory))
            print("Point Total: " + str(points))
            
        elif choice == 2:
            print("Points gained/lost: " + str(theQuest.points2))
            points += theQuest.points2
            if choice == theQuest.seq:
                resultCard(theQuest.seqStory)
                print(str(theQuest.seqStory))
            print("Point Total: " + str(points))
            
        elif choice == 3:
            print("Points gained/lost: " + str(theQuest.points3))
            points += theQuest.points3
            if choice == theQuest.seq:
                resultCard(theQuest.seqStory)
                print(str(theQuest.seqStory))
            print("Point Total: " + str(points))

        elif choice == 4: #Quick QUIT
            losingCard()
            card.goto(0,-160)
            card.write("(You Quit)", True, align="center", font=('Times', 18, "normal"))
            print("Goodbye!")
        else:
            print("Invalid choice.  Please try again.")

        if points >= 25: #Winning condition
            winCard()
            print("You Win!")
            playAgain()
            done = True
            
        if points <= 0: #Losing condition
            losingCard()
            print("You lose!")
            playAgain()
            done = True

        if len(theQuest.doneList) == len(cardCollection): #Run out of cards condition
            losingCard()
            print("You lose because you ran out of cards!")
            playAgain()
            done = True


main()
