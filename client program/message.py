import requests

# Django server URL
#todo: replace this ip address with address of host machine
url = 'http://0.0.0.0:8000/API/receive_message'

# The text message you want to send
print("Type exit to quit program")
while True:
    message = input("send to server: ")
    if message.lower() == "exit":
        break
    # Send the POST request with the message
    response = requests.post(url, data={'message': message})
    print(response)



# Print the response from the server
