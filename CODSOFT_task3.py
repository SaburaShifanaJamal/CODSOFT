import string
import random
def create_secret_key(size):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation
    all_chars = lowercase + uppercase + numbers + special_chars
    secret_key = ''.join(random.choice(all_chars) for _ in range(size))
    return secret_key
def run():
    while True:
        try:
            size = int(input("Enter the desired length for your secret key: "))
            if size <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    secret_key = create_secret_key(size)
    print(f"Generated Secret Key: {secret_key}")
if __name__ == "__main__":
    run()
