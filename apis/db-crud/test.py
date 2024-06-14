import csv
import random


# Function to generate a random English name
def generate_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(first_names) + " " + random.choice(last_names)


# Generate data for 100 rows
data = []
for i in range(1, 101):
    row = {
        "Id": i,
        "Name": generate_name(),
        "101": round(random.uniform(0, 10), 2),
        "102": round(random.uniform(0, 10), 2),
        "103": round(random.uniform(0, 10), 2),
        "104": round(random.uniform(0, 10), 2),
        "105": round(random.uniform(0, 10), 2),
        "106": round(random.uniform(0, 10), 2),
        "107": round(random.uniform(0, 10), 2),
        "108": round(random.uniform(0, 10), 2),
        "109": round(random.uniform(0, 10), 2),
        "110": round(random.uniform(0, 10), 2),
        "111": round(random.uniform(0, 10), 2),
        "112": round(random.uniform(0, 10), 2),
        "113": round(random.uniform(0, 10), 2),
        "114": round(random.uniform(0, 10), 2),
        "115": round(random.uniform(0, 10), 2),
        "116": round(random.uniform(0, 10), 2),
        "117": round(random.uniform(0, 10), 2)
    }
    data.append(row)

# Define the fieldnames for the CSV
fieldnames = ["Id", "Name", "101", "102", "103", "104", "105", "106", "107", "108", "109",
              "110", "111", "112", "113", "114", "115", "116", "117"]

# Write the data to a CSV file
csv_filename = "applicants_ratings_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_filename}' has been created successfully.")
