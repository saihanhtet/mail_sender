# Python Flask based email sender

The Python mail sender script is a command-line tool that allows you to send emails from the command line using the Flask-Mail library. It provides a convenient way to send emails programmatically without the need for a full-fledged web application or server.

To use the mail sender script, you need to provide the required command-line arguments:

- --email: The email address of the recipient.
- --title: The title or subject of the email.
- --content or --msg: The content of the email. You can either provide a file path to a text file containing the email content (--content), or directly provide the email message as a string (--msg).

To use this, first clone the git repo by this command

```bash
git clone 

cd 

pip install requirements.txt
```
then to send the mail:
```bash
python mail_sender.py --email admin@gmail.com --title greeting --content content.txt
``` 

help:
```bash
python mail_sender.py --help
```