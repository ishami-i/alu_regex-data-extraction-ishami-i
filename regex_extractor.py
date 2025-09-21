#!/usr/bin/env python3
"""
regex_extractor.py

Extracts data from text using Regular Expressions:
- Emails
- Phone numbers
- URLs
- HTML tags
- Time in 12-hour or 24-hour format
- Hashtags
- Currency amounts
- Credit card numbers
"""

import re
import os

# -------------------------------
# Regex extractor functions
# -------------------------------

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

def extract_html_tags(text):
    return re.findall(r"<[^>]+>", text)

def extract_phone_numbers(text):
    pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r"(\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4})"
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    pattern = r"[$€£]\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

def extract_emails(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, text)

def extract_urls(text):
    return re.findall(r"(https?://[^\s]+)", text)

def extract_times(text):
    # Matches 24h (14:30) or 12h with AM/PM (2:30 PM)
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"
    return re.findall(pattern, text)


# -------------------------------
# Choose text source
# -------------------------------

def handle_text_choice():
    print("Choose your text source:")
    print("1. Enter your own text")
    print("2. Use the default sample text")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        user_text = input("\nPlease type or paste your text: ")

        os.makedirs("sample_texts", exist_ok=True)
        file_path = os.path.join("sample_texts", "user_text.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(user_text)

        print(f"\nYour text has been saved at: {file_path}")
        return user_text

    elif choice == "2":
        default_text = """
        Contact me at john.doe@example.com or (123) 456-7890.
        Visit https://example.com for details.
        Price: $19.99 or €45.00.
        Meeting time: 10:30 AM or 22:15.
        Use this card: 1234-5678-9012-3456.
        <p>This is a paragraph</p>
        #HashtagExample
        """
        print("\nUsing default sample text.")
        return default_text.strip()

    else:
        print("\nInvalid choice. Please restart and select 1 or 2.")
        return None


# -------------------------------
# Main program
# -------------------------------

def main():
    text = handle_text_choice()
    if not text:
        return

    print("\n===== Extracted Data =====")
    print("Emails:", extract_emails(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("URLs:", extract_urls(text))
    print("HTML Tags:", extract_html_tags(text))
    print("Times:", extract_times(text))
    print("Hashtags:", extract_hashtags(text))
    print("Currency Amounts:", extract_currency_amounts(text))
    print("Credit Card Numbers:", extract_credit_cards(text))
    print("==========================")

if __name__ == "__main__":
    main()
