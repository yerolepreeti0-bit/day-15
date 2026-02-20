# Given
population = 10000
disease_rate = 0.02
accuracy = 0.95

# Calculate counts
diseased = population * disease_rate          # 2% of 10000
not_diseased = population - diseased

# Test outcomes
true_positive = diseased * 0.95               # P(Positive | Disease)
false_positive = not_diseased * 0.05          # P(Positive | No Disease)

total_positive = true_positive + false_positive

# Bayes probability
P_disease_given_positive = true_positive / total_positive

print("Diseased:", diseased)
print("Not Diseased:", not_diseased)
print("True Positives:", true_positive)
print("False Positives:", false_positive)
print("Total Positives:", total_positive)
print("\nP(Disease | Positive) =", P_disease_given_positive)
print("P(Disease | Positive) = {:.2f}%".format(P_disease_given_positive * 100))
