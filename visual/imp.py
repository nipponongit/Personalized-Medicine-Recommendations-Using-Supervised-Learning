import pandas as pd
import numpy as np


df = pd.read_csv("cleaned_filled_medicine.csv")


if 'Age_Group' not in df.columns:
    np.random.seed(42)
    age_groups = ['0-18', '19-35', '36-60', '60+']
    df['Age_Group'] = np.random.choice(age_groups, size=len(df))


if 'Dosage' not in df.columns:
    possible_doses = ['250mg', '500mg', '1000mg']
    df['Dosage'] = np.random.choice(possible_doses, size=len(df))

def get_medicine_by_age_symptom_severity(age, symptom, severity=None):
  
    if age <= 18:
        age_group = '0-18'
    elif 19 <= age <= 35:
        age_group = '19-35'
    elif 36 <= age <= 60:
        age_group = '36-60'
    else:
        age_group = '60+'
    
  
    medicines = df[
        (df['Age_Group'] == age_group) &
        (df['Reason'].str.contains(symptom, case=False, na=False))
    ]
    
  
    if severity:
        if severity.lower() in ['mild', 'light']:
            medicines = medicines[medicines['Dosage'].str.extract('(\d+)').astype(float)[0] <= 500]
        elif severity.lower() in ['heavy', 'severe', 'strong']:
            medicines = medicines[medicines['Dosage'].str.extract('(\d+)').astype(float)[0] > 500]
    
    if medicines.empty:
        return "No medicines found for the given inputs."
    else:
        return medicines[['Drug_Name', 'Reason', 'Dosage']].head(3)


try:
    age_input = int(input("Enter your age: "))
    symptom_input = input("Enter the symptom: ")
    severity_input = input("Is your symptom mild or heavy? (optional): ")

    severity = severity_input.strip() if severity_input.strip() != "" else None

    result = get_medicine_by_age_symptom_severity(age_input, symptom_input, severity)
    print(result)
except ValueError:
    print("Please enter valid input.")
