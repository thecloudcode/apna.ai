import pandas as pd
import random
import faker

# Initialize the faker generator
fake = faker.Faker()

# Generate data
data = {
    "company_id": [i for i in range(1, 101)],
    "name": [fake.company() for _ in range(100)],
    "website": [fake.url() for _ in range(100)],
    "job_openings": [random.randint(1, 50) for _ in range(100)],
    "applicants_taken": [random.randint(1, 20) for _ in range(100)],
    "job_apply_counts": [random.randint(10, 500) for _ in range(100)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('companies.csv', index=False)

df.head()
