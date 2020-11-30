import flask
from flask import render_template, request, jsonify, redirect, url_for
from flask import flash
import os
app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
app.config["DEBUG"] = True 

items  = []
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', items = items, length = len(items), zip = zip, redirect = redirect)

@app.route('/', methods=['POST'])
def onAddPress():
    item = request.form['item']
    if len(item)==0:
    	flash('Empty field cannot be added!')
    	return redirect('http://127.0.0.1:5000/')
    else:
    	items.append(item)
    	return redirect(url_for('home'))

@app.route('/delete/', methods=['GET'])
def onDeletePress():
    deleteItem = dict(request.args)
    print(deleteItem)
    index = int(deleteItem.get('delete'))
    print(index)
    items.pop(index)
    return redirect(url_for('home'))

if __name__ == "__main__":
	app.run()