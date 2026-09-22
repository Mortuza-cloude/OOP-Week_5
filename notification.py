class EmailNotification:
    def __init__(self,recipient, message):
        self.recipient = recipient
        self.message = message
    def send (self):
        print(f"[EMAIL] to {self.recipient}: {self.message}")

class SMSNotification:
    def __init__(self, recipient, message):
        self.reipient = recipient
        self.message = message
def send (self):
    print(f" [SMS] To {self.recipient}: {self.message}")

class PushNotification:
    def __init__(self,recipient, message):
        self.reipient = recipient
        self.message = message  

    def send(self):
        