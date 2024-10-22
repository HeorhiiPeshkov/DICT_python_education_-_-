# #stage 1
# print("HANGMAN.\nThe game will be available soon.")

# # stage 2
# print("HANGMAN")
# word = input("Guess the word:>")
# if word == "python":
#     print("You survived!")
# else:
#     print("You lost!")

#stage 3
import random
programming_languages = ["python", 'java', 'javascript', 'php', 'pascal', 'c#', 'c++']
ran_prog_lang = (random.choice(programming_languages))
writ_ran_prog_lang = input("Guess the word:>")
if writ_ran_prog_lang == ran_prog_lang:
    print('You survived!')
else:
    print('You lost!')

# #stage 4
# import random
# programming_languages = ["python", 'java', 'javascript', 'php', 'pascal', 'c#']
# hid_prog_lang = ["pyt---", 'j---', 'jav-------', '---', 'pas---', '--']
# ran_prog_lang = (random.choice(programming_languages))
# ran_hid_prog_lang = (random.choice(hid_prog_lang))
# writ_ran_prog_lang = input(f"Guess the word {ran_hid_prog_lang}:>")
# if writ_ran_prog_lang == ran_prog_lang:
#     print('You survived!')
# else:
#     print('You lost!')

