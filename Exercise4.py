P_regular = 0.40
P_irregular = 0.60

# Pass rates
P_pass_given_regular = 0.90
P_pass_given_irregular = 0.50

# Total probability of passing
P_pass = (P_pass_given_regular * P_regular) + \
         (P_pass_given_irregular * P_irregular)

# Bayes theorem
P_regular_given_pass = (P_pass_given_regular * P_regular) / P_pass

print("Probability student was regular given pass:",
      round(P_regular_given_pass, 4))
print("Percentage:",
      round(P_regular_given_pass * 100, 2), "%")
