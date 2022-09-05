import smtplib
def mailSend(receiver, subject, mail_content, mailfrom):
    from email.message import EmailMessage
    receiver = receiver.strip()
    mailfrom = mailfrom.strip()

    # The mail addresses and password
    sender_address = 'Unknown@unknown.com'
    sender_pass = 'hjh76^%&^%PP'
    receiver_address = receiver
    # Setup the MIME
    msg = EmailMessage()
    msg.add_header('Content-Type', 'text/html')
    mail_content = mail_content.encode('utf-8')
    msg.set_payload(mail_content)

    # msg.set_content(mail_content)
    msg['Subject'] = subject
    msg['From'] = mailfrom
    msg['To'] = receiver
    # msg['Cc'] = ''
    # msg['Bcc'] = 'microsoft.prime1@gmail.com,hypatiasoftwaresolutions@gmail.com'
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login('akashavinash397@gmail.com', "wlvyerrclsawifrh")  # login with mail_id and password
    session.send_message(msg)
    session.quit()
    # print('Mail Sent')           this is working well only to check that mail is going or not


# mailSend("singh.avinash397@gmail.com", "regarding", "helloavinash singh", "akashavinash397@gmail.com", )  this is only for check
