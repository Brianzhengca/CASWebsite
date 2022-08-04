from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

#... so on and so forth depending on needs
#error catching below

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(500)
def internal_server_error(error):
    print("_____________________________________internal server error below_____________________________________")
    return render_template('500.html'), 500

if __name__ == '__main__':
   app.run(debug=True)
