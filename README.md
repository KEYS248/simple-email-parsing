# simple-email-parsing
Explanation and examples: simple programs to reading through emails with IMAP

## read.py
Reads inbox emails from a specified email account using IMAP and prints out the senders and subject lines.

## read-respond.py
Reads inbox emails from a specified email account using IMAP until a target string is found in the subject line.
Then a response email is sent using SMTP to that same sender.

## read-respond-attach.py
Scans inbox emails for target string in subject line using IMAP.
Response with specified attachment using SMTP.

## Resources
This information was the main source for building these programs.
* https://codehandbook.org/how-to-read-email-from-gmail-using-python/
* https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
* http://naelshiab.com/tutorial-send-email-python/
* https://bimleshsharma.wordpress.com/2013/06/06/python-script-to-send-email-with-images-attachment/
