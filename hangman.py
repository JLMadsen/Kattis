answer = input()
guesses = input()
attempts = 10
for guess in guesses:
    if len(answer) == 0:
        print("WIN")
        exit()
    if guess in answer:
        answer = answer.replace(guess, "")
    else:
        attempts -= 1
        if attempts == 0:
            print("LOSE")
            exit()