# Todo have to get all the jenkins jobs
# Inventory them into a CSV file

import jenkins
import csv


user = 'devops'
pw = 'devops'
url = 'http://44.199.255.163:8080/'

def getAlljobJenkins(url,user,pw) :
    server = jenkins.Jenkins(url, user, pw)
    listJobs = server.get_all_jobs()
    jenkinsList = []
    for i in listJobs:
        jobName = i.get('name')
        jobUrl = i.get('url')
        jobStatus = i.get('color')
        jenkinsList.append([jobName,jobUrl,jobStatus])
    return jenkinsList

def writeToCsv(filename,jenkinsList):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        value = ['name','url', 'color']
        writer.writerow(value)
        for i in jenkinsList:
            writer.writerow(i)

def main():
    jobs = getAlljobJenkins('http://44.199.255.163:8080/','devops','devops')
    writeToCsv('jaicoTesting.csv',jobs)
    print("File imported successfully!")

if __name__ == "___main__":
    main ()

