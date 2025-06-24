import re
import os
from datetime import datetime

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║          WEAK PASSWORD SCANNER v1.0                ║
    ║    Coded by Pakistani Ethical Hacker               ║
    ║         Mr. Sabaz Ali Khan                         ║
    ║    Date: {}                                       ║
    ╚════════════════════════════════════════════════════╝
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(banner)

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters)")
    else:
        score += 2

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 2
    else:
        feedback.append("Add uppercase letters")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 2
    else:
        feedback.append("Add lowercase letters")

    # Check for numbers
    if re.search(r'\d', password):
        score += 2
    else:
        feedback.append("Add numbers")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        feedback.append("Add special characters")

    # Determine strength based on score
    if score <= 4:
        strength = "Weak"
    elif score <= 8:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    while True:
        print("\n[1] Scan Password")
        print("[2] Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            password = input("\nEnter password to scan: ")
            strength, feedback = check_password_strength(password)
            
            print("\nPassword Strength: {}".format(strength))
            if feedback:
                print("Suggestions to improve password:")
                for suggestion in feedback:
                    print("- {}".format(suggestion))
        
        elif choice == '2':
            print("\nThank you for using Weak Password Scanner!")
            print("Stay secure! - Mr. Sabaz Ali Khan")
            break
        
        else:
            print("\nInvalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()