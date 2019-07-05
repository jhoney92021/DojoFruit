from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def store():
    return render_template('index.html')

@app.route('/checkout', methods=[ 'GET', 'POST'])
def checkout():
    count=0
    count += int(request.form['Raspberry'])+int(request.form['Strawberry'])+int(request.form['Apple'])
    return render_template(
        'checkout.html',
        amount= count,
        name=request.form['name'],
        student=request.form['student'], 
        Strawberry=request.form['Strawberry'],
        Raspberry=request.form['Raspberry'],
        Apple=request.form['Apple']
      )

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')


if __name__=='__main__':
    app.run(debug=True)