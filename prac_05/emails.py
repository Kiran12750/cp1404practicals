"""
Email and Name Storage
Estimate: 15 minutes
Actual:   10 minutes
"""
def main():
    email_dict = {}
    email = input("Email: ")

    while email:  # Continue as long as the email is not blank
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ('', 'y'):  # Default to 'y' if input is blank
            name = input("Name: ")

        email_dict[email] = name
        email = input("Email: ")  # Prompt for the next email

    # Print all stored emails and names
    print("\nStored Emails and Names:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extracts and formats the name from the email."""
    name_part = email.split('@')[0]  # Get the part before '@'
    name = name_part.replace('.', ' ').title()  # Replace '.' with space and capitalize
    return name

main()
