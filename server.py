import socket
import json

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def lambda_handler(event, context):
    # Process the event (HTTP GET request in this case)
    ip_address = get_ip_address()

    # Create the response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"My IP address is: {ip_address}"
    }

    return response

