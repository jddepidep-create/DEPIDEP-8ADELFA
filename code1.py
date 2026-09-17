# Create a list of allowed choices
valid_methods = ["cash","gcash","card"]
# Get user input and remove extra spaces
method = input("Enter Payment method: ").strip().lower()
#Check if input exists in the allow list
if method in valid_methods:
    print("Valid payment method")
else:
    print("Invalid payment method")

