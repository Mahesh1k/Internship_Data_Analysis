import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\kudir\Downloads\Data-analyst-Data.csv")

# Preprocess 'Family Income' column
data['Family Income'] = data['Family Income'].str.replace(',', '')  # Remove commas

def convert_income_to_lakhs(income):
    if 'Lakh+' in income:
        return int(income.split()[0])
    elif '-' in income:
        range_values = income.split('-')
        upper_limit = int(range_values[1].split()[0])
        if upper_limit == 0:
            return 0
        else:
            return upper_limit
    else:
        return float(income) / 100000  # Convert other values to Lakhs

# Convert 'Family Income' to Lakhs
data['Family Income'] = data['Family Income'].apply(convert_income_to_lakhs)

# Calculate average income in Lakhs
average_income = data['Family Income'].mean()
print(f"Average Income (in Lakhs): {average_income:.2f} Lakhs")
