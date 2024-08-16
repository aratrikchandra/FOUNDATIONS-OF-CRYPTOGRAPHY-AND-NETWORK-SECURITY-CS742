# Question 1

Preamble: Did I tell Agent X has a kid of college going age? Her father is her role model, and unlike her father who had no major training in security, she is an aspiring hacker (ethical or not, yet to be seen), wanting to learn all kinds of security topics.

She is currently enrolled as a student in a course CS-224 in an online ed-tech platform. The site is hosted on http://localhost:80/ Her friend "Rajesh" however is waitlisted in this course. She wants to see if she can find a way to login as "admin" user and convert Rajesh's waitlisted status to enrolled.

Submission Details:
- Once you convert Rajesh's waitlisted status, you will get a flag, submit it in "/home/labDirectory/flag.txt". It will serve as proof of concept of your work.

Guidance:
You need to find  a way to login as "admin" user and convert Rajesh's waitlisted status.
To make things a bit easier for you, here is some additional info (which in the real world you wouldn’t normally have). The query used to run on backend application by PHP is:  "SELECT * FROM `users` WHERE `username` = '$username' AND `password` = '$password'"

Submission Details:
- Once you convert Rajesh's waitlisted status, you will get flag, submit it in "/home/labDirectory/flag.txt". It will serve as proof of concept of your work.

Solution:

First stop your apache2 server and then from vlab stop/start apache2 server
Go to local host and their will find a login form with username and password

You can manipulate the SQL query to always return true by injecting a payload like ' OR '1'='1. This would make the query "SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '' OR '1'='1'". Since '1'='1' is always true, this would log you in as the first user in the database, which is often the admin user.

Access the Admin Account: If the first user is not the admin, you might need to use a UNION-based SQL Injection to log in as the admin. This involves using the UNION SQL operator to combine the results of the original query with results from a new query that returns the admin credentials.

Change Rajesh’s Status: Once you’re logged in as the admin, you can change Rajesh’s status from waitlisted to enrolled


# Question 2

Preamble:  Well we never got to know the name of Agent X’s daughter, she goes by the name (fire) “Cracker” in the hacker community  :-). Now you ask what is on her plate?

The sysads of the ed-tech are not too dumb, they noticed unauthorized changes in their database, post investigation, they figured out the issues of authentication bypass and surprisingly quickly fixed it. Further they rolled back the database to a previous backup, and thus Rajesh is again in the waitlisted status!

Rajesh needs help again to move out of the waitlist. Rajesh has shared his username and password for this hacking and his credentials are "Rajesh:SecretPwd!" (special characters included.  (Well TBH Cracker could use her own account, but she is smart and  doesn’t want her account banned from further hacking or taken to task in case something leaks!)

Cracker found out that there is a search page in course details page which is vulnerable to SQL Injection attack. The task is to use UNION based SQL injection techniques to get hold of "users" table and exfiltrate "admin" user's credentials. Then  login as admin and change the waitlist status of Rajesh, specifically for CS-224 course.


Guidance:
You need to find  a way to login as "admin" user and convert Rajesh's waitlisted status.
To make things a bit easier for you, here is some additional info (which in the real world you wouldn’t normally have). 
The query used to run on backend application by PHP is: "SELECT sno,username,waitlisted,courseid FROM userdetails WHERE courseid = '$courseid' AND username = '$searchQuery' AND waitlisted = 0 "
The users table has following create table query when the table is created:

   	 "CREATE TABLE `users` (
   	   `sno` int(11) NOT NULL,
   	   `username` varchar(255) NOT NULL,
   	   `password` varchar(255) NOT NULL
   	 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
Steps to exfiltrate data using UNION based SQL injection technique
Step-1: Identify the number of columns fetched by the backend application.
Step-2: Identify the data type of the columns fetched
Step-3: Identify columns which are fetched and visible on your application. Ideally identify the columns in which your custom data is going to be visible to you when the application renders the html code.
Step-4: Identify table name, and column details for which we want to exfiltrate data from.
Exfiltrate the data (Either in a single column via concat function, or multiple columns).
References:
https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data
https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns
https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text
https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables
https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column



Submission Details:
- Once you convert Rajesh's waitlisted status, you will get flag, submit it in "/home/labDirectory/flag.txt". It will serve as proof of concept of your work.

# Question 3:   
Preamble: Cracker has soon enough realized that hacking is a cat and mouse game. After the endsem ended, the sysads did a thorough check and patched up all SQL Injection vulnerable points. And also change the password of "admin" user to more secure password.

Alas! But Cracker is not one to easily give up. She wants admin access to do all kinds of things, like get to know marks of all students!

She browsed the website and noticed a new feedback feature where students can comment on the course and it will be shown in the course details page itself. Is it possible this is vulnerable to XSS attack?

Cracker has Rajesh's credentials ("Rajesh:SecretPwd!") to cover her tracks!
In the first part, she will do some homework and then in the second part she will actually steal the session cookie of the admin, which can permit her to login as admin.

Part-1: Identifying Stored XSS Vulnerability

A simple way to check whether a page has XSS vulnerability is to pop an alert box. Let us try this first. Craft an XSS payload to pop an altert message when you visit the course details page of the course. Note you are still operating using Rajesh’s account. Once alert pops, the same course-details page will give you the flag as well.

Guidance: Here you can alert anything. But to get the flag DO-NOT use any spaces in between your tags and functions. This is the regex used to get the flag: "/<script>alert\(['\"]?.+['\"]?\);<\/script>/"

Submission Details:
- Once you have submitted the XSS payload according to the regex above, you will get flag, submit it in "/home/labDirectory/flag.txt" in "flagPart1" key. It will serve as proof of concept of your work.


Part-2: Stealing cookies using stored XSS vulnerability
Now that you have found a point where you can leverage the XSS vulnerability, let us use it to our advantage and steal the session cookie details of the admin user. The implications of this is, once you get the session cookie of a user, you can use it to login as that user without knowing any username/password (though we will not do this extra step of logging in)



Goal: Create an XSS payload which will get the session cookie of a currently logged in user (e.g. admin when he logs in to see the feedback), and send it to the attacker. 

GUIDANCE:
- Create payload following below document: https://pswalia2u.medium.com/exploiting-xss-stealing-cookies-csrf-2325ec03136e
- The payload you create should send the cookie to some service listening on a port at an IP address. In a real world, this would be some machine in the Internet(Of course attacker's). Here, we will use the lab container and your machine for simulating this scenario, so use your "eth0" or "wlan" network interface related IP address of your machine in the payload.
- To listen on some port on your machine you can use "netcat" using command: nc -lknvp <port>. This basically mimics a service running on the specified port on the machine where the command is run.
- Alternatively, you can host your own HTTP server(Since the request will come from XSS payload as an HTTP request) using Python:
       - For Python3: sudo python3 -m http.server <port>
       - For Python2: sudo python -m SimpleHTTPServer <port>
- You don’t have to model the admin login. Our backend will login as admin and visit the course detail pages every 1 minute. This should trigger a cookie sent to the port you are listening on if your payload was right!

Submission Details:
- Once you have received the admin session cookie details, the flag will be in URL encoded form. Use some online tool to URL decode the flag and submit it in "/home/labDirectory/flag.txt" in "adminFlag" key. It will serve as proof of concept of your work.
      ...combine these three problem statements into a mini project problem statement and write a detailed problem statement.
