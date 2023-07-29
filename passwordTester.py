import re

def check_password_strength(password):
    # Define the criteria for password strength using regular expressions
    length_regex = r'.{8,}'        # Minimum length of 8 characters
    uppercase_regex = r'[A-Z]'     # At least one uppercase letter
    lowercase_regex = r'[a-z]'     # At least one lowercase letter
    digit_regex = r'\d'            # At least one digit
    special_char_regex = r'[^A-Za-z0-9]'  # At least one special character

    # Check each criterion and keep track of whether it's met or not
    meets_length = re.search(length_regex, password) is not None
    meets_uppercase = re.search(uppercase_regex, password) is not None
    meets_lowercase = re.search(lowercase_regex, password) is not None
    meets_digit = re.search(digit_regex, password) is not None
    meets_special_char = re.search(special_char_regex, password) is not None

    # Calculate the password strength score
    strength_score = 0

    if meets_length:
        strength_score += 2

    if meets_uppercase:
        strength_score += 2

    if meets_lowercase:
        strength_score += 2

    if meets_digit:
        strength_score += 2

    if meets_special_char:
        strength_score += 3

    return strength_score, {
        "length": meets_length,
        "uppercase": meets_uppercase,
        "lowercase": meets_lowercase,
        "digit": meets_digit,
        "special_char": meets_special_char
    }

def suggest_password_improvements(password_checks):
    suggestions = []
    if not password_checks["length"]:
        suggestions.append("Use at least 8 characters.")
    if not password_checks["uppercase"]:
        suggestions.append("Use at least one uppercase letter.")
    if not password_checks["lowercase"]:
        suggestions.append("Use at least one lowercase letter.")
    if not password_checks["digit"]:
        suggestions.append("Use at least one number.")
    if not password_checks["special_char"]:
        suggestions.append("Use at least one special character (e.g., @, #, $).")

    if suggestions:
        print("Your password could be stronger. Consider the following improvements:")
        for suggestion in suggestions:
            print("-", suggestion)

def main():
    while True:
        password = input("Enter your password (or 'q' to quit): ")
        
        if password.lower() == 'q':
            break
        
        strength_score, password_checks = check_password_strength(password)

        if strength_score >= 8:
            print("Strong password!")
        elif 5 <= strength_score < 8:
            print("Moderate password.")
            suggest_password_improvements(password_checks)
        else:
            print("Weak password. Please consider using a stronger password.")
            suggest_password_improvements(password_checks)

if __name__ == "__main__":
    main()
