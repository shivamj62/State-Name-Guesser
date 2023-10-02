import turtle
import pandas

correct_guesses = []
# shivam
# Window Creation
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading master data csv file
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()

# Function to grab center coords of all states on the map by clicking on state within turtle Screen
# def get_click(x,y):
#    print(x,y)
# turtle.onscreenclick(get_click)
# turtle.mainloop()

# Keeps game running until all guess
while len(correct_guesses) < 50:
    # Text input for guess
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                              prompt="What's another state name?").title()
    # Exit Condition
    if answer == "Exit":
        # Creation of .csv file containing names of unguessed states
        unguessed_states = [state for state in all_states if state not in correct_guesses]
        df = pandas.DataFrame(unguessed_states)
        df.to_csv("states_to_learn.csv")
        break
    
    # Updating map with names of guessed states and keeping track of correct guesses
    elif answer in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data["state"] == answer]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer)

        correct_guesses.append(answer)




