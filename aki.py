# Importing the necessary functions from modules.
from akinator import Akinator, CantGoBackAnyFurther

# Getting the values from the user.
questions = int(input("Enter the maximum number of questions: "))

# Initializing akinator.
aki = Akinator()
start = aki.start_game()

# Asking the user questions until the limit is reached.
while aki.progression < questions + 1:

    answer = input(f"{start}: ")

    if answer == "b":

        try:

            start = aki.back()

        except CantGoBackAnyFurther:

            pass

    else:

        start = aki.answer(answer)

aki.win()

# Asking the user if the guess is correct.
correct = input(f"It's {aki.first_guess['name']}!\n\n{aki.first_guess['description']} ({aki.first_guess['absolute_picture_path']})\nIs this correct? ").lower()

# Determining who won.
if correct in ["yes", "y"]:

    print("Akinator won!")

else:

    print("You won!")