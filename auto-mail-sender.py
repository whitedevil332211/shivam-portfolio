import smtplib
import time
import csv
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP setup (for Gmail you need an App Password)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "your-email@gmail.com"       # replace with your email
SMTP_PASS = "your-app-password"          # replace with your Gmail App Password

# Your links
RESUME_LINK = "https://whitedevil332211.github.io/shivam-portfolio/shivam_resume.html"
PROJECT_LINK = "https://whitedevil332211.github.io/shivam-portfolio/"

# Cold Email Template
def make_email(name, company):
    greeting = f"Hi {name}," if name else "Hi,"
    company_line = f"I’m Shivam, a web designer and developer. I can help {company} with responsive UI/UX and clean frontend execution." if company else "I’m Shivam, a web designer and developer specializing in responsive UI/UX and clean frontend execution."

    body = f"""{greeting}

{company_line}

I’ve built a Zomato‑style food discovery web app (listing, detail pages, responsive design). You can check it here:

Resume: {RESUME_LINK}
Project: {PROJECT_LINK}

I am immediately available for Web Design & Development roles.

Best regards,
Shivam Kumar
Email: {SMTP_USER}
"""
    return body

# Function to send email
def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

# Load recipients from CSV
def load_recipients(csv_file):
    recipients = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipients.append({
                "name": row.get("name", ""),
                "email": row.get("email", ""),
                "company": row.get("company", "")
            })
    return recipients

# Main
if __name__ == "__main__":
    recipients = load_recipients("recipients.csv")
    daily_limit = 60   # 50–70 emails per day

    for i, r in enumerate(recipients[:daily_limit]):
        body = make_email(r["name"], r["company"])
        subject = "Frontend/UI Portfolio — Shivam Kumar"
        try:
            send_email(r["email"], subject, body)
            print(f"✓ Sent to: {r['email']}")
        except Exception as e:
            print(f"✗ Failed: {r['email']} → {e}")

        # Random delay between emails (45–90 seconds)
        delay = random.randint(45, 90)
        print(f"...waiting {delay} seconds")
        time.sleep(delay)

    print("All emails for today sent ✅")
