# source: http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/

import os
import smtplib
 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
 
def sendEmail(TO,
			  filePath,
              cmd):
    
    msg = MIMEMultipart()
    msg["From"] = cmd.mail_address
    msg["To"] = TO
    msg["Subject"] = cmd.mail_subject
    msg['Date'] = formatdate(localtime=True)
 
    # attach a file
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(filePath,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
    msg.attach(part)
 
    server = smtplib.SMTP(cmd.mail_host)
	if (cmd.mail_username & cmd.mail_password):
		server.login(cmd.mail_username, cmd.mail_password)
 
    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMsg = "Unable to send email. Error: %s" % str(e)