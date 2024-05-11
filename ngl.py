import requests

def sendSpam(user, message):
	url = 'https://ngl.link/api/submit'
	payload = {'username': user, 'question': message, 'deviceId': ""}
	headers = {
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
	} 
	response = requests.post(url, json=payload, headers=headers) 
	return response.status_code
def Spam(link,message,amount):
	x = link.split("/")
	user = x[3]

	status_code = sendSpam(user, message)
	y = "success"
	n = "error"
	text = f"\033[93m[ NGL ] \033[91m[\033[97m{y if status_code == 200 else n}\033[91m]: \033[94mMessage sent to \033[95m{user}\033[0m"
	return f"{y if status_code == 200 else n}"