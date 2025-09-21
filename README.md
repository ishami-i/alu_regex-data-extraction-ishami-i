# 📊 Regex Data Extractor

This Python program extracts useful data from text using **regular expressions (regex)**.  
It can identify and extract:

- 📧 Emails  
- 📞 Phone Numbers  
- 🔗 URLs  
- 🏷️ HTML Tags  
- ⏰ Times (12-hour & 24-hour formats)  
- #️⃣ Hashtags  
- 💰 Currency Amounts  
- 💳 Credit Card Numbers  

---

## 🚀 Features
- Works with **user-provided text** or a **default sample text**.  
- Saves your input to a `sample_texts/user_text.txt` file for future use.  
- Clean and modular extraction functions.  
- Easy to extend with more regex patterns.  

---

## 📦 Requirements
- Python **3.10+** (for `match`/`case` structure).
- No external dependencies (uses only `re` and `os` from ste this repo or copy the script into a `.py` file:
   ```bash
   git clone https://github.com/yourusername/regex-data-extractor.git
   cd regex-data-extractor

