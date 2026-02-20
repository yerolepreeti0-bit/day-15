P_spam = 0.11
P_ham = 0.93

P_free_given_spam = 0.91
P_free_given_ham = 0.055
# Total probability of "Free"
P_free = (
    P_free_given_spam * P_spam +
    P_free_given_ham * P_ham
)
# Bayes theorem
P_spam_given_free = (
    P_free_given_spam * P_spam
) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)

# Convert to percentage
print("Probability email is Spam if it contains 'Free':", round(P_spam_given_free * 100, 2), "%")