#
# WHILE Loop
#

# i = 1
# while i<=10:
#     print(i)
#     i += 1

##
# Guess Secret word game
#

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if not(out_of_guesses):
    print("You Win! ")
else:
    print("You Loose")