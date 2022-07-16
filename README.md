# ReListener-for-YT-Music
Python Script meant to be automated using cronjob that creates a weekly and running playlist of your tastes for Youtube Music using python, ytmusicapi, and Mailgun API

# Installation
1. ReListener requires a *headers_raw.txt* for the [main.py](https://github.com/nathaniellamjohnson/ReListener-for-YT-Music/blob/main/main.py) to function. Paste in your headers that you get from [the ytmusicapi copy authentication headers](https://ytmusicapi.readthedocs.io/en/latest/setup.html#copy-authentication-headers) section in *headers_raw.txt* and edit the 'with open()' in  [main.py](https://github.com/nathaniellamjohnson/ReListener-for-YT-Music/blob/main/main.py) with the path. 
2. If you want email to be sent via the [Mailgun API](https://www.mailgun.com/), edit the [main.py](https://github.com/nathaniellamjohnson/ReListener-for-YT-Music/blob/main/main.py) variable `target_email` to the email of your choice and edit the [mgemail.py](https://github.com/nathaniellamjohnson/ReListener-for-YT-Music/blob/main/mgemail.py) with your appropriate API key, domain, and email.
	-  If not, feel free to delete the email parts as they are not essential to playlist creation.
3. To automate ReListener using crontab, 
	1. Open crontab file in your terminal using `crontab -e`
	2. Add a line in the format `[cron schedule expression] [direct path to python interpreter] [direct path to main.py]`
		- For help with cron schedule expressions, visit [https://crontab.guru/](https://crontab.guru/)

# Requirements

- Python 3.6 or higher - [https://www.python.org](https://www.python.org)
- Mailgun Domain (required for emailing)

## Technologies Used

- Python
	- [ytmusicapi](https://github.com/sigma67/ytmusicapi)
- Mailgun API
- Cron

## Contributing

Pull requests are welcome. There are some features that could be implemented, but I'm happy with the current version. 










