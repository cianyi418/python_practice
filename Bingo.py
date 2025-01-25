import random

bing_num = random.randint(1, 100)
times = 1

guess = int(input("Guess a number between 1 and 100: "))
while guess != bing_num:
    if guess > bing_num:
        print("Too high")
        times += 1
    elif guess < bing_num:
        print("Too low")
        times += 1
    guess = int(input("Guess again: "))
else:
    print("Bingo", times, "tries!")

#suggested solution from the copilot
'''
import random

def play_bingo():
    bing_num = random.randint(1, 100)
    times = 1

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess > bing_num:
            print("Too high")
        elif guess < bing_num:
            print("Too low")
        else:
            print(f"Bingo! You guessed it in {times} tries!")
            break

        times += 1

if __name__ == "__main__":
    play_bingo() 
'''