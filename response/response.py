from validator_collection import validators, errors

try:
    email = validators.email(input("What's your email address: "))
    print("Valid")
except errors.InvalidEmailError or errors.EmptyValueError:
    print("Invalid")

