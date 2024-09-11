import json
from faker import Faker

# Initialize Faker
fake = Faker()

# Read the JSON file
with open('student_audit_data.json', 'r') as file:
    data = json.load(file)

# Replace student names with fake names including a middle initial
for student in data:
    first_name = fake.first_name()
    middle_initial = fake.first_name()[0] + '.'
    last_name = fake.last_name()
    student['student_name'] = f"{first_name} {middle_initial} {last_name}"

for student in data:
    advisor_name = fake.first_name()
    advisor_initial = fake.first_name()[0] + '.'
    advisor_last_name = fake.last_name()
    student['advisor']= f"{advisor_name} {advisor_initial} {advisor_last_name}"
    
# Write the modified data to a new JSON file
with open('student_audit_data_with_fake_names.json', 'w') as file:
    json.dump(data, file, indent=2)
    
