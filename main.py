import vonage

# Create a Vonage client instance with your API credentials
# Replace 'your_api_key' and 'your_api_secret' with your actual Vonage API credentials
client = vonage.Client(key='your_api_key', secret='your_api_secret')
sms = vonage.Sms(client)

# Send an SMS using the Vonage API 
# Replace 'your_brand_name', 'recipient_phone_number', and 'your_message_text' with actual values
response = sms.send_message(
    {
    'from': 'your_brand_name',
    'to': 'recipient_phone_number',
    'text': 'your_message_text'
    }
)

if response['messages'][0]['status'] == '0':
    print('Message sent successfully.')
else:
    print(f"Message failed with error: {response['messages'][0]['error-text']}")