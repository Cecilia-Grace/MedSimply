import africastalking

#Africa's talking: notification sending(sandbox)
AT_USERNAME = 'sandbox'
AT_API_KEY = 'atsk_f3ea648d3b29e45c797ca0e41c94000956ae567ef38f4d1bf0bde8280c61b83d022234ec'

# Africa's talking: notification sending(live)
# AT_USERNAME = 'MedSimply'
# AT_API_KEY = 'atsk_654376d04c657e07c5ba21f4ba42fb1543a5133990bdf3a84579f057a08bb4822107dae0'

# Initialize Africa's Talking SDK (once)
africastalking.initialize(AT_USERNAME, AT_API_KEY)
sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(
            message=message,
            recipients=[to],
            sender_id='MedSimply Reminder'
        )
        return response
    except Exception as e:
        return f"SMS ERROR: {e}"
