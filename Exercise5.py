
P_experienced = 0.60
P_fresher = 0.40

# Interview success rates
P_cleared_given_experienced = 0.70
P_cleared_given_fresher = 0.30

# Total probability of clearing
P_cleared = (P_cleared_given_experienced * P_experienced) + \
            (P_cleared_given_fresher * P_fresher)

# Bayes theorem
P_experienced_given_cleared = \
    (P_cleared_given_experienced * P_experienced) / P_cleared

print("Probability applicant was experienced given cleared:",
      round(P_experienced_given_cleared, 4))
print("Percentage:",
      round(P_experienced_given_cleared * 100, 2), "%")
