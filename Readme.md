*API* (Application Programming Interface) is a software intermediary that create an avenue for two applications to communicate with each other (which includes sending and receiving data). 
In a simpler term, imagine entering into a restaurant, first of all you will have to glance through the menu to make a choice of what to order. Whatever food you ordered will be made in the kitchen. There must be a connection point between you and the kitchen, so that your order can be delivered. The connection point can be made to understand what your order is and knows appropriately where to get it. That’s where the attendant or API comes in. The attendant is the linking – or API – that takes your order and tells the kitchen what to do to get your order served. Then the attendant delivers the response back to you; in this case, it is the food you ordered.

**API are very power and they can give you unlimited power as regard the number of functionalities you want to enable on your platform**

*Twilio is one of such API'S. In this tuturioal I will walk you step by step on how to create a Python texting leveraging on Twilio API*

> Requirements 

* Python – you can install [PYTHON](python.org/download "Python Official Website"). If you’re using MAC, you should probably have python preinstalled. Ensure you install latest python although both Python 2 and Python 3 are supported by Twilio’s Python server-side SDK supports 
* Twilio helper library- open your terminal to install using ``pip install twilio``.
With the free twilio account you can only text numbers you have verified on Twilio platform.

### Step 1:- Create a Twillio account 
Goto [TWILIO](https://twilio.com "Twilio Website Page") to sign up for an account. Enter the required details into each of the box as shown below;


![signup form.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613183170000/xAgrmZ6N9.jpeg)

Click on Start your free Account, you will be required to solve a puzzle, after which a verification mail will be sent to your email box.

### Step 2 :- . Verify your phone number

When you click the link for email verification sent to your email inbox, you will be redirected to a landing page to verify your phone number. Messages can only be sent to verified phone number on a trial account.
Enter the verification code sent to your phone number after clicking the verify button to complete phone number verification.

![number verification.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613183433506/gJAWzlM-D.jpeg)

Verification successful? Congratulations, personalize your account setting by filling up the following field under the congratulation message as shown below;


![verificationsuccesfull.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613184245937/wEjYTbjHC.jpeg)



![Undersuccesfullmessage.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613184252925/1zK8zy5XU.jpeg)



### Step 3:-	Get Your Twilio Phone number
On getting to project dashboard in the [Twilio Console](https://www.twilio.com/console - "Twillio Dashboard") click on ``Get Trial Number``, a dialog box will pop up with a generated Twillio number for you, click on choose number as shown below;


![trialnumber.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613184549015/o64YC63qY.jpeg)


![twillionumber.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613184827125/9GOKWbZyq.jpeg)

### Step 4:- Get Twilio Credentials
On the dashboard, Get Account SID and Auth Token, both will be need in your code.


![authandSID.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1613184912228/Nq1I5QRGF.jpeg)

### Step 5:- Pip Install Twilio
Open terminal (Command Line Interface – CLI), run ```pip install twilio``` command to install Twillio Library;

``` 
pip install twilio

``` 

### Step 6:- Open code editor(VS Code, Pycharm or IDLE) and enter the follows line of code and replace the required placeholders as explained above.

``` python
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="God bless Africa!.",
                     from_='TWILIO_PHONE_NUMBER',
                     to='VERIFIED_PHONE_NUMBER'

                 )

print(message.sid)

```
 > Replace all the credentials placeholder

Replace the placeholders for account_sid and auth_token with your personal Twilio credentials you copied under step 4. You can also Go to [Twilio](https://www.twilio.com/console "Twilio Console") and log in to get your Account SID and Auth Token.

> Replace the ```TWILIO_PHONE_NUMBER```  with your twilio number gotten in Step 3.

> Replace the ```VERIFIED_PHONE_NUMBER``` (Replace with your phone number verified in step 4). A trial account can only send messages to verified phone numbers. Although, it can be any mobile number that has been verified and that can receive SMS. But, Its advised you insert your personal number for a test and see the magic happens.

> Access [Twilio Console's Verified Caller IDs](https://www.twilio.com/console/phone-numbers/verified "Verify Phone Numbers")   to verify phone numbers. Also, the Short description “Sent from a twilio trial account” included in your outgoing message automatically will be removed after you Upgrade your Twilio account.

*You can choose to run the program inside the code editor. Alternatively, you can run it through the terminal (Command Prompt) through step 9 below;*

### Step 6:- Run the code through terminal

Open the terminal (Command prompt), locate the directory where your code 
was saved and run 
```
python send_sms.py

``` 
In this case, my code file named send_sms.py was saved in desktop directory.

Conclusion:- 
To build a sms app with python using Twillio REST API, two things are most required to make this process successful, first is a twilio phone number that will be gotten after signing up on [TWILIO](https://www.twilio.com), secondly, verified phone number (to be the receipient).