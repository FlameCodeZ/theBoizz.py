from random import seed
from random import randint
import time
print("Write the following number in quick succession to defuse the bomb, your team depends on you!")
for _ in range(1):
	value = randint(000000000,999999999)
	print(value)

	defuseAttempt = input("Now is the time soldier enter the numbers!!!\n")
	if defuseAttempt == value:
		print("You did it comrade, you've saved us all!")
print(value)
print(defuseAttempt)