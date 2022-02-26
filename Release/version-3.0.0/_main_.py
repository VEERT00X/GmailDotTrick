import sys , essentials

"""
Generate Emails strings by adding a '.' in them.
"""

Email = sys.argv[1]

if "@gmail.com" in Email:
    print("Error please provide email without '@gmail.com' ")
    sys.exit(1)
else:
       
    print(essentials.GenerateEmail(email=Email))