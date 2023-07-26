# Get user's height in inches as input
height_inches = float(input("What is your height in inches? "))

# Convert height from inches to centimeters (1 inch = 2.54 cm)
height_cm = height_inches * 2.54

# Check if the user is tall enough to ride (minimum height requirement is 145cm)
if height_cm >= 145:
    print("You are tall enough to ride!")
else:
    print("Sorry, you need to grow some more to ride.")
