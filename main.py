from flask import Flask
from flask import render_template
import json

app = Flask(__name__, template_folder="templates", static_folder="static")

info = json.load(open("club_info.json"))

#these functions do not work yet
@app.route('/test')
def info_box_test():
  return make_club_info_box("science_club")

#these functions do not work yet
def make_club_info_box(id):
    '''
    "science_club": {
        "name": "Science Club",
        "date": "Fridays",
        "time": "3:00-400 pm",
        "room": "1708",
        "description": "We do things.",
        "extended_description": "omg weird crap aaa pvp simp house",
        "email": "scienceclubinterlake@gmail.com",
        "link": "https://discord.gg/3g5TmngyBE",
        "thumbnail": "science_club.png"
    }
    '''
    name = info[id]["name"]
    date = info[id]["date"]
    time = info[id]["time"]
    room = info[id]["room"]
    description = info[id]["description"]
    extended_description = info[id]["extended_description"]
    email = info[id]["email"]
    link = info[id]["link"]
    thumbnail = info[id]["thumbnail"]

    return f'''
        <div class="col">
          <div class="card shadow-sm">
            <img class="thumbnail" src="static/{thumbnail}" height=225/>
           
            <div class="card-body">
              <p class="card-header"><b>{name}</b></p>
              <p class="card-text">{description}</p>
              <a class="card-details" href="mailto:{email}" rel="noopener noreferrer">📧{email}</a>
              <p class="card-details">📍 {room} 🕐{date} {time}</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="window.location.href = 'clubpage.html';">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="window.open('{link}')">Discord</button>
                </div>
                <small class="text-muted">9 mins</small>
              </div>
            </div>
          </div>
        </div>'''
    


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
