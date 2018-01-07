import imaplib
import time
import smtplib
import email
import email.mime.multipart
import email.mime.text

# This program searches inbox emails for a specific string in the subject line, then sends a reply email to the sender.
# Written by David Klein, January 7 2017

def main():

	# The variables below are for you to define to your preferences.
	account = 'yourEmail@gmail.com'
	password = 'yourPassword'
		# Gmail users will have to allow access to less secure apps from this link.
		#    https://myaccount.google.com/lesssecureapps
		# Gmail users with 2-Step Verification will have to generate a one-time App password.
		#    Simple follow the link above and click the lower 'Learn More' link.
	target = 'Automatic Email Request' # The subject line string you want to find.
	limit = 20 # The number of emails in the inbox the program should read for each loop.
	reply_subject = 'Automatic Email Request: Accepted.'
	reply_body = 'Sending response to same recipient now.'

	# Variables to repeating the loop and storing the address of the target string sender.
	recipient = ''
	searching = True
	loop = 1

	while searching:
		print('Running loop {}...'.format(loop))
		searching, recipient = read_mail(account, password, target, limit, searching, recipient)
		time.sleep(60) # The program waits 60 seconds before attempting to read the inbox again.
		loop += 1

	print('Target found, sending confirmation to: ' + recipient)
	send_mail(account, password, recipient, reply_subject, reply_body)

def send_mail(account, password, recipient, reply_subject, reply_body):
	"""
	Sends an email from a specified email account to a specified email address.

	:param account: user email address
	:param password: user email password
	:param recipient: email address of the sender of the target string
	:param reply_subject: subject of reply email
	:param reply_body: body of reply email
	"""
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(account, password)

		msg = email.mime.multipart.MIMEMultipart()
		msg['From'] = account
		msg['To'] = recipient
		msg['Subject'] = reply_subject
		body = reply_body
		msg.attach(email.mime.text.MIMEText(body, 'plain'))

		text = msg.as_string()
		server.sendmail(account, recipient, text)
		server.quit()

	except Exception as e:
		print('send_mail error: ' + str(e))

def read_mail(account, password, target, limit, searching, recipient):
	"""
	Reads a specified email account, then returns the address when the target string is found.

	:param account: user email address
	:param password: user email password
	:param target: string to be searched for in the subject line
	:param limit: limit to number of inbox emails to iterate over
	:param searching: if the program should continue searching for the target string
	:param recipient: email address of the sender of the target string
	:return: searching, recipient
	"""
	try:
		smtp_server = 'imap.gmail.com'
		mail = imaplib.IMAP4_SSL(smtp_server)
		mail.login(account, password)
		count = 0

		mail.select('inbox')
		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]
		id_list = mail_ids.split()

		for i in reversed(id_list):
			type, data = mail.fetch(i, '(RFC822)')
			# These 3 lines below count the emails read for this loop and stops it once the limit is reached.
			if count >= limit:
				break
			count += 1

			for response_part in data:
				if isinstance(response_part, tuple):
					msg = email.message_from_string(response_part[1].decode('utf-8', errors='ignore'))
					email_subject = msg['subject']
					email_from = msg['from']
					if(email_subject == target):
						searching = False
						recipient = email_from

		mail.close()
		return searching, recipient

	except Exception as e:
		print('read_mail error: ' + str(e))

main()