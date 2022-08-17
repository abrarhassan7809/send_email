import smtplib

gmail_user = 'abrarhassan7809@gmail.com'
gmail_password = 'pthxavulmyiwftau'

sent_from = gmail_user
sent_to = 'abrarhassan847@gmail.com'
message = 'this is python code testing'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, sent_to, message)
    print('Email sent!')

except:
    print('Something went wrong...')
