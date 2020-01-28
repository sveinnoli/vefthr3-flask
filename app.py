from flask import Flask, render_template
app = Flask(__name__)

kt = [2902003030, 3029032020]
kt_sum = [sum(int(digit) for digit in str(number)) for number in kt]

@app.route('/')
def index():
	return '<a href="/kennitala">Kennitala</a> \n'  \
		   '<a href="/postur">Póstur</a>' 
			   
@app.route('/kennitala')
def kennitala():
	return render_template('kennitala.html', kt=kt)

@app.route('/kennitala/<int:kt_current>')
def dversuma(kt_current):
	return render_template('dversuma.html', kt_sum=kt_sum, kt=kt_current,)
	
@app.route('/postur')
def sida2():
	return render_template('postur.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)