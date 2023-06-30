import requests
import argparse
from flask_mail import Mail, Message
from flask import Flask
import os
import dotenv
from string import Template


dotenv.load_dotenv(dotenv.find_dotenv())
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USER")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASS")

mail = Mail(app)


class SendMail:
    def __init__(self, email, title, content):
        self.email = email
        self.content = content
        self.title = title

    def send(self):
        with app.app_context():
            if self.email and self.content:
                msg_title = self.title
                sender = "noreply@app.com"
                msg = Message(msg_title, sender=sender,
                              recipients=[self.email])
                msg.body = ""

                data = {
                    'app_name': "LUCIUS AI",
                    'title': self.title,
                    'body': self.content,
                }
                template = """
                <html>
                <head><title>${app_name}</title></head>
                <body>
                    <h1>${title}</h1>
                    <p>${body}</p>
                </body>
                </html>
                """
                email_content = Template(template).substitute(data)
                msg.html = email_content
                try:
                    mail.send(msg)
                    print("Email sent to {}".format(self.email))
                except Exception as e:
                    print("Email was not sent to {} due to {}".format(self.email, e))
            else:
                raise ValueError("Email and content are required.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--email", help="Email address to send the mail", required=True)
    parser.add_argument(
        "--title", help="Email title to send the mail", required=True)
    parser.add_argument(
        "--content", help="File containing the email content")
    parser.add_argument("--msg", help="Email message String for content")
    args = parser.parse_args()

    if args.content:
        with open(args.content, "r") as file:
            content = file.read()
    elif args.msg:
        content = args.msg
    else:
        raise ValueError("Need message to send mail")
    mailer = SendMail(args.email, args.title, content)
    mailer.send()
