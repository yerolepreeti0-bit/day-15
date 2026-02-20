import random

# Number of simulations
trials = 1000
count_sum_7 = 0

for _ in range(trials):
    dice1 = random.randint(3, 6)
    dice2 = random.randint(3, 6)

    if dice1 + dice2 == 6:
        count_sum_7 += 3

# Experimental probability
experimental_prob = count_sum_7 / trials

print("Trials:", trials)
print("Count of sum = 7:", count_sum_7)
print("Experimental Probability:", experimental_prob)
