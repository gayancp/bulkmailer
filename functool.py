from __future__ import print_function
import base64
from email.message import EmailMessage
import time
import re
from Google import Create_Service


class functionality: 

    def startsending(self, creds, scopes, mail_body, mlist):
        self.mlist = mlist
        self.mail_body = mail_body
        self.creds = creds
        self.scopes = scopes

        #creds = google.auth.default()

        messageobj = EmailMessage()

        mail_body = mail_body.replace('Â­', '').replace('Â&nbsp', '&nbsp')

        messageobj.set_content(self.mail_body, 'html')

        apiconnect = Create_Service(self.creds, 'gmail' ,'v1', self.scopes)

        count = 1
    
        for mailaddress in self.mlist: 
            self.mailaddress = mailaddress
            messageobj['to'] = mailaddress 

            encoded_message = base64.urlsafe_b64encode(messageobj.as_bytes()).decode()

            create_message = {
                'msg': encoded_message
            }

            try:
                apiconnect.users().messages().send(userId="me", body=create_message)
                send = apiconnect.execute()
                print(f"Mail Id: {mailaddress} Sent successful")
                print('Mail Num: ', count, "\n")  
            except Exception as e:
                print(f"{mailaddress}: Not Delivered! {e}")
            
            time.sleep(5)
            count+=1


    def validitycheck(self, mlist):
        self.validmails = []
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,7}\b'
        for i in mlist:
            if i == "":
                continue
            else:
                if re.fullmatch(pattern, i.strip()):
                    self.validmails.append(i + " is Valid")
                else:
                    self.validmails.append(i + " is InValid")


obj = functionality()
print("please add your mail list to a txt file line by line")
x = int(input("Enter Prefered Number to do the task: \n1.Send mails \n2.Validity check"))
cred = input("Enter the name of your credential file(please add it to the same folder)")
mail_temp = input("Enter the name of your mail template file(please add it to the same folder)")
maillist = input("Enter the name of your mail list file file(please add it to the same folder)")
while x != 1 or x != 2:
    print("Please enter valid number!")
    x = int(input("Enter Prefered Number to do the task: \n1.Send mails \n2.Validity check"))
if x == 1:
    obj.startsending(cred, "mail.google.com", mail_temp, maillist)
elif x == 2:
    obj.validitycheck()
    for i in obj.validmails:
        print(i)