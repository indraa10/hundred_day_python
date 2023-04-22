## Day9
#### Dictionaries and Nesting
# switch case

select_language = True

while select_language:
    lang = input("enter your fav language: ").lower()

    match lang:
        case "python":
            print("AI/ML")
        case "java":
            print("app development")
        case _:
            print("Not sure")

    next_selection = input("do you want to select again: 'yes' or 'no': ").lower()
    if next_selection == 'yes':
        select_language = True
    elif next_selection == 'no':
        select_language = False
    else:
        continue
