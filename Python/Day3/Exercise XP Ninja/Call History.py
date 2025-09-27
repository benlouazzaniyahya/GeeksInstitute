class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  # Stores call records
        self.messages = []      # Stores messages

    def call(self, other_phone):
        """Simulate a call between phones."""
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)

    def show_call_history(self):
        """Display call history."""
        if not self.call_history:
            print(f"{self.phone_number} has no call history.")
        else:
            print(f"Call History for {self.phone_number}:")
            for record in self.call_history:
                print(record)

    def send_message(self, other_phone, content):
        """Send a message to another phone."""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        """Display messages sent by this phone."""
        outgoing = [msg for msg in self.messages if msg["from"] == self.phone_number]
        if not outgoing:
            print(f"{self.phone_number} has no outgoing messages.")
        else:
            print(f"Outgoing Messages from {self.phone_number}:")
            for msg in outgoing:
                print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        """Display messages received by this phone."""
        incoming = [msg for msg in self.messages if msg["to"] == self.phone_number]
        if not incoming:
            print(f"{self.phone_number} has no incoming messages.")
        else:
            print(f"Incoming Messages for {self.phone_number}:")
            for msg in incoming:
                print(f"From {msg['from']}: {msg['content']}")

    def show_messages_from(self, phone_number):
        """Display messages received from a specific phone number."""
        messages_from = [msg for msg in self.messages if msg["from"] == phone_number and msg["to"] == self.phone_number]
        if not messages_from:
            print(f"No messages from {phone_number} to {self.phone_number}.")
        else:
            print(f"Messages from {phone_number} to {self.phone_number}:")
            for msg in messages_from:
                print(msg["content"])


# ===== Example Usage =====
if __name__ == "__main__":
    phone1 = Phone("123-456-7890")
    phone2 = Phone("987-654-3210")

    phone1.call(phone2)
    phone2.call(phone1)

    phone1.show_call_history()
    phone2.show_call_history()

    phone1.send_message(phone2, "Hello, how are you?")
    phone2.send_message(phone1, "I'm good, thanks!")

    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()

    phone1.show_messages_from("987-654-3210")
