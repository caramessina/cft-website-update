from CFT import app

if __name__ == '__main__':  #to actually run the app
    app.secret_key='secret123'
    app.run(debug=True)
