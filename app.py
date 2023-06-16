from flask import Flask, request, render_template
from pymessenger.bot import Bot
import request as memeRequest

app = Flask(__name__)
ACCESS_TOKEN = 'EAABiqs9S67wBAEAMgey94mxI3hHKpOQqQWWsJsijwhzWBBxD1ZBXRUr6INcTveNgeOUfX3HGchigMK20cUHs1IPqtZCPeBDdl3d4hlLbsX8Y7vQYfMrFpRlsycXiabNXh1brzA6a3k9cgbZCnRes0HvAyiK5yKsroGHroUfLKykZB4eo65Le'
VERIFY_TOKEN = 'memebot2023'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def retrieve_messages():
	if(request.method == 'GET'):
		token = request.args.get("hub.verify_token")
		return verify_token(token)
	elif(request.method == 'POST'):
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					recipient_id = message['sender']['id']
				if message['message'].get('text'):
					req = memeRequest.Request(message['message'].get('text'))
					response = req.process()
					if(response.type == "text" or response.type == "error"):
						send_message(recipient_id, response.content)
					elif(response.type == "file"):
						send_file(recipient_id, response.content)


	return "Processed"

@app.route('/templates')
def getTemplates():
    return render_template('meme-bot-templates.html')

def verify_token(token):
	if token == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Verification token is invalid'

def send_message(recipient_id, response):
	bot.send_text_message(recipient_id, response)
	return "success"

def send_file(recipient_id, response):
	bot.send_image_url(recipient_id, response)
	return "success"