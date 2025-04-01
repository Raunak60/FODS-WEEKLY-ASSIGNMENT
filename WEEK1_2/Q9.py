# Number guessing game
import random
answer = random.randint(1, 100)
attempts = 5
for _ in range(attempts):
    guess = int(input("Guess a number (1-100): "))
    if guess == answer:
        print("Correct number!")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game Over. The number was", answer)