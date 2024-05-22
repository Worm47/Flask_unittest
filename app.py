from flask import Flask, render_template, request

app = Flask(__name__)

exchange_rates = {
    'usd_to_rub': 91.63,
    'eur_to_rub': 98.86,
    'jpy_to_rub': 0.59,
    'rub_to_usd': 1 / 91.63,
    'rub_to_eur': 1 / 98.86,
    'rub_to_jpy': 1 / 0.59
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    if from_currency == to_currency:
        converted_amount = amount
    elif from_currency == 'rub':
        converted_amount = amount * exchange_rates['rub_to_' + to_currency]
    elif to_currency == 'rub':
        converted_amount = amount * exchange_rates[from_currency + '_to_rub']
    else:
        converted_amount = amount * exchange_rates[from_currency + '_to_rub'] * exchange_rates['rub_to_' + to_currency]

    converted_amount = abs(round(converted_amount, 4))
    return render_template('index.html', converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)

