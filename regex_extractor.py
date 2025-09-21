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

If you enter your own text, the program also saves the text
and the extracted data (with a timestamp) inside sample_texts/.
"""

import re
import os
from datetime import datetime

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
# Handle text source
# -------------------------------

def handle_text_choice():
    """Ask user for text or use default sample."""
    print("Choose your text source:")
    print("1. Enter your own text")
    print("2. Use the default sample text")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        user_text = input("\nPlease type or paste your text: ")
        return user_text, True  # True = user provided text

    elif choice == "2":
        default_text = (
            "Contact me at john.doe@example.com or (123) 456-7890. "
            "Visit https://example.com for details. "
            "Price: $19.99 or €45.00. "
            "Meeting time: 10:30 AM or 22:15. "
            "Use this card: 1234-5678-9012-3456. "
            "<p>This is a paragraph</p> #HashtagExample"
        )
        print("\nUsing default sample text.")
        return default_text.strip(), False

    else:
        print("\nInvalid choice. Please restart and select 1 or 2.")
        return None, False


# -------------------------------
# Save extracted data
# -------------------------------

def save_results_with_timestamp(text, results):
    """Save the text and extracted data to a timestamped file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("sample_texts", exist_ok=True)
    out_file = os.path.join("sample_texts", f"extracted_{timestamp}.txt")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("Original text:\n")
        f.write(text)
        f.write("\n\n===== Extracted Data =====\n")
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
        f.write("==========================\n")

    print(f"\nResults saved to: {out_file}")


# -------------------------------
# Main program
# -------------------------------

def main():
    text, is_user_text = handle_text_choice()
    if not text:
        return

    results = {
        "Emails": extract_emails(text),
        "Phone Numbers": extract_phone_numbers(text),
        "URLs": extract_urls(text),
        "HTML Tags": extract_html_tags(text),
        "Times": extract_times(text),
        "Hashtags": extract_hashtags(text),
        "Currency Amounts": extract_currency_amounts(text),
        "Credit Card Numbers": extract_credit_cards(text),
    }

    print("\n===== Extracted Data =====")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("==========================")

    if is_user_text:
        save_results_with_timestamp(text, results)


if __name__ == "__main__":
    main()
