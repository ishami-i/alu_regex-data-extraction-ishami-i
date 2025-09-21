#!/usr/bin/env python3

"""
This program extracts data from a bunch of text by removing or identifying:
- Emails
- Phone numbers
- URLs
- HTML tags
- Time in 12-hour or 24-hour format
- Hashtags
- Currency amounts
- Credit card numbers

Regex is used for extraction.
"""

import re
import os

# 1. Hashtags
def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

# 2. HTML tags
def extract_html_tags(text):
    pattern = r"<[^>]+>"
    return re.findall(pattern, text)

# 3. Phone numbers
def extract_phone_numbers(text):
    pattern = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    return re.findall(pattern, text)

# 4. Credit card numbers
def extract_credit_cards(text):
    pattern = r"(\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4})"
    return re.findall(pattern, text)

# 5. Currency amounts
def extract_currency_amounts(text):
    pattern = r"[$€£]\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

# 6. Emails
def extract_emails(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, text)

# 7. URLs
def extract_urls(text):
    pattern = r"(https?://[^\s]+)"
    return re.findall(pattern, text)

# 8. Times (12h or 24h)
def extract_times(text):
    pattern = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"
    return re.findall(pattern, text)

# -------------------------------
# Handle user text choice
# -------------------------------
def handle_text_choice():
    print("Here, you can choose to:")
    print("1. Enter your own text")
    print("2. Use the default sample text")

    choice = input("Enter 1 or 2: ").strip()

    match choice:
        case "1":
            user_text = input("\nPlease type your text: ")

            # Ensure sample_texts directory exists
            os.makedirs("sample_texts", exist_ok=True)

            # Save user text
            file_path = os.path.join("sample_texts", "user_text.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(user_text)

            print(f"\n Your text has been saved at: {file_path}")
            return user_text

        case "2":
            default_text = """
            Contact me at john.doe@example.com or (123) 456-7890.
            Visit https://example.com for details.
            Price: $19.99 or €45.00.
            Meeting time: 10:30 AM or 22:15.
            Use this card: 1234-5678-9012-3456.
            <p>This is a paragraph</p>
            #HashtagExample
            """
            print("\n Using default sample text.")
            return default_text.strip()

        case _:
            print("\n Invalid choice. Please restart and select 1 or 2.")
            return None

# -------------------------------
# Main Program
# -------------------------------
def main():
    text = handle_text_choice()
    if not text:
        return

    print("\n Extracted Data:")
    print("Emails:", extract_emails(text))
    print("Phone Numbers:", extract_phone_numbers(text))
    print("URLs:", extract_urls(text))
    print("HTML Tags:", extract_html_tags(text))
    print("Times:", extract_times(text))
    print("Hashtags:", extract_hashtags(text))
    print("Currency Amounts:", extract_currency_amounts(text))
    print("Credit Card Numbers:", extract_credit_cards(text))

# Run program
if __name__ == "__main__":
    main()

