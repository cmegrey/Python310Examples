#Functions
def store_result(storage_object, object_element, result):
    storage_object[object_element].append(result)

def collect_and_store_user_info(question_object, question_element, answer_object, answer_element):
    for element in question_object[question_element]:
        user_response = input(f"What is your {element}? ") #Add data validation for blank response
        print(f"Your {element} is {user_response}")
        store_result(answer_object, answer_element, user_response)

def collect_and_store_user_sessions(question_object, question_element, answer_object, answer_element):
    print("Please indicate which of the following sessions you wish to attend. Respond with either Y or N\n")

    for element in question_object[question_element]:
        user_response = input(f"{element}? ")
        if user_response.upper() == "Y":
            print(f"Ok, I've recorded your interest to attend {element}.")
            store_result(answer_object, answer_element, True)
        else:
            print(f"Ok, I've recorded your disinterest to attend {element}.")
            store_result(answer_object, answer_element, False)

#Main code block
if __name__ == "__main__":
    questions = (["name", "conference ID", "organization", "email address", "food preference"],["Python for beginners", "Database development with Python", "Python for data science", "Advanced Python for application developers"])
    
    answers = ([],[])

    collect_and_store_user_info(questions, 0, answers, 0)

    collect_and_store_user_sessions(questions, 1, answers, 1)

    #For deugging, print out the answers tuple
    print(answers)