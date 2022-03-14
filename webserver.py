from threading import Thread
from flask import Flask, request, jsonify
import bot


app = Flask('')
 
@app.route('/')
def home():
  return "server"


@app.route('/login', methods=['GET', 'POST'])
def login():
  userid = request.args.get('userid')
  token = request.args.get('token')

  text = "Принято! Теперь вы можете закрыть вкладку"
  if userid == None or token == None:
    text = "Вставь в консоль, и не балуйся"
  else:
    bot.add_token_c(userid, token)
  return text, 200



def run():
  app.run(host='0.0.0.0',port=8080)
  # app.run(host='bot.discordself.xyz',port=8080)
  
  
 
def keep_alive():
  t = Thread(target=run)
  t.start()