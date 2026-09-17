try:
    # Data type check: Try converting input into a float
    score = float(input("Enter examination score: "))

    # Range check must be between 0-100
    if 0 <= score <= 100:
        print("Valid Score")
    else:
        print("Invalid grade. Score must be between 0 and 100.")

except ValueError:
    # Triggered if Conversion Fails
    print("Invalid input. Please enter a number.")