import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")


templates = {
    "1": {
        "subject": "Welcome!",
        "message": """Hello {name},

Welcome! We're glad to have you.

Best regards,
Your Name
"""
    },

    "2": {
        "subject": "Following Up",
        "message": """Hello {name},

I'm following up on our previous conversation.

Please let me know if you have any questions.

Best regards,
Your Name
"""
    },

    "3": {
        "subject": "Thank You",
        "message": """Hello {name},

Thank you for reaching out. We really appreciate your interest.

Best regards,
Your Name
"""
    }
}


def create_email(sender, recipient, subject, message):
	email = EmailMessage()

	email["From"] = sender
	email["To"] = recipient
	email["Subject"] = subject

	email.set_content(message)

	return email


def send_email(email):
	try:
		with smtplib.SMTP("smtp.gmail.com", 587) as server:
			server.starttls()
			server.login(email_address, email_password)
			server.send_message(email)

		print("✅ Email sent successfully!")

	except Exception as error:
		print(f"❌ Failed to send email: {error}")


def display_templates():
	print("""
============================== EMAIL TEMPLATES ==============================

1. Welcome
2. Follow-up
3. Thank You
""")


def email_automation():
	display_templates()

	choice = input("Choose template (1-3): ").strip()

	template = templates.get(choice)

	if template is None:
		print("❌ Invalid template.")
		return

	name = input("Recipient name: ").strip()

	recipients = input(
        "Enter recipient emails separated by commas: ").strip().split(",")

	recipients = [email.strip() for email in recipients]

	subject = template["subject"]
	message = template["message"].format(name=name)

	print("\n============================== EMAIL PREVIEW ==============================")
	print(f"To: {', '.join(recipients)}")
	print(f"Subject: {subject}")
	print(f"\n{message}")

	confirm = input("\nSend this email? (y/n): ").strip().lower()

	if confirm != "y":
		print("❌ Email cancelled.")
		return

	for recipient in recipients:
		email = create_email(
            email_address,
            recipient,
            subject,
            message
        )

	send_email(email)

email_automation()