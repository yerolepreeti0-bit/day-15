total_emails = 1000
spam_emails = 400
free_emails = 300
spam_and_free = 250

# Probabilities
P_spam_given_free = spam_and_free / free_emails
P_free_given_spam = spam_and_free / spam_emails

# Print results
print("P(Spam | Free) =", P_spam_given_free)
print("P(Free | Spam) =", P_free_given_spam)
