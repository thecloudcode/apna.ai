import pandas as pd
from faker import Faker

fake = Faker()
num_records = 99
data = []
status_options = ['applied', 'interviewed', 'hired', 'rejected']

user_id = [i for i in range(1001,1018)]
id = [i for i in range(3,102)]
ind = 0
for _ in range(17):
    # name = fake.name()
    email = fake.email()
    # phone_number = fake.phone_number()
    date = fake.date_this_decade()
    # status = fake.random_element(elements=status_options)
    data.append([id[ind], email,  date])
    ind+=1

df = pd.DataFrame(data, columns=['jobseeker_id', 'job_id', 'date_applied', 'status'])
df.to_csv('User.csv', index=False)