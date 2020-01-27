from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<a href="sida1>lidura</a>' \
		   '<a href="/sida2">lidurb</a>'
@app.route('/sida1')
def kennitala():
	kt = [2902003030, 2902004040]
	
		sum = 0
		for x in kt:
			while (x != 0): 
				sum = sum + int(x % 10) 
				x = int(n/10) 
			return sum
	
	return render_template('kennitala.html')

@app.route('/sida2')
def sida2():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)