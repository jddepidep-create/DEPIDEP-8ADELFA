import re
student_id = input("Enter student ID: ").strip()
# Pattern (4 digits (d\{4}), hyphen (-), 4 digits(d\{4})
pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern, student_id):
    print("Valid student ID")
else:
    print("Invalid student ID")