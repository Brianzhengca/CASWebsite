from flask import Flask
from flask import render_template, redirect
import json
import pandas as pd
import random

club_excel = pd.read_excel('test.xlsx')


app = Flask(__name__, template_folder="templates", static_folder="static")

info = json.load(open("club_info.json"))
print(info)

#these functions do not work yet
@app.route('/test')
def info_box_test():
  return make_club_info_box("science")

#these functions do not work yet
def make_club_info_box(id):
    '''
    "science_club": {
        "name": "Science Club",
        "president: "Allison Park",
        "date": "Fridays",
        "time": "3:00-400 pm",
        "location": "1708",
        "description": "We do things.",
        "extended_description": "Order art commissions to help support our friends Liv and Webb, who are a disabled Black & indigenous (Taíno) couple struggling to afford medications, food, transportation, and rent. More info You can order a commission by replying to the email you received this link from, or by filling out thi...",
        "email": "scienceclubinterlake@gmail.com",
        "link": "https://discord.gg/3g5TmngyBE",
        "thumbnail": "science_club.png",
        "walk_in": true
        "sign_up_link": null
    }
    '''
    name = info[id]["name"]
    president = info[id]["president"]
    date = info[id]["date"]
    time = info[id]["time"]
    location = info[id]["location"]
    description = info[id]["description"]
    extended_description = info[id]["extended_description"]
    email = info[id]["email"]
    link = info[id]["link"]
    thumbnail = info[id]["thumbnail"]
    walk_in = info[id]["walk_in"]

    walk_in_text = ""
    sign_up_button = ""
    if walk_in:
      walk_in_text = "No sign ups required, just walk in"
    else:
      walk_in_text = "Please sign up using the button below"
      sign_up_button

    return f'''
        <div class="col">
          <div class="card shadow-sm">
            <img class="thumbnail" src="static/{thumbnail}" height=225/>
           
            <div class="card-body">
              <p class="card-header"><b>{name}</b></p>
              <p class="card-text">{description}</p>
              <a class="card-details" href="mailto:{email}" rel="noopener noreferrer">📧{email}</a>
              <p class="card-details">📍 {location} 🕐{date} {time}</p>
              <p class="card-details">{walk_in_text}</p>
              <p class="card-details">
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="window.location.href = 'clubpage.html';">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="window.open('{link}')">Discord</button>
                </div>
              </div>
            </div>
          </div>
        </div>'''
    
@app.route("/")
def index():
  #actually make an index page sometime
  return redirect("/clubs")


#we eventually want it to sort on the client side, not ours
@app.route('/clubs')
def clubs_page():
    #alphabet

    print(type(render_template('index.html')))

    club_boxes = ""
    for club_id in sorted(info.keys()):
      club_boxes += make_club_info_box(club_id)
    
    return render_template('index.html', club_boxes=club_boxes)

@app.route('/clubs-random')
def random_clubs_page():
    #randomize
    print(type(render_template('index.html')))

    club_boxes = ""
    keys = list(info.keys())
    random.shuffle(keys)

    for club_id in keys:
      club_boxes += make_club_info_box(club_id)
    
    return render_template('index.html', club_boxes=club_boxes)





@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/clubs/<club>')
def clubgape(club):
  return club

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
