# from flask import Flask, request, jsonify
# import pandas as pd
# import pickle

# # pipe = pickle.load(open('/home/neeraj/pandas-demo/iplDatasets/pipe.pkl'),'rb')

# with open('/home/neeraj/pandas-demo/iplDatasets/pipe.pkl', 'rb') as f:
#     pipe = pickle.load(f)
# app = Flask(__name__)

# # Sample Python function to be called
# def probablity(pipe,lst):
#     df = pd.DataFrame([lst],columns=['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left',
#            'wickets_left', 'total_runs_x', 'crr', 'rrr'])
#     out=pipe.predict(df)
#     return pipe.predict_proba(df)
# # print(result(pipe,lst))

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     lst=[data['batting_team'],
#         data['bowling_team'],
#         data['current_score'],
#         data['wickets'],
#         data['overs'],
#         data['target'],
#         data['city']
#         # data['runs_left'],
#         # data['balls_left'],
#         # data['wickets_left'],
#         # data['total_runs_x'],
#         # data['crr'],
#         # data['rrr']
#         ]
#     runs_left = data['target']-data['score']
#     balls_left = 120-(data['overs']*6)   
#     wickets_left = 10-data['wickets']
#     crr = data['current_score']/data['overs']
#     rrr = (runs_left*6)/balls_left
#     lst2 = [data['batting_team'], data['bowling_team'], data['city'], runs_left, balls_left,
#            wickets_left, data['target'], crr, rrr]
#     result = probablity(pipe,lst2)
#     return jsonify({'result': result})

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, render_template_string,render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)


# Function to be called with form inputs
def probablity(pipe,lst):
    df = pd.DataFrame([lst],columns=['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left',
           'wickets_left', 'total_runs_x', 'crr', 'rrr'])
    # out=pipe.predict(df)
    ans = pipe.predict_proba(df)
    loss = ans[0][0]
    win = ans[0][1]
    print(ans)
    dic = {'team1':'Sunrisers Hyderabad','team2':'Mumbai Indians','team3':'Royal Challengers Bangalore','team4':'Kolkata Knight Riders','team5':'Kings XI Punjab','team6':'Chennai Super Kings','team7':'Delhi Capitals','team8':'Rajasthan Royals'}
    # return dic[lst[0]] + ': ' + str(np.round(win*100,2))+"%" 
    return f"{dic[lst[0]]}: {np.round(win*100,2)}% \n\n{dic[lst[1]]}: {np.round(loss*100,2)}%"

@app.route('/')
def index():
    return render_template_string(open('templates/ipl.html').read())

@app.route('/submit', methods=['GET','POST'])
def submit():
    # inputs = [request.form['battingTeam'], request.form['bowlingTeam'], request.form['currentScore'],request.form['wickets'],request.form['oversCompleted'],request.form['target'],request.form['venue']]
    runs_left = int(request.form['target'])-int(request.form['currentScore'])
    balls_left = 120-(int(request.form['oversCompleted'])*6)   
    wickets_left = 10-int(request.form['wickets'])
    crr = int(request.form['currentScore'])/int(request.form['oversCompleted'])
    rrr = (runs_left*6)/balls_left
    bat = request.form['battingTeam']
    ball = request.form['bowlingTeam']
    lst=[bat, ball, request.form['venue'], runs_left, balls_left,
           wickets_left, int(request.form['target']), crr, rrr]
    result = probablity(pipe,lst)
    return render_template('result.html', result=result)
   
if __name__ == '__main__':
    app.run(debug=True)
