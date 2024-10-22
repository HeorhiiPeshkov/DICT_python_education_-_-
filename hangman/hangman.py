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
import random
programming_languages = ["python", "java", "pascal", 'golang', 'assembler']
hid_prog_lang = [lang[:3] + "-" * (len(programming_languages) - 3) for lang in programming_languages]
ran_index = random.randrange(len(programming_languages))
ran_prog_lang = programming_languages[ran_index]
ran_hid_prog_lang = hid_prog_lang[ran_index]
writ_ran_prog_lang = input(f"Guess the word {ran_hid_prog_lang}:> ")
if writ_ran_prog_lang == ran_prog_lang:
    print('You survived!')
else:
    print('You lost!')