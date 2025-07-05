from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/machines')
def machines():
    return render_template('machines.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html')

if __name__ == '__main__':
    app.run(debug=True)
