# #stage 1
# print("HANGMAN.\nThe game will be available soon.")

# # stage 2
# print("HANGMAN")
# word = input("Guess the word:>")
# if word == "python":
#     print("You survived!")
# else:
#     print("You lost!")

# #stage 3
# import random
# programming_languages = ["python", 'java', 'javascript', 'php', 'pascal', 'c#', 'c++']
# ran_prog_lang = (random.choice(programming_languages))
# writ_ran_prog_lang = input("Guess the word:>")
# if writ_ran_prog_lang == ran_prog_lang:
#     print('You survived!')
# else:
#     print('You lost!')

# # #stage 4
# import random
# programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
# hid_prog_lang = [lang[:3] + "-" * (len(programming_languages) - 3) for lang in programming_languages]
# ran_index = random.randrange(len(programming_languages))
# ran_prog_lang = programming_languages[ran_index]
# ran_hid_prog_lang = hid_prog_lang[ran_index]
# writ_ran_prog_lang = input(f"Guess the word {ran_hid_prog_lang}:> ")
# if writ_ran_prog_lang == ran_prog_lang:
#     print('You survived!')
# else:
#     print('You lost!')

# # stage 5
# import random
# programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
# ran_prog_lang = random.choice(programming_languages)
# guessed_letters = []
# attempts = 8
# while attempts > 0:
#     displayed = ""
#     for letter in ran_prog_lang:
#         if letter in guessed_letters:
#             displayed += letter
#         else:
#             displayed += "-"
#     print(displayed)
#     guess = input('Input a letter: >')
#     if guess in guessed_letters:
#         print(r'''That letter doesn't appear in the word''')
#     guessed_letters.append(guess) #список унікальних елементів (додає до списку літер)
#     if guess in ran_prog_lang:
#         all_letters_guessed = True
#         for letter in ran_prog_lang:
#             if letter not in guessed_letters:
#                 all_letters_guessed = False
#                 break
#         if all_letters_guessed:
#             print(r'''Thanks for playing! We'll see how well you did in the next stage''')
#             break
#     else:
#         attempts -= 1
#         print(r'''That letter doesn't appear in the word''')
# if attempts == 0:
#     print(r'''Thanks for playing! We'll see how well you did in the next stage''')

# # stage 6
# import random
# programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
# ran_prog_lang = random.choice(programming_languages)
# guessed_letters = []
# attempts = 8
# while attempts > 0:
#     displayed = ""
#     for letter in ran_prog_lang:
#         if letter in guessed_letters:
#             displayed += letter
#         else:
#             displayed += "-"
#     print(displayed)
#     guess = input('Input a letter: >')
#     if guess in guessed_letters:
#         print("No improvements")
#         attempts -= 1
#         continue
#     if attempts == 0:
#         print(r'''Thanks for playing! We'll see how well you did in the next stage''')
#     guessed_letters.append(guess) #список унікальних елементів (додає до списку літер)
#     if guess in ran_prog_lang:
#         all_letters_guessed = True
#         for letter in ran_prog_lang:
#             if letter not in guessed_letters:
#                 all_letters_guessed = False
#                 break
#         if all_letters_guessed:
#             print(r'''Thanks for playing! We'll see how well you did in the next stage''')
#             break
#     else:
#         attempts -= 1
#         print(r'''That letter doesn't appear in the word''')
# if attempts == 0:
#     print(r'''Thanks for playing! We'll see how well you did in the next stage''')

# # stage 7
# import random
# programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
# ran_prog_lang = random.choice(programming_languages)
# guessed_letters = []
# attempts = 8
# while attempts > 0:
#     displayed = ""
#     for letter in ran_prog_lang:
#         if letter in guessed_letters:
#             displayed += letter
#         else:
#             displayed += "-"
#     print(displayed)
#     guess = input('Input a letter: >')
#     if guess in guessed_letters:
#         print("You've already guessed this letter")
#         continue
#     if not guess.isalpha() or not guess.islower():
#         print("Please enter a lowercase English letter.")
#         continue
#     if len(guess) != 1:
#         print("You should input a single letter.")
#         continue
#     guessed_letters.append(guess) #список унікальних елементів (додає до списку літер)
#     if guess in ran_prog_lang:
#         all_letters_guessed = True
#         for letter in ran_prog_lang:
#             if letter not in guessed_letters:
#                 all_letters_guessed = False
#                 break
#         if all_letters_guessed:
#             print(r'''Thanks for playing! We'll see how well you did in the next stage''')
#             break
#     else:
#          attempts -= 1
#          print(r'''That letter doesn't appear in the word''')
# if attempts == 0:
#     print(r'''Thanks for playing! We'll see how well you did in the next stage''')

# stage 8
main_menu = input('Type "play" to play the game, "exit" to quit:>')
if main_menu == 'exit':
    print('')
elif main_menu != 'play':
    input('Type "play" to play the game, "exit" to quit:>')
elif main_menu == 'play':
    import random
    programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
    ran_prog_lang = random.choice(programming_languages)
    guessed_letters = []
    attempts = 8
    while attempts > 0:
        displayed = ""
        for letter in ran_prog_lang:
            if letter in guessed_letters:
                displayed += letter
            else:
                displayed += "-"
        print(displayed)
        guess = input('Input a letter: >')
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue
        if not guess.isalpha() or not guess.islower():
            print("Please enter a lowercase English letter.")
            continue
        if len(guess) != 1:
            print("You should input a single letter.")
            continue
        guessed_letters.append(guess)  # список унікальних елементів (додає до списку літер)
        if guess in ran_prog_lang:
            all_letters_guessed = True
            for letter in ran_prog_lang:
                if letter not in guessed_letters:
                    all_letters_guessed = False
                    break
            if all_letters_guessed:
                print(r'''Thanks for playing! We'll see how well you did in the next stage''')
                break
        else:
            attempts -= 1
            print(r'''That letter doesn't appear in the word''')
    if attempts == 0:
        print(r'''Thanks for playing! We'll see how well you did in the next stage''')