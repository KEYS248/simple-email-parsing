import email
import imaplib
import smtpd
import time

# This program reads emails and prints out the sender and subject line.
# Written by David Klein, January 7 2017

account = 'yourEmail@gmail.com'
password = 'yourPassword'
		# Gmail users will have to allow access to less secure apps from this link.
		#    https://myaccount.google.com/lesssecureapps
		# Gmail users with 2-Step Verification will have to generate a one-time App password.
		#    Simple follow the link above and click the lower 'Learn More' link.
smtp_server = 'imap.gmail.com'
smtp_port = 993

def readmail():
	try:
		mail = imaplib.IMAP4_SSL(smtp_server)
		mail.login(account, password)

		mail.select('inbox')
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		id_list = mail_ids.split()

		for i in reversed(id_list):
			type, data = mail.fetch(i, '(RFC822)')

			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode('utf-8', errors='ignore'))
					email_subject = msg['subject']
					email_from = msg['from']
					print('From: ' + email_from)
					print('Subject: ' + email_subject + '\n')

	except Exception as e:
		print('ERROR: ' + str(e))

readmail()