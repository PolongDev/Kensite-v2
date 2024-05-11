from flask import Flask, jsonify, request, render_template
import requests
import time
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#----------------------------#
#________[ CONFIG ]__________#
from ngl import Spam

#_________[ PAGES ]__________#
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/gpt')
def gpt():
	return render_template('gpt.html')
@app.route('/imgbb')
def imgbb():
	xxA = "https://api.imgbb.com/1/upload?key=35cf9f5cc0b00be80e423ddeead3d8d6"
	return render_template('imgbb.html',key=xxA)
@app.route('/ngl')
def ngl():
	return render_template('ngl.html',ngl="/api/ngl")
@app.route('/fbDl')
def fbDl():
  return render_template('/fbDl.html',api="https://hoanghao.me/api/facebook/download")
#________[ FUNCTIONS]________#



#__________[ APIs ]__________#
@app.route('/api/gpt',methods=['GET'])
def api_gpt():
	query = request.args.get('query')
	uid = request.args.get('uid')
	gpt_res = requests.get(f"https://deku-rest-api.replit.app/gpt4?prompt={query}&uid={uid}")
	return gpt_res.json()
@app.route('/api/ngl',methods=['POST'])
def api_ngl():
	j = request.json
	link = j.get('link')
	message = j.get('message')
	amount = j.get('amount')
	time.sleep(1.5)
	if not link or not message or not amount:
		return jsonify({"msg": 'Lagyan mo ng link,message oh amount BOBO kaba?'}),400
	res = Spam(link, message, amount)
	return jsonify({
		"msg": res
	}),200
#----------------------------#
if __name__ == '__main__':
	app.run(port=80)
