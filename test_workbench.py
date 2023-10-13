questions = (["name", "conference ID", "organization", "email address", "food preference"],["Python for beginners", "Database development with Python", "Python for data science", "Advanced Python for application developers"])

for element in questions[0]:
    user_response = input(f"What is your {element}? ")
    print(f"Your {element} is {user_response}")

print("Please indicate which of the following sessions you wish to attend. Respond with either Y or N\n")

for element in questions[1]:
    user_response = input(f"{element}? ")
    if user_response.upper() == "Y":
        print(f"Ok, I've recorded your interest to attend {element}.")
    else:
        print(f"Ok, I've recorded your disinterest to attend {element}.")