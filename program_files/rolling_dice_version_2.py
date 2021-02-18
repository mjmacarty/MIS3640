from random import randint
import matplotlib.pyplot as plt

rolls = {k : 0 for k in range(2,13)}
iterations = int(input("How many rolls would you like to simulate? "))

for iteration in range(iterations):
    roll = randint(1,6) + randint(1,6)
    rolls[roll] += 1
# using hexadecimal code for color
plt.bar(list(rolls.keys()), list(rolls.values()), color = '#407294')
plt.show()