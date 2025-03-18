from flask import Flask, jsonify, request, render_template;
import requests

app = Flask(__name__)

@app.route('/')
def route_function():
    response = requests.get('http://127.0.0.1:5000/teamsname')
    teams = response.json()['name']
    return render_template('homepage.html',teams=sorted(teams))

@app.route('/teamvsteam')
def teamvsteam():
    team1=request.args.get('team1')
    team2 = request.args.get('team2')
    response2 = requests.get(f'http://127.0.0.1:5000/get_teams_record?team1={team1}&team2={team2}')
    response2=response2.json()

    response = requests.get('http://127.0.0.1:5000/teamsname')
    teams = response.json()['name']
    # print(response2.json())
    return render_template('homepage.html',result=response2,teams=sorted(teams))

@app.route('/batsman-details')
def get_batsman_details():
    a= requests.get('http://127.0.0.1:5000/playername')
    players = a.json()['players']
    return render_template('batsmandetail.html',players=sorted(players))

@app.route('/batsman-analysis')
def get_batsman_analysis():
    player_name=request.args.get('player')
    response3 = requests.get(f'http://127.0.0.1:5000/api/batsman_record?bats_name={player_name}')
    # print(response3.json()[player_name])
    response3 = response3.json()
    return response3
    # return render_template('batsmandetail.html', result=response3)

app.run(debug=True,port=7000)