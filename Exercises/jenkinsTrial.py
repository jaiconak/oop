import jenkins 
import csv
import os

print("Writing to:", os.getcwd())

def listJenkinsJob(url,user,pw):
    server = jenkins.Jenkins(url, user, pw)
    jobList = server.get_all_jobs()
    jenkinsJobs = []

    for counter in jobList:
        jobName = counter.get('name')
        jobUrl = counter.get('url')
        jobStatus = counter.get('color')
        jenkinsJobs.append([jobName, jobUrl,jobStatus])

    return jenkinsJobs

def csvCreate(file, jenkinsJobs): 
    with open(file, "w", newline="") as file:
        writer = csv.writer(file)
        value = ['Name', 'URL', 'Color']
        writer.writerow(value)
        for i in jenkinsJobs:
            writer.writerow(i)

def main():
    jobJenkinsList = listJenkinsJob('http://44.204.190.236:8080/', 'devops', 'devops')
    csvCreate('jenkinsJobsTesting.csv', jobJenkinsList)
    print("File imported successfully!")


if __name__ == "___main__":
    main ()



