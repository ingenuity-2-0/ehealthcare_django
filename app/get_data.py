from bs4 import BeautifulSoup
import requests
from doctor.models import Specialist, Doctor
from hospital.models import Hospital
from symptoms.models import Symptoms
import json


def data_for_auto_suggestion():
    doctors = Doctor.objects.all()
    doctor_list = []
    for x in doctors:
        doctor_list.append(x.name)
    specialists = Specialist.objects.all()
    for x in specialists:
        doctor_list.append(x.name)
    hospitals = Hospital.objects.all()
    hospital_list = []
    for x in hospitals:
        hospital_list.append(x.name)
    symptoms = Symptoms.objects.all()
    symptom_list = []
    for x in symptoms:
        symptom_list.append(x.symptom)
    with open('./static/assets/dataAPI.json', 'r') as json_file:
        file = json.load(json_file)
        json_file.close()
    file['diseases'] = symptom_list
    file['doctorSpe'] = doctor_list
    file['hospitals'] = hospital_list
    # print(file)
    with open('./static/assets/dataAPI.json', 'w') as json_file:
        json_object = json.dumps(file)
        json_file.write(json_object)
        json_file.close()
    # with open('./data/dataAPI.json', 'w') as json_file:
    # print(doctor_list)
    # print(hospital_list)
    # print(symptom_list)


def covid19_last24():
    latest24 = {}
    try:
        url = 'http://103.247.238.92/webportal/pages/covid19.php'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        latest = soup.find_all(class_='callout')
        for x in latest:
            number = x.find(class_="info-box-number")
            number1 = x.find(class_="last_24_hour_body")
            temp1 = str(number1.text.strip())
            temp1 = temp1.replace(' ', '_')
            temp2 = str(number.text.strip())
            latest24.update({temp1: temp2})
        # print(latest24)
    except:
        latest24 = {
            'Lab_Test': 0,
            'Confirmed': 0,
            'Recovered': 0,
            'Death': 0
        }
    return latest24


def covid19_api():
    try:
        data = requests.get('https://disease.sh/v3/covid-19/all')
        d = data.json()
        infected = d['cases']
        deaths = d['deaths']
        recovered = d['recovered']
        tests = d['tests']
        dict1 = {'infected': infected,
                 'deaths': deaths,
                 'recovered': recovered,
                 'tests': tests}
    except:
        dict1 = {'infected': 0,
                 'deaths': 0,
                 'recovered': 0,
                 'tests': 0}
    return dict1
