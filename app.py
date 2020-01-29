from flask import Flask, render_template
app = Flask(__name__)

kt_list = [2902003030, 3029032020]

def getSum(n): 
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum

@app.route('/')
def index():
	return render_template("index.html")
	#return render_template('kennitala.html', kt=kt_list)
			   
@app.route('/kennitala')
def kennitolur():
	return render_template('kennitala.html', kt=kt_list)

@app.route('/kennitala/<int:kt>')
def dversuma(kt):
	kt_sum = getSum(kt)
	return render_template('dversuma.html', kt_sum=kt_sum, kt=kt,)
	
@app.route('/postur')
def sida2():
	return render_template('postur.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)