import yagmail

try:
    yag = yagmail.SMTP('abrarhassan7809@gmail.com', 'pthxavulmyiwftau')

    yag.send('abrarhassan847@gmail.com', 'Testing Yagmail', ['Hurray, it worked!'])
    print("Email sent successfully")
except Exception as e:
    print("Error, email was not sent")
    print(e)
