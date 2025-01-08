## BEGINNER LEVEL

# Step 1: Get input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Step 2: Calculate BMI
bmi = weight / (height ** 2)

# Step 3: Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Step 4: Display the results
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")

## ADVANCED LEVEL

#Check
import os
if os.path.exists("bmi_data.csv"):
    print("File found!")
else:
    print("File not found!")

#Creating a CSV file
import pandas as pd
try:
    # Load the data from CSV file
    bmi_data = pd.read_csv("bmi_data.csv")
    # Check if DataFrame is empty
    if bmi_data.empty:
        print("The CSV file is empty!")
    else:
        # Display the data in the console
        print(bmi_data)
except Exception as e:
    print(f"Error reading the file: {e}")


import matplotlib.pyplot as plt
# Count the occurrences of each category
category_counts = bmi_data["Category"].value_counts()
# Plotting the pie chart
category_counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["lightblue", "green", "orange", "red"])
# Adding title
plt.title("BMI Category Distribution")
# Display the plot
plt.show()


import matplotlib.pyplot as plt
# Count the occurrences of each category
category_counts = bmi_data["Category"].value_counts()
# Plotting the bar graph
category_counts.plot(kind="bar", color=["lightblue", "green", "orange", "red"])
# Adding title and labels
plt.title("BMI Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
# Display the plot
plt.show()


# Plotting the scatter plot of Weight vs Height
plt.scatter(bmi_data["Weight"], bmi_data["Height"], color="blue", alpha=0.5)
# Adding title and labels
plt.title("Weight vs Height")
plt.xlabel("Weight (kg)")
plt.ylabel("Height (m)")
# Display the plot
plt.show()


import matplotlib.pyplot as plt
# Plotting the histogram of BMI values
plt.hist(bmi_data["BMI"], bins=10, color="skyblue", edgecolor="black")
# Adding title and labels
plt.title("Distribution of BMI Values")
plt.xlabel("BMI")
plt.ylabel("Frequency")
# Display the plot
plt.show()
          

import seaborn as sns
# Plotting the pair plot to visualize relationships between multiple variables
sns.pairplot(bmi_data[["Weight", "Height", "BMI"]])
# Display the plot
plt.show()





















