# Secure Application

## 1 Broken access control and priviledge escalation due to improper authorization:
Attacker finds the admin login page using bruteforce. Attacker has a list of popular API endpoints. Then attacker logs in as a normal user and tries to access admin page. Due to improper authorization, attacker is granted access.

Solution:<br>
While checking the session, also check whether the user is Admin or not.

## 2 Session Hijacking 
Creating a hidden form that exploits the API that updates the user profile. Attacker places the form in the blog's content; whenever a user clicks on the button, its email is changed. Later attacker can use the forgot password feature to change the password.

Solution:<br>
Replace the HTML with Markdown and escape the HTML tags like `<script>`.<br>
Use tokens[or password] to update the profile.

## 3 Sensitive data access
All the profile pictures are stored on the server. The webpage sends a POST request to fetch the picture. The attacker exploits this. He can send mallicious file name in the request, like "../../../../../../../etc/passwd" or "../../config.py" 

Solution:<br>
Attacker replaces username with a malicious filename. So validate the username while fetching the profile picture.

## 4 Denial Of Service attack
Attacker can DOS the server, this makes the services unavailable the the normal users. 

Solution:<br>
1. Anomaly Based Distributed Denial of Service
Attack Detection and Prevention with Machine
Learning<br> This paper introduces a technique that uses anomaly detection techniques to detect DOS attack.

2. Using Monitoring tools to quickly sent notification in case of DOS.

3. Changing the proxy server.