# Generate a random number
import random
for x in range(1):
  secret_number = random.randint(0,100)

# Input guess from user
guess = -1
n=0

        
while secret_number != guess and n!= 10:
    n=n+1

    guess = input("Guess the secret number in less than 10 tries:")
    print ("Your guess is: ", guess, "This was guess number ", n)
    guess = int(guess)
    
# Check if guess = random number that was generated
    if guess < secret_number and n < 10:
     print ("Your guess is low")
    elif guess > secret_number and n < 10:
        print ("Your guess is high")
    elif n < 10:
        print ("Your guess is Right! Hurray you win!")
    else:
        print ("Sorry, you lose.")



