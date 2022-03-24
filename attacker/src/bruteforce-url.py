from string import ascii_lowercase
import requests
import json
import sys

def get_response_code(url, target):
    response = requests.get(url + "/" + target)
    return response.status_code
    
def gen_str(crr, limit=13):
    if crr != "":
        # resp_code = get_response_code("http://localhost:8000/", crr)
        resp_code = 200
        if resp_code in range(200, 300):
            print(crr, resp_code)
        

    if len(crr) > limit: return

    for ch in ascii_lowercase:
        gen_str(crr + ch, limit)
    

if __name__ == "__main__":
    gen_str("", 10)