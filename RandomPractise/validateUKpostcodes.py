'''
The postcode system in England (and the UK generally) follows specific alphanumeric rules and is divided into two parts separated by a space: the outward code and the inward code. The outward code includes the postcode area (one or two letters) and postcode district (one or two digits, sometimes followed by a letter). The inward code consists of a sector (one digit) and a unit (two letters). The total postcode length is typically 6 to 8 characters, including a space.

Here are key rules:

Outward code: 1 or 2 letters for area, followed by 1 or 2 digits for district (sometimes a district digit followed by a letter).

Inward code: 1 digit sector, followed by 2 letters unit.

Examples: "SW1W 0NY", "PO16 7GZ", "GU16 7HF", "L1 8JQ".

The format can be summarized roughly as:

One or two letters

One or two digits (or a digit and a letter)

Space

One digit

Two letters
'''

import re
def insert_space(postcode):
    print(f"Postcode is: {postcode}")
    postcode = postcode.strip().upper()
    print(f"Postcode after strip is now: {postcode}")
    if ' ' not in postcode and len(postcode) > 3:
        postcode = postcode[:-3] + ' ' + postcode[-3:]
    return postcode

def validate_postcode_regex_simple(postcode):
    postcode = insert_space(postcode)
    pattern = r"^[A-Z]{1,2}[0-9]{1,2}[A-Z]? [0-9][A-Z]{2}$"
    return re.match(pattern, postcode) is not None

def validate_postcode_bruteforce_simple(postcode):
    postcode = insert_space(postcode)
    # rest of validation code unchanged from before
    if len(postcode) < 6 or len(postcode) > 7:
        return False
    
    if postcode.count(' ') != 1:
        return False
    
    outward, inward = postcode.split(' ')
    
    if len(outward) < 2 or len(outward) > 4:
        return False
    
    if len(inward) != 3:
        return False
    
    letters = ''
    digits_and_letter = ''
    for c in outward:
        if c.isalpha():
            letters += c
        else:
            digits_and_letter += c
    
    if len(letters) < 1 or len(letters) > 2:
        return False
    
    if len(digits_and_letter) < 1 or len(digits_and_letter) > 2:
        return False
    
    if not digits_and_letter[0].isdigit():
        return False
    
    if len(digits_and_letter) == 2 and not (digits_and_letter[1].isdigit() or digits_and_letter[1].isalpha()):
        return False
    
    if not inward[0].isdigit():
        return False
    if not inward[1].isalpha() or not inward[2].isalpha():
        return False
    
    return True

# Example test
postcodes = [
    "A99AA",   # without space
    "AA9A9AA", # without space
    "AA999AA", # without space
    "A9 9AA",  # with space
    "AA9 9AA", # with space
    "B12BB",   # without space
]

print("Regex Simple Validation:")
# for pc in postcodes:
#     print(f"{pc}: {validate_postcode_regex_simple(pc)}")

print("\nBrute Force Simple Validation:")
for pc in postcodes:
    print(f"{pc}: {validate_postcode_bruteforce_simple(pc)}")
