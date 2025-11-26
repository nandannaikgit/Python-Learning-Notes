class Notification:
    def send(self):
        print("Notification sent")

class EmailNotification(Notification):
    def send(self):
        print("Email sent.")
        
class SMSNotification(Notification):
    def send(self):
        print("SMS sent")
        
