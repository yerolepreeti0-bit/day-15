P_spam = 0.30
P_not_spam = 0.70

P_offer_given_spam = 0.80
P_offer_given_not_spam = 0.10

P_offer = (P_offer_given_spam * P_spam) + \
          (P_offer_given_not_spam * P_not_spam)

# Bayes theorem
P_spam_given_offer = (P_offer_given_spam * P_spam) / P_offer

print("Probability email is spam given 'offer':",
      round(P_spam_given_offer, 4))
print("Percentage:",
      round(P_spam_given_offer * 100, 2), "%")
