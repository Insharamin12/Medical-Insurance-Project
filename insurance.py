# Dictionary to store medical insurance costs for different individuals
medical_costs = {"Marina": 6607.0, "Vinay": 3225.0}
# Update the dictionary with additional individuals and their costs
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

print(medical_costs)
# Add a numeric key to demonstrate dictionary flexibility
medical_costs[1] = 3325.0
print(medical_costs)

# Calculate total insurance cost
total_cost = 0

# Sum up all insurance costs
for cost in medical_costs.values():
   total_cost += cost

# Calculate and display average insurance cost
average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

# Lists containing names and corresponding ages
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# Create a dictionary mapping names to ages using zip
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

# Retrieve and display Marina's age using get() method
marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

# Initialize empty dictionary for detailed medical records
medical_records = {}

# Add detailed medical records for each individual
# Each record contains age, sex, BMI, number of children, smoking status, and insurance cost
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

# Display Connie's specific insurance cost
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

# Print detailed information for each person in the medical records
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))

# Function to update medical records with new patient information
def update_medical_records(name, data):
    medical_records[name] = data
    print(f"Updated medical record for {name}.")

# Create and add a new patient record
new_record = {"Age": 29, "Sex": "Non-binary", "BMI": 22.5, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 4100.0}
update_medical_records("Alex", new_record)

# Print all medical records after the update
print("\nUpdated medical records:")
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))