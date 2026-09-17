pin = input("Create a 6 digit PIN: ").strip()

# Check length (exactly 6) AND content (all digits)
if len(pin) == 6  and pin.isdigit():
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")
