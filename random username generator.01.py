import random
import string
# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Fierce", "Brave", "Clever", "Swift", "Mighty", "Sly", "Jolly"]
nouns = ["Dragon", "Tiger", "Falcon", "Warrior", "Wizard", "Knight", "Ninja", "Shadow", "Panther", "Ghost"]
def generate_username(include_number=False, include_special=False):
    """Generates a random username based on user preferences."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    if include_number:
        username += str(random.randint(10, 99))  # Adds a random 2-digit number
    if include_special:
        username += random.choice(string.punctuation)  # Adds a random special character
    return username
def save_to_file(username, filename="usernames.txt"):
    """Saves the generated username to a file."""
    with open(filename, "a") as file:
        file.write(username + "\n")
def main():
    print("Welcome to the Random Username Generator!")
    while True:
        include_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        username = generate_username(include_number, include_special)
        print(f"Generated Username: {username}")
        save = input("Save this username to file? (yes/no): ").strip().lower()
        if save == "yes":
            save_to_file(username)
            print("Username saved successfully!")
        another = input("Generate another username? (yes/no): ").strip().lower()
        if another != "yes":
            print("Thanks for using the username generator!")
            break
if __name__ == "_main_":
    main()
