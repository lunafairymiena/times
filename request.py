import urllib3, requests, json

iam_token = 'eyJraWQiOiIyMDIwMDgyMzE4MzIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMDhHSlIxIiwiaWQiOiJJQk1pZC01NTAwMDhHSlIxIiwicmVhbG1pZCI6IklCTWlkIiwiaWRlbnRpZmllciI6IjU1MDAwOEdKUjEiLCJnaXZlbl9uYW1lIjoiWW9pY2hpIiwiZmFtaWx5X25hbWUiOiJOYWthc2hpbWEiLCJuYW1lIjoiWW9pY2hpIE5ha2FzaGltYSIsImVtYWlsIjoibmFrYXNoaW1hM0BuZWMuY29tIiwic3ViIjoibmFrYXNoaW1hM0BuZWMuY29tIiwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiMGIyZDk2MTdkMWQ3NDY0ZGE4MTE3MDJkMjhkNGNiMmEifSwiaWF0IjoxNTk5NDY3OTI4LCJleHAiOjE1OTk0NzE1MjgsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTpwYXNzY29kZSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImJ4IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.SYExLaupDnKhGW7t24Evh330sGc8qhRTdEWxm-pfR6SYlUSrGse2GANeIts9c8kPBBsTPRikfgUyi3wqs_1uGeMSxxGLlZUXZ0O01L190r8w50X8nIIXi2Qgkf6aFHbIYh-9Fx0bQzm8rO9ParlyWXp_P60_qKnPG96WYVWM3I5cXpWFxPnELb1OoMPtwsA2gcj6c59Qfp8P7pXuJibcYVP4WpAbE_8wECx-kF3NGazxgLtmeMrd23JIAd91trwHNEU7zih1wMdw6jVjk5Om9HrXIXt7tNYjOOKJTT5YQVOswTBRgordaHIIEf1ReQFuzLoUSfE0JHRnEVeWywnEJQ'
ml_instance_id = 'db17d9b9-3c58-4984-b314-a01a20fa639c'
array_of_values_to_be_scored = 1
another_array_of_values_to_be_scored = 1

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["No.", "Place", "Date", "Time"], "values": [array_of_values_to_be_scored,another_array_of_values_to_be_scored]}]}
print("Scoring request")

response_scoring = requests.post('https://jp-tok.ml.cloud.ibm.com/v4/deployments/2e8dab1e-313a-4de5-89f6-a3b6e8aab5ce/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))