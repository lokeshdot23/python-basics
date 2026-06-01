#email automation
#uses simple mail transfer protocol
import random
import smtplib #simple mail transfer protocol
digits='0123456789'
OTP=''
for _ in range(6):
    OTP+=random.choice(digits)
    #mam example
    #OTP+=digits[math.floor(random.random()*10)]
msg=OTP+" is your otp"+"\nthis otp is generated using smtplib"
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("mogalapallilokesh@gmail.com","tkmx qpsq snni leti")
user="mogalapallilokesh@gmail.com"
email=input("enter the sender email")
s.sendmail(user,email,msg)
while True:
    a=input("please enter your otp")
    if a==OTP:
        print("otp is correct :)")
        break
    else:
        print("wrong otp : Try Again :(")
        
