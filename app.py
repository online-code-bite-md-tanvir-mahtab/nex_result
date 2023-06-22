import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from joblib import load
from sklearn.model_selection import train_test_split
import random
import streamlit as st




def main(score,value,df,yf):
  row,col = df[df['next_result'] != yf].shape
  print(row)
  correct_prediction = (row/int(len(df))) * 100
  st.title('Upcoming result:')
  st.write(f'Spin Result: {value}')
  st.write(f'Confidence: {score * 100} %')
  st.write(f'Percentage Of correct prediction: {correct_prediction} %')
  st.title(f'The updated Data out of 100 ,  data were predicted is {row}')
  df['result'] = yf
  st.table(df[df['next_result'] != yf])



# starting to collect the data from the api
params = {
    'filter': '',
    'sort_by': '',
    'sort_desc': 'false',
    'page_num': '1',
    'per_page': '100',
    'period': '72hours'
}
head = {'Authorization': 'Bearer 35423482-f852-453c-97a4-4f5763f4796f'}
response = requests.get(url='https://api.tracksino.com/crazytime_history',params=params,headers=head)
data = response.json()['data']

# preprocessing the data
df = pd.DataFrame()

rc = []
wh =[]
res = []
sm = []
tw = []
tp = []
vu = []
sl = []
mul = []

for i in range(len(data)):
  round_code = data[i]['round_code']
  when = data[i]['when']
  result = data[i]['result']
  slot_multiplier = data[i]['slot_multiplier']
  try:
    multiplier = data[i]['multiplier']
  except: 
    multiplier = 1
  total_winners = data[i]['total_winners']
  total_payout = data[i]['total_payout']
  video_uid = data[i]['video_uid']
  slot_result = data[i]['slot_result']
  rc.append(round_code)
  wh.append(when)
  res.append(result)
  sm.append(slot_multiplier)
  tw.append(total_winners)
  tp.append(total_payout)
  vu.append(video_uid)
  sl.append(slot_result)
  mul.append(multiplier)


df = pd.DataFrame(
    {
        'round_code': rc,
        'when': wh,
        'result': res,
        'slot_result': sl,
        'slot_multiplier': sm,
        'multiplier':mul,
        'total_winners': tw,
        'total_payout': tp,
        'video_uid': vu
  }
)




data = df
# print(data)
event_list = [1.0, 2.0, 5.0, 10.0, 100.0, 200.0, 300.0, 400.0]
probabilities = [0.3888, 0.2407, 0.1296, 0.074, 0.074, 0.037, 0.037, 0.0185]


model = load('new_my_model.jblib')
result = model.predict(data[['when', 'slot_result', 'slot_multiplier','multiplier']])
score = accuracy_score(data['result'],result)
data['next_result'] = result
n_data = data[['total_payout','next_result']]
value = n_data['next_result'][0]
y_data = data['result']


if __name__ == '__main__':
    main(score,value,n_data,y_data)