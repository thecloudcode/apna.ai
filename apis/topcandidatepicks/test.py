import pandas as pd
import random
import faker

# Initialize Faker
fake = faker.Faker()

# Generate data
user_data = {
    "jobseeker_id" : [int(i) for i in range(1001, 1101)],
    "user_id": [int(i) for i in range(1001, 1101)]
}

# Create DataFrame
df = pd.DataFrame(user_data)

# Save to Excel
file_path = "jobseeker.csv"
df.to_csv(file_path, index=False, header=True)
