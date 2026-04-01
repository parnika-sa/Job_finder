# 🎯 Job Finder — Automated Daily Job Alert Bot

> **Let your dream job come to your inbox — every day, automatically.**

A Python-based automation bot that fetches relevant job listings from the **Adzuna API** and delivers a beautifully formatted **HTML email alert** to your inbox daily — no manual searching needed.

---

## ✨ Features

- 🔍 **Multi-keyword & multi-location search** — search multiple job titles across multiple cities at once
- 📧 **Beautiful HTML email** — clean, professional job cards with Apply Now buttons
- 🔄 **Duplicate filtering** — same job never appears twice
- ⏰ **Scheduled daily alerts** — set your preferred time, the bot runs automatically
- 💰 **Salary display** — shown clearly in INR format
- ⚡ **Easy configuration** — just update `config.py`, everything else is handled

---

## 📁 Project Structure

```
Job_finder/
│
├── main.py           # Entry point — run the bot from here
├── job_fetcher.py    # Fetches jobs from the Adzuna API
├── email_sender.py   # Builds and sends the HTML email
├── config.py         # ⚙️ All your settings go here
└── requirements.txt  # Python dependencies
```

---

## ⚙️ Setup Guide

### Step 1 — Clone the repo

```bash
git clone https://github.com/parnika-sa/Job_finder.git
cd Job_finder
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Get a free Adzuna API Key

1. Create a free account at [developer.adzuna.com](https://developer.adzuna.com/)
2. Copy your `APP_ID` and `APP_KEY`

### Step 4 — Generate a Gmail App Password

> ⚠️ Your regular Gmail password will NOT work — you need an App Password

1. Go to Google Account → Security → Enable 2-Step Verification
2. Then visit: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Select "Mail" → Generate → Copy the 16-character password

### Step 5 — Configure `config.py`

```python
# Adzuna API
APP_ID = "your_app_id"
APP_KEY = "your_app_key"

# Email Settings
SENDER_EMAIL = "your_gmail@gmail.com"
SENDER_PASSWORD = "your_16char_app_password"
RECEIVER_EMAIL = "where_alerts_should_go@gmail.com"

# Job Search Settings
SEARCH_LOCATIONS = ["Mohali", "Chandigarh", "Zirakpur"]
SEARCH_KEYWORDS = ["SEO executive", "digital marketing"]

# Schedule
ALERT_TIME = "09:00"   # 24-hour format

# Filters
MAX_RESULTS_PER_SEARCH = 5
```

### Step 6 — Run the bot

```bash
python main.py
```

A test alert will be sent immediately on first run, then it will fire automatically every day at your scheduled time.

---

## 📧 Email Preview

Each email contains job cards with the following details:

| Field | Details |
|---|---|
| 🏢 Company | Company name |
| 📍 Location | City / Area |
| 💰 Salary | INR range (if available) |
| 📝 Description | Short job description |
| 🔗 Apply Now | Direct application link |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| [Adzuna API](https://developer.adzuna.com/) | Job data source |
| `smtplib` | Email sending via Gmail SMTP |
| `schedule` | Daily automation |
| `requests` | API calls |

---

## 🔧 Customization

- **Add a new city** → append to `SEARCH_LOCATIONS` list
- **Search a different job role** → add a keyword to `SEARCH_KEYWORDS`
- **Get more results** → increase `MAX_RESULTS_PER_SEARCH`
- **Change alert time** → update `ALERT_TIME = "HH:MM"`

---

## ⚠️ Important Notes

- The bot needs to **keep running** to send scheduled alerts. For 24/7 operation, consider hosting on a cloud platform like [PythonAnywhere](https://www.pythonanywhere.com/) or [Railway](https://railway.app/)
- Adzuna may have limited listings for some Indian cities — results can vary
- **Never push your API credentials or App Password to GitHub** — add `config.py` to `.gitignore`

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have a feature idea, feel free to open an Issue.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ and Python • <a href="https://github.com/parnika-sa/Job_finder">Ankit maurya</a></p>
