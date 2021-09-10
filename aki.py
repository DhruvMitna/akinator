from akinator import Akinator, CantGoBackAnyFurther

questions = int(input("Enter the maximum number of questions: "))

aki = Akinator()
start = aki.start_game()

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

correct = input(f"It's {aki.first_guess['name']}!\n\n{aki.first_guess['description']} ({aki.first_guess['absolute_picture_path']})\nIs this correct? ").lower()

if correct in ["yes", "y"]:

    print("Akinator won!")

else:

    print("You won!")