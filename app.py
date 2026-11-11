from flask import Flask, render_templat, request
app = Flask(__name__)
@app.route('/')
def register():
	return render_template('register.html)'

@app.route('/success', methods=['POST'])
def success():
	return render_template('success.html', data = request.form())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')