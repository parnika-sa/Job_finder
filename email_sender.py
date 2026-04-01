# =============================================
# email_sender.py - HTML Email banana aur bhejna
# =============================================

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from config import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL
from job_fetcher import format_salary


def build_html_email(jobs):
    """
    Jobs ka ek sundar HTML email banata hai
    """
    today = datetime.now().strftime("%d %B %Y")
    job_count = len(jobs)

    # --- Job Cards HTML ---
    job_cards_html = ""

    if job_count == 0:
        job_cards_html = """
        <div style="text-align:center; padding:40px; color:#888;">
            <h3>Aaj koi nayi job nahi mili 😔</h3>
            <p>Kal phir check karenge!</p>
        </div>
        """
    else:
        for job in jobs:
            salary_text = format_salary(job['salary_min'], job['salary_max'])
            job_cards_html += f"""
            <div style="
                background: #ffffff;
                border: 1px solid #e0e0e0;
                border-left: 4px solid #4F46E5;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 16px;
            ">
                <h3 style="margin:0 0 8px 0; color:#1a1a2e; font-size:16px;">
                    {job['title']}
                </h3>
                <p style="margin:0 0 4px 0; color:#4F46E5; font-weight:600; font-size:14px;">
                    🏢 {job['company']}
                </p>
                <p style="margin:0 0 4px 0; color:#666; font-size:13px;">
                    📍 {job['location']}
                </p>
                <p style="margin:0 0 4px 0; color:#2ecc71; font-size:13px; font-weight:600;">
                    💰 {salary_text}
                </p>
                <p style="margin:8px 0; color:#555; font-size:13px; line-height:1.5;">
                    {job['description']}
                </p>
                <p style="margin:4px 0; color:#888; font-size:12px;">
                    🔍 Found via: <em>{job['keyword']}</em>
                </p>
                <a href="{job['url']}" style="
                    display: inline-block;
                    margin-top: 12px;
                    background: #4F46E5;
                    color: white;
                    padding: 8px 20px;
                    border-radius: 6px;
                    text-decoration: none;
                    font-size: 13px;
                    font-weight: 600;
                ">Apply Now →</a>
            </div>
            """

    # --- Full Email HTML ---
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="margin:0; padding:0; background:#f5f5f5; font-family: 'Segoe UI', Arial, sans-serif;">

        <div style="max-width:600px; margin:20px auto; background:#f5f5f5;">

            <!-- Header -->
            <div style="
                background: linear-gradient(135deg, #4F46E5, #7C3AED);
                padding: 30px 24px;
                border-radius: 12px 12px 0 0;
                text-align: center;
            ">
                <h1 style="color:white; margin:0; font-size:24px;">🎯 Daily Job Alert</h1>
                <p style="color:rgba(255,255,255,0.85); margin:8px 0 0; font-size:14px;">
                    {today} • Mohali | Chandigarh | Zirakpur
                </p>
            </div>

            <!-- Stats Bar -->
            <div style="
                background: #4F46E5;
                padding: 12px 24px;
                display: flex;
                text-align: center;
            ">
                <p style="color:white; margin:0; font-size:14px; width:100%; text-align:center;">
                    ✅ <strong>{job_count} new jobs</strong> found today matching your profile
                </p>
            </div>

            <!-- Job Cards -->
            <div style="background:#f5f5f5; padding:20px 24px;">
                {job_cards_html}
            </div>

            <!-- Footer -->
            <div style="
                background: #1a1a2e;
                padding: 20px 24px;
                border-radius: 0 0 12px 12px;
                text-align: center;
            ">
                <p style="color:#aaa; font-size:12px; margin:0;">
                    Ankit ka Job Alert Bot 🤖 | Auto-generated daily alert<br>
                    Built with Python + Adzuna API
                </p>
            </div>

        </div>
    </body>
    </html>
    """
    return html


def send_email(jobs):
    """
    Email bhejta hai Gmail SMTP se
    """
    try:
        print("\n📧 Email bhej raha hun...")

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🎯 Job Alert: {len(jobs)} Jobs | {datetime.now().strftime('%d %b %Y')}"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        html_content = build_html_email(jobs)
        msg.attach(MIMEText(html_content, "html"))

        # Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print(f"✅ Email successfully bheja! ({len(jobs)} jobs included)")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Gmail login failed! App Password check karo")
        print("   Guide: https://myaccount.google.com/apppasswords")
        return False
    except Exception as e:
        print(f"❌ Email send error: {e}")
        return False
