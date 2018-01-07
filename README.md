# simple-email-parsing
Explanation and examples: simple programs to reading through emails with IMAP

## email-reader.py
Reads inbox emails from a specified email account using IMAP and prints out the senders and subject lines.

## read-response.py
Reads inbox emails from a specified email account using IMAP until a target string is found in the subject line.
Then a response email is sent using SMTP to that same sender.

## Resources
This information was the main source for building these programs.
* https://codehandbook.org/how-to-read-email-from-gmail-using-python/
* https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
* http://naelshiab.com/tutorial-send-email-python/
