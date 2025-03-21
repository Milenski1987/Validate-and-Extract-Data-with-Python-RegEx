import re
import time

# Catch if user choice is out of range of commands
class UnknownCommand(Exception):
    pass


def find_email():
    """
    This function should find and return an email address from the given text.
    Using re.search() with a regex pattern to match an email format.
    """
    text = input("Please enter text: ")
    # regex pattern
    email_pattern = r"(([a-z0-9]+[\-\.\_]?[a-z0-9]*)@[a-z]+(\.[a-z]+)+)"
    # Search for the email in the text
    match = re.search(email_pattern, text, flags=re.IGNORECASE)
    # Return the matched email (if found)
    if match:
        return match.group()
    return "Email not found!"


def extract_emails_and_phones():
    """
    This function should find and return all email addresses and phone numbers from the given text.
    Use re.findall() with proper regex patterns to match emails and phone numbers.
    """
    text = input("Please enter text: ")
    # Regex patterns
    email_pattern = r"(([a-z0-9]+[\-\.\_]?[a-z0-9]*)@[a-z]+(\.[a-z]+)+)"
    phone_pattern = r"(\+\d{0,3}(\s|\-){1}\d{3}\2\d{3,4}\2\d{3,4})"
    # Find all emails in the text
    emails = []
    email_results = re.findall(email_pattern, text, flags=re.IGNORECASE)
    for result in email_results:
        emails.append(result[0])
    # Find all phone numbers in the text
    phone_numbers = []
    phone_numbers_results = re.findall(phone_pattern, text)
    for result in phone_numbers_results:
        phone_numbers.append(result[0])
    # Return both lists (emails, phones)
    return emails, phone_numbers


def validate_email():
    """
    This function should check if the email is valid.
    Use re.match() with a regex pattern to match a correct email format.
    """
    email = input("Please enter email for validation: ")
    # Email regex pattern
    email_pattern = r"\b[a-z0-9]+[\_\.\-]?[a-z0-9]+@[a-z]+\.[a-z]+\b"
    # Return True if the email is valid, otherwise False
    match = re.match(email_pattern, email, flags=re.IGNORECASE)
    if match:
        return True
    return False


def validate_password():
    """
    This function should check if the password is strong.
    Use re.match() with a regex pattern to check for the required conditions.
    """
    password = input("Please enter password for validation: ")
    # Password regex pattern
    password_pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    # Return True if the password meets all conditions, otherwise False
    match = re.match(password_pattern, password)
    if match:
        return True
    return False


def replace_word():
    """
    This function should replace all occurrences of 'old_word' with 'new_word' in the given text.
    Use re.sub() for this task.
    """
    text = input("Please enter text: ")
    old_word = input("Enter word to be replaced: ")
    new_word = input("Enter word replacement: ")
    # regex pattern
    pattern = fr"{old_word}"
    # Return the modified text
    result = re.sub(pattern, new_word, text)
    return result


def extract_dates():
    """
    This function should find and return all dates in specific format from the given text.
    Use re.findall() with proper regex patterns to match dates.
    """
    text = input("Please enter text to search for dates: ")
    # dates regex pattern
    date_pattern = r"\b(0[1-9]|[1-2][0-9]|3[0-1])([(\/\-\.])([A-Z][a-z]{2}|0[1-9]|1[0-2])\2([0-9]{4})\b"
    valid_dates = []

    dates = re.findall(date_pattern, text)
    for date in dates:
        valid_dates.append(f"Day: {date[0]} Month: {date[2]} Year: {date[3]}")
    return valid_dates


def extract_urls():
    """
    This function should find and return all URLs found the given text.
    Use re.findall() with proper regex patterns to match URLs.
    """
    text = input("Please enter text to look for URLs: ")
    # URLs regex pattern
    url_pattern = r"\b((https:\/\/|www\.+)([a-z]+\-?[a-z]+)(\.[a-z]+){1,2})\b"

    links = []
    links_result = re.findall(url_pattern, text)
    for link in links_result:
        links.append(link[0])
    return links

def greeting():
    """
    This function gives the user the option to choose what type of work they want to do
    """
    print("Choose what you want to do:")
    print("1. Find email in given text.")
    print("2. Extract emails and phone numbers from given text.")
    print("3. Validate email.")
    print("4. Validate Password.")
    print("5. Replace all occurrences of chosen word with new word in given text")
    print("6. Extract valid dates from given text")
    print("7. Find and extract URLs from given text")
    print("0. Exit")

def user_choices():
    """
    Brain of the program
    """
    while True:
        # User needs to enter a valid integer
        try:
            user_choice = int(input("Make your choice by entering a number: "))
            if user_choice not in [1, 2, 3, 4, 5, 6, 7, 0]:
                raise UnknownCommand
        except ValueError:
            print("Please enter valid positive number:")
        except UnknownCommand:
            print("Please choose number from list above:")
        else:
            break

    if user_choice == 0:
        goodbye()
        exit()

    choices = {
        1: find_email,
        2: extract_emails_and_phones,
        3: validate_email,
        4: validate_password,
        5: replace_word,
        6: extract_dates,
        7: extract_urls
        }
    print(choices[user_choice]())

    time.sleep(2)

    print("Do you want to continue with another option in program?")
    next_choice = input("Y or N: ")
    if next_choice.upper() == "Y":
        print()
        greeting()
        user_choices()
    else:
        goodbye()
        exit()

def goodbye():
    """
    Something for goodbye
    """
    print("Goodbye")
    print("Thank you for support")


def main():
    print("Welcome to the world of RegEx")
    greeting()
    user_choices()


if __name__ == '__main__':
    main()
