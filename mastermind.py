
# Generate a random 4-digit number
import random


num = random.randrange(1000, 10000)

# Initialize the counter for tries
ctr = 0
max_tries = 5  # Set the maximum number of tries

# Function to check the guess
def check_guess(n, num):
    count = 0
    correct = ['X'] * 4  # Placeholder for correct digits
   
    n_str = str(n)
    num_str = str(num)

    for i in range(4):
        if n_str[i] == num_str[i]:
            count += 1
            correct[i] = n_str[i]

    return count, correct

# Main game loop
while ctr < max_tries:
    try:
        n = int(input("Guess the 4-digit number: "))
       
        if n < 1000 or n > 9999:
            print("Please enter a valid 4-digit number.")
            continue
       
        ctr += 1  # Increment the counter for each guess

        if n == num:
            print("You've become a Mastermind!")
            print("It took you only", ctr, "tries.")
            break

        count, correct = check_guess(n, num)
       
        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
        else:
            print("None of the numbers in your input match.")
       
        print(f"You have {max_tries - ctr} tries left.\n")

    except ValueError:
        print("Invalid input. Please enter a number.")

if ctr == max_tries and n != num:
    print(f"Sorry, you've used all your tries. The correct number was {num}.")
