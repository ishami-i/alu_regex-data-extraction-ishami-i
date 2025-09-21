# Regex Data Extractor
This is a CLI-based project for the ALU formative work, it is called the Regex Onboarding Hackathon.
The goal of this project is to extract data using regex.

#Data to be Extracted
The script will be able to detect:
-Email addresses
-URLs
-Phone numbers
-Credit card numbers
-Times in both 12-hour & 24-hour format
-HTML tags
-Hashtags
-Currency amounts

#Repository Structure
```
.
├── README.md
├── regex_extractor.py
└── sample_texts
```
Meanwhile, after extracting data using external text, the structure changed this structure
```
.
├── README.md
├── regex_extractor.py
└── sample_texts
    └── extracted_20250921_045251.txt
```

# How to use it
## Step 1: Getting Python 3
First things first, check if you have Python 3 installed on it.
If not, then install it using any of the following codes:
```
-    sudo apt install python3
-    sudo apt install python3-pip
-    brew install python3(for macOS)

```
Then use the following to check if it has been installed;
```
-    python3 --version
```
## Step 2: cloning repository
After that, clone the Repository using the following.
```
git clone https://github.com/ishami-i/alu_regex-data-extraction-ishami-i.git
cd alu_regex-data-extraction-ishami-i
```

## Step 3: Run the script
```
./regex_extractor.py
```
-After running, you get a prompt; you either choose external text or use the default.
for external will be save in sample_texts directory, as extracted_{timestamp}.txt

-By default, you get the result on the terminal.
#

# Licence
This project is licensed under the MIT License. Feel free to use, modify, and share—just keep it real and credit where it’s due.






