import requests

url = 'http://localhost:9696/predict'

customer = {
    'lead_source': 'organic_search',
    'industry': 'retail',
    'employment_status': 'employed',
    'location': 'south_america',
    'annual_income': 75000.0,
    'number_of_courses_viewed': 3,
    'interaction_count': 7,
    'lead_score': 0.75,
    'customerid': 'TestSubject001'
}
response = requests.post(url, json=customer)
#response = requests.post(url, json=customer).json()
#print(response)
print("Status code:", response.status_code)
print("Contenido devuelto:\n", response.text)


if response['churn'] == True:
    print('sending promo email to %s' % customer['customerid'])
else:
    print('not sending promo email to %s' % customer['customerid'])