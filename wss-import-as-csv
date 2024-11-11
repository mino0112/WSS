import pandas as pd

def pisano_period(n):
    if n == 1:
        return 1  # Pisano period for 1 is 1
    previous, current = 0, 1
    for i in range(0, n * n):  # Maximum length is n*n
        previous, current = current, (previous + current) % n
        # Check for the beginning of a new period
        if previous == 0 and current == 1:
            return i + 1

# Store Pisano periods in a dictionary
pisano_periods = {}
for i in range(1, 65536): # Limit of CSV file
    pisano_periods[i] = pisano_period(i)

# Create a DataFrame
df = pd.DataFrame(list(pisano_periods.items()), columns=['n', 'Pisano Period'])

# Save the DataFrame to a CSV file
df.to_csv('pisano_periods.csv', index=False)

print("Pisano periods saved to 'pisano_periods.csv'")

from google.colab import files

files.download('pisano_periods.csv')
