"""
To help develop your online research skills, let's try an example.
Your mission today is to find three different ways to print the number 0 thru 10 using Python. Write the code to do this, after having researched online some techniques that make this easy. By the way, printing each number individually does not count!
Be prepared to discuss and demonstrate the code to your classmates
"""


#Using a 'while' loop
count = 0
while count < 11:
    print(count)
    count += 1

#Using a 'for' loop
for count in range(11):
    print(count)

#Using a 'for' loop and a list
numbers_list = list(range(11))
for count in numbers_list:
    print(count)
    count += 1
