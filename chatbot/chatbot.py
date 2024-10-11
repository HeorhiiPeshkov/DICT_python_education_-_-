print("Hello! My name is Practice3_Chat_Bot.\nI was created in 2024")
your_name = input("Please, remind me your name.\n>")
print(f"What a great name you have, {your_name}!")
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
reminder3 = int(input(">"))
reminder5 = int(input(">"))
reminder7 = int(input(">"))
your_age = (reminder3*70 + reminder5*21 + reminder7*15)%105
print(f"Your age is {your_age}; that's a good time to start programming!")
number = int(input("Now I will prove to you that I can count to any number you want.\n>"))
i = 0
while i <= number:
    print(f"{i}!")
    i = i+1
print("Who performs main character in Titanic?")
question = int(input("1. Robert De Niro.\n2. Leonardo Dicaprio.\n3. Johny Depp.\n4. Tom Hardy.\n>"))
while question != 2:
    print("Please, try again!")
    question = int(input(">"))
print("Completed!")
print("Congratulations, have a nice day!")