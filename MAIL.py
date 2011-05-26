# source: http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/

import os
import smtplib
 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
 
def sendEmail(TO,
			  filePath,
              FROM="blub@bla.de"):
    HOST = "smtp.web.de"
 
    msg = MIMEMultipart()
    msg["From"] = FROM
    msg["To"] = TO
    msg["Subject"] = "You've got mail!"
    msg['Date']    = formatdate(localtime=True)
 
    # attach a file
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(filePath,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
    msg.attach(part)
 
    server = smtplib.SMTP(HOST)
    server.login(USERNAME, PASSWORD)  # optional
 
    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMsg = "Unable to send email. Error: %s" % str(e)
 
if __name__ == "__main__":
    sendEmail()