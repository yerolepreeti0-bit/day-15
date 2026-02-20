P_M1 = 0.50
P_M2 = 0.30
P_M3 = 0.20

# Defective rates
P_D_given_M1 = 0.02
P_D_given_M2 = 0.03
P_D_given_M3 = 0.05

# Total probability of defect
P_D = (P_D_given_M1 * P_M1) + \
      (P_D_given_M2 * P_M2) + \
      (P_D_given_M3 * P_M3)

# Bayes theorem
P_M3_given_D = (P_D_given_M3 * P_M3) / P_D

print("Probability defective product came from M3:",
      round(P_M3_given_D, 4))
print("Percentage:",
      round(P_M3_given_D * 100, 2), "%")
