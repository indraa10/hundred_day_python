import random as rd


def level_selector():
    level = input("Enter level : 'Hard' or 'Medium' or 'Easy' : \n").lower()
    match level:
        case "hard":
            return 5
        case "medium":
            return 7
        case "easy":
            return 10
        case _:
            return 0


def guess_num():
    selected_num = rd.randint(0, 50)
    retry_attempt = level_selector()

    while retry_attempt > 0:
        guess_number = int(input("guess the number between 0 and 50 . both the mentioned number included: "))
        if guess_number > selected_num:
            print("the guessed number is greater than actual number")
        elif guess_number < selected_num:
            print("the guessed number is less than actual number")
        else:
            print("Bulls EYE!!!")
            break

        retry_attempt -= 1
        print(f"You have {retry_attempt} left")


guess_num()
