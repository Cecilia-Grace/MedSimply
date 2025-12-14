import africastalking

#Africa's talking: notification sending
AT_USERNAME = 'sandbox'
AT_API_KEY = 'atsk_f3ea648d3b29e45c797ca0e41c94000956ae567ef38f4d1bf0bde8280c61b83d022234ec'

# Initialize Africa's Talking SDK (once)
africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS

def send_sms(recipient_number: str, text_message: str):
    try:
        response = sms.send(
            message=text_message,
            recipients=[recipient_number],
            sender_id="MedSimply Reminder"
        )
        return response
    except Exception as e:
        return f"Error sending SMS: {e}"

