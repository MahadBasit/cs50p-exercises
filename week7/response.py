import validators
 
 
def main():
    email = input("What's your email address? ")
    print("Valid" if is_valid(email) else "Invalid")
 
 
def is_valid(email):
    return bool(validators.email(email))
 
 
if __name__ == "__main__":
    main()
 