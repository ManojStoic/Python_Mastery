import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('.\docs\index.html').read_text())
email = EmailMessage()

email['from'] = 'Test1'
email['to'] = 'test@gmail.com'
email['subject'] = 'Test - You have won 1,000,000 rupees!'

email.set_content(html.substitute({'name':'Test1'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('test@gmail.com','helloztmmyoldfriend1')
    smtp.send_message(email)
    print('All works now!') #returning SMTP authentication error

