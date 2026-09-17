grade= float(input("Enter your Grade: "))

# Check lower and upper bounds (0-100)
if 0 <= grade <= 100:
    print("Valid Grade")
else:
    print("Invalid grade. Grade must be between 0 and 100.")

