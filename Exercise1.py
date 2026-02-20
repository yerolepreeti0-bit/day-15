# Given probabilities
P_rain = 0.30
P_no_rain = 1 - P_rain

P_traffic_given_rain = 0.60
P_traffic_given_no_rain = 0.20

# Total probability of traffic
P_traffic = (P_traffic_given_rain * P_rain) + \
            (P_traffic_given_no_rain * P_no_rain)

# Bayes theorem
P_rain_given_traffic = (P_traffic_given_rain * P_rain) / P_traffic

print("Probability it rained given traffic jam:",
      round(P_rain_given_traffic, 4))
print("Percentage:", round(P_rain_given_traffic * 100, 2), "%")
