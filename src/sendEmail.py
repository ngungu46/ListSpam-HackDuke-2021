import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def emailOut(targetEAddress):
    #connect to gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login("smartList@gmail.com", "??????")  #We'd use an email address of our company

    msg = MIMEMultipart()
    msg['From'] = 'smartList@gmail.com'
    msg['To'] = targetEAddress
    msg['Subject'] = "Your Weekly Events Suggestions! "
    message = "Dear Aspirant Student! \n\n You've done so well in the past week. With a new week coming, there is another week full of exciting events on the horizon! Please check the image below for the top picks we collected for you and you only! \n\n Best,\n The Smart List Team"
    msg.attach(MIMEText(message))

    fp = open('W1UID001.jpg', 'rb')
    msgImage = MIMEImage(fp.read(), name="Smart List")
    fp.close()
   
    msg.attach(msgImage)

    # mes = "\n\n Best,\n The Smart List Team"
    # msg.attach(MIMEText(mes))


    server.send_message(msg)

    server.quit()

targetAddresses = 'tw123@duke.edu'
emailOut(targetAddresses)