import requests

def send_email(to_email_address, email_subject_line, email_body_text):
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "YOUR_API_KEY"),
		data={"from": "YOUR_FROM_EMAIL",
			"to": [to_email_address],
			"subject": email_subject_line,
			"text": email_body_text})

