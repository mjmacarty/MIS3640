import random
from time import time, sleep

total_time = 0
average_time = 0
print("Welcome to thje reaction time tester")
print("When the prompt apprears hit enter!")
sentinel = 1
for run in range(3):

    print("Get ready")
    prompt = random.random() * 5
    sleep(prompt)
    start_time = time()
    print("Quick, hit enter!!")
    input()
    reaction_time = time() - start_time
    total_time += reaction_time
    print(f"Wow, that was fast. It took {reaction_time:.3f}")
    #print(sentinal)
    average_time = total_time / sentinel
    sentinel += 1
    print("-" * 25)
    print(f"Average time was {average_time:.3f}")



