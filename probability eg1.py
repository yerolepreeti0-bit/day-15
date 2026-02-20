total_people = 100
smokers = 40
cancer_patients = 10
smokers_with_cancer = 8

# Conditional Probability Formula 
P_cancer_and_smoker = smokers_with_cancer / total_people
P_smoker = smokers / total_people
P_cancer_given_smoker = P_cancer_and_smoker / P_smoker

print("P(Cancer | Smoker) =", P_cancer_given_smoker)

#  Reverse probability P(Smoker/Cancer)

total_people = 100
smokers = 40
cancer_patients = 10
smokers_with_cancer = 8

P_smoker_and_cancer = smokers_with_cancer / total_people
P_cancer = cancer_patients / total_people
P_smoker_given_cancer = P_smoker_and_cancer / P_cancer

print("P(Smoker | Cancer) =", P_smoker_given_cancer)
