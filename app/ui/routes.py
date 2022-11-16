from flask import Blueprint, render_template, request, redirect
from app.models import db, Player
import pandas as pd


ui_bp = Blueprint(
  'ui_bp', __name__,
  template_folder='templates',
  static_folder='static'
)

# App Home Page
@ui_bp.route('/')
def home():
    return render_template("home.html")

# Players list page and players_all API route

@ui_bp.route('/players')
def list_players():
   players = Player.query
   return render_template('players.html', players=players)

@ui_bp.route('/api/players')
def players_all():
    return {'data': [player.to_dict() for player in Player.query]}

# Add a single player from the new player form

@ui_bp.route('/players/add_player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        player = Player(name=name, height=height, weight=weight)
        db.session.add(player)
        db.session.commit()
    return render_template('new_player.html')

# Import multiple players

@ui_bp.route('/players/import')
def import_players():
   title = 'Import Datasets'
   return render_template('upload_players.html', title=title)

@ui_bp.route('/players/import/upload_file', methods=['POST'])
def upload_file():
    # get the uploaded file
    uploaded_file = request.files['file']
    # if not empty
    if uploaded_file.filename != '':
        # set the file path
        # file_path = os.path.join(config.UPLOAD_FOLDER, uploaded_file.filename)
        # save the file
        uploaded_file.save(uploaded_file.filename)
        add_players(uploaded_file.filename)

    return redirect('/players/import')

def add_players(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Player object for each row (row key names must match CSV header row)
    for i, row in csv_data.iterrows():
       player = Player(
            name=row['name'],
            height=row['height'],
            weight=row['weight']
       )

       # Insert current player into db

    db.session.add(player)
    db.session.commit()