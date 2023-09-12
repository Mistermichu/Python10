from flask import Flask, render_template


@app.route('/')
def index():
    # Tutaj możesz wstawić kod do pobierania stanu konta, magazynu itp.
    return render_template('index.html')


@app.route('/historia/')
def history():
    # Tutaj możesz wstawić kod do pobierania historii operacji
    return render_template('history.html')


if __name__ == '__main__':
    app.run()
