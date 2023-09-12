from flask import Flask, render_template
from Data_store import FileHandler

data_handler = FileHandler("history.txt", "balance.txt", "inventory.json")

app = Flask(__name__)


@app.route('/')
def index():
    account_balance = data_handler.account_balance
    inventory = data_handler.inventory

    return render_template('index.html', account_balance=account_balance, inventory=inventory)


@app.route('/historia/')
def history():
    # Tutaj możesz wstawić kod do pobierania historii operacji
    return render_template('history.html')


if __name__ == '__main__':
    app.run()
