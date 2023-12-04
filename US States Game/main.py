import csv
import pandas
import turtle
from turtle import Turtle, Screen

image = "blank_states_img.gif"

# Screen setup
screen = Screen()
screen.title("US States Game")
# Add shape to the screen then to turtle
screen.addshape(image)
turtle.shape(image)

# Get user input
answer = screen.textinput(title="Enter your answer", prompt="Name a state: ").title()

# Add each state and its coordinates(as a list) to a dict
states_dict = {}
with open("50_states.csv") as states:
    state_list = csv.reader(states)
    for state in state_list:
        if state[0] == "state":
            continue
        states_dict[state[0]] = [int(state[1]), int(state[2])]


# Function to write the correct guess onto the map
def write_state(state_, x_cor, y_cor):
    # Initialize turtle
    gbenga = Turtle()
    gbenga.hideturtle()
    gbenga.penup()
    gbenga.goto(x_cor, y_cor)
    gbenga.write(f"{state_}", move=False, align="center", font=("Arial", 8, "italic"))


# Set up score, correct guesses and continuously ask for guesses
score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    if answer == "Exit":
        break
    # Check if answer is in our dict AND hasn't been guessed yet
    elif answer in states_dict and answer not in correct_guesses:
        score += 1
        xcor = states_dict[answer][0]
        ycor = states_dict[answer][1]
        write_state(answer, xcor, ycor)
        correct_guesses.append(answer)

    answer = screen.textinput(title=f"{score}/50 states correct", prompt="Enter another state: ").title()

# add states not guessed to a csv file
to_be_learned = {"States To be learned": [state for state in states_dict if state not in correct_guesses]}
to_be_learned_df = pandas.DataFrame(to_be_learned)
to_be_learned_df.to_csv("states_to_be_learned")
