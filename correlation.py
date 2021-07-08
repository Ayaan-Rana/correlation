import plotly.express as px
import csv
import numpy as np



def getDataSource(data_path):
    days_present=[]
    student_marks=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row['Days Present']))
            student_marks.append(float(row['Marks In Percentage']))
    
    return {'x' : days_present, 'y' : student_marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('Correlation between number of days present and student marks :-   /n--->',correlation[0,1])

def setup():
    data_path = 'data.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()