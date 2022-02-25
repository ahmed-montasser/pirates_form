import os
import smtplib
import imghdr
from email.message import EmailMessage
import qrcode, io


def generateQrCode(name, url):
    Name = name
    Url = url
    msg = f'{Name}\n\n{Url}'
    qrImg = qrcode.make(msg)
    buf = io.BytesIO()
    qrImg.save(buf, format='JPEG')
    byte_im = buf.getvalue()
    return byte_im

def sendEmail(subject, from_address, to_address, name, url ):

    emailMessage = EmailMessage()

    emailMessage['Subject'] = subject
    emailMessage['From'] = from_address
    emailMessage['To'] = to_address
    emailMessage.set_content('Qr Code attached..\nHope You enjoy the event')

    f = generateQrCode(name, url)
    file_type = 'JPEG'
    file_name = f'{name}.JPEG'

    emailMessage.add_attachment(f, maintype='image', subtype=file_type, filename= file_name)


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login('fool.zeet2012@gmail.com', 'A7laDINO2016')
        smtp.send_message(emailMessage)