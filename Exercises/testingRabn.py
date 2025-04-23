import jenkins 
import csv
import os

print("Writing to:", os.getcwd())

user = 'devops'
pw = 'devops'
url = 'http://44.204.190.236:8080/'
server = jenkins.Jenkins(url, user, pw)
jobList = server.get_all_jobs()
# print (jobList)

jenkinsJobs = []


for counter in jobList:
    jobName = counter.get('name')
    jobUrl = counter.get('url')
    jobStatus = counter.get('color')
    rab = jenkinsJobs.append([jobName, jobUrl,jobStatus])
    print("************************************************************************************************************************************************************")
    print(counter)