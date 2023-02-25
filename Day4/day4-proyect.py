from random import *
secretNumber = randint(1, 100)
#print(f"Random number is: {secretNumber}")

userLife = 8
nAttempts = 0
userName = input("What is your name? ")
print(f"Hello {userName} tell me a number between 1 and 100")
while (userLife >= 0):
	userLife -= 1
	nAttempts += 1
	inputNumber = int(input())
	if inputNumber >= 101 or inputNumber <= 0:
		print("Your number is not in the range")	
	elif inputNumber > secretNumber :
		print(f"Your number is greater than the random number")
	elif inputNumber < secretNumber :
		print(f"Your number is less than the random number")
	else :
		print(f"\nYou win {userName} with {nAttempts} Attempts \n\n")
		finish = input("Do you want to play again? (y/n) ")
		if finish == "y":
			userLife = 8
		else:
			exit()

print(f"You lose the number was {secretNumber}")