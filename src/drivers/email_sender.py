import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "qmdzrtfislauhz4z@ethereal.email"
    login = "qmdzrtfislauhz4z@ethereal.email"
    pwd = "ygaedu5ZKa87xh51q1"

    msg = MIMEMultipart()
    msg["from"] = 'viagens_confirmar@gmail.com'
    msg["to"] = ', '.join(to_addrs)

    msg["subject"] = "Confirmação de participação"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, pwd)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()