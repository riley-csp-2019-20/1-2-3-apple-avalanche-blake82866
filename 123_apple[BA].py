#   a123_apple_1.py
import turtle as trtl
import random
drawer = trtl.Turtle()
# make backround
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")

apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

apple = trtl.Turtle()

# create random letters
rad_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]   
appletters = random.choice(rad_letters)
rad_letters.append(appletters)

# create apple
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  apple.ht()
  apple.penup()
  ycor = random.randint(0, 100)
  xcor = random.randint(-100, 100)
  apple.goto(xcor,ycor)
  apple.showturtle()
  wn.update()

def A():
  drawer.ht()
  drawer.penup()
  gox = apple.xcor()
  goy = apple.ycor() 
  drawer.goto(gox,goy)
  drawer.setheading(270)
  drawer.forward(45)
  drawer.setheading(180)
  drawer.forward(20)
  drawer.color("white")
  drawer.write(appletters, font=("Arial", 50, "bold"))

#create apple
draw_apple(apple)
A()

def life_alert():
  apple.pendown()
  apple.speed(5)
  newx = apple.xcor()
  apple.goto(newx,-150)
  drawer.clear()
  apple.hideturtle()
  apple.clear()
  apple.penup()
  ycor = random.randint(0, 100)
  xcor = random.randint(-100, 100)
  apple.goto(xcor,ycor)
  apple.showturtle()
  A()

# when letters are clicked have them fall
wn.onkey(life_alert, appletters)

wn.listen()
rad_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]   
appletters = random.choice(rad_letters)
rad_letters.append(appletters)
wn.onkey(life_alert, appletters)
wn.listen()

trtl.mainloop()