from flask import Flask, render_template
app = Flask(__name__)
kt_list = [2902003030, 3029032020]
frettir = [[0, "Mbl.is oft notað í forritum sem dæmi!", "Það er nyfundið að mbl.is er meiri oftar notað í sem sýnidæmi í forritun en notað til að lesa fréttir", "höfundur@email.is", "\static\images\mbl.png"],
           [1, "Eldur kviknaði í skógi utan af reykjavik", "Það var risa eldur um daginn sem kviknaði í skóg utan reykjavik, það var fundið út að strumpar voru á háaum dópum þegar eldurinn kviknaði", "strumpur@email.is", "/static/images/forestfire.jpg"]]
def getSum(n): 
    sum = 0
    while (n != 0): 
        sum = sum + int(n % 10) 
        n = int(n/10) 
    return sum

@app.route('/')
def index():
	return render_template("frettir.html")
			   
@app.route('/kennitala')
def kennitolur():
	return render_template('kennitala.html', kt=kt_list)

@app.route('/kennitala/<int:kt>')
def dversuma(kt):
	kt_sum = getSum(kt)
	return render_template('dversuma.html', kt_sum=kt_sum, kt=kt,)
	
#Siða fyrir allar frettirnar
@app.route('/frettir')
def postur():
	return render_template('frettir.html', frettir=frettir)

#Siða fyrir Grein
@app.route('/frettir/<int:id>')
def frett(id):
    frett=frettir[id]
    return render_template('post.html', frett=frett)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)