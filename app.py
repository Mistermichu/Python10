from flask import Flask, render_template, request, redirect, url_for
from Data_store import FileHandler, FileWriter
from functions import menu, balance, account_balance_note, sell, buy, list_overview, inventory_overview, history_overview, inventory_correction
from Manager import Manager

data_handler = FileHandler("history.txt", "balance.txt", "inventory.json")
save_data = FileWriter(
    "history.txt", "balance.txt", "inventory.json")
manager = Manager(data_handler.history,
                  data_handler.account_balance, data_handler.inventory)

app = Flask(__name__)


@app.route('/')
def index():
    account_balance = manager.account_balance
    inventory = manager.inventory

    return render_template('index.html', account_balance=account_balance, inventory=inventory)


@app.route('/buy', methods=['POST'])
def process_buy():
    purchase_product = request.form.get('purchase_product')
    purchase_price = float(request.form.get('purchase_price'))
    purchase_quantity = int(request.form.get('purchase_quantity'))
    manager.account_balance -= buy(manager.account_balance,
                                   manager.history, manager.inventory, purchase_product, purchase_price, purchase_quantity)
    save_data.save_history(manager.history)
    save_data.save_balance(manager.account_balance)
    save_data.save_inventory(manager.inventory)

    return render_template('index.html', account_balance=manager.account_balance, inventory=manager.inventory)


@app.route('/historia/')
def history():
    # Tutaj możesz wstawić kod do pobierania historii operacji
    return render_template('history.html')


if __name__ == '__main__':
    app.run()
