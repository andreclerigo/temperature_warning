# coding=utf-8
import os
import smtplib
from dotenv import load_dotenv
from os.path import join, dirname
from email.mime.text import MIMEText
from time import time, sleep

# Returns the core Temperature
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

# Repeat every X minutes
def loopTemperatureAlert():
	#Setting up enviorment variables
	dotenv_path = join(dirname(__file__),'.env')
	load_dotenv(dotenv_path)
	EMAIL = os.environ.get("EMAIL")
	PASSWORD = os.environ.get("PASSWORD")

	while True:
		sleep(600 - time() % 600)
		high = 70

		# Conver the value to a float number
		temp = float(getCPUtemperature())

		# Check if the temperature is above 'high'
		if (temp >= high):
			subject = "Critical warning! The temperature is: {} ".format(temp)
			body = "Critical warning! The actual temperature is: {} \n".format(temp)

			# Enter your smtp Server-Connection
			server = smtplib.SMTP('smtp.gmail.com', 587) # if your using gmail: smtp.gmail.com
			server.ehlo()
			server.starttls()
			server.ehlo
			# Login
			server.login(EMAIL, PASSWORD)
		
			msg = MIMEText(body)
			msg['Subject'] = subject
			msg['From'] = EMAIL
			msg['To'] = EMAIL

			# Finally send the mail
			server.sendmail(EMAIL, EMAIL, msg.as_string())
			server.quit()

def main():
	loopTemperatureAlert()

main()
