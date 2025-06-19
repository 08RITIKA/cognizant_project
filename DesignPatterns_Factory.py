class Notification:
    def notify(self):
        pass

class EmailNotification(Notification):
    def notify(self):
        return "Sending Email Notification"

class SMSNotification(Notification):
    def notify(self):
        return "Sending SMS Notification"

def get_notification(notification_type):
    if notification_type == 'email':
        return EmailNotification()
    elif notification_type == 'sms':
        return SMSNotification()

# Test
n = get_notification('sms')
print(n.notify())  # Output: Sending SMS Notification