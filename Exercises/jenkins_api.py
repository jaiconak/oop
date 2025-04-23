import jenkins 

jenkinsUrl = 'http://3.227.255.7:8080/'
jenkinsUsername = 'devops'
jenkinsPassword = 'devops'

# Create an object that can log into jenkins server
server = jenkins.Jenkins(jenkinsUrl, username=jenkinsUsername, password=jenkinsPassword)
# print(f"""There are 
# {server.jobs_count()} Jobs in your Jenkins Server!""")

serverNum = server.jobs_count()

# for i in dir(server):
#     print(i)

# user = server.get_whoami()['fullName']

jobs = server.get_jobs()
# print(jobs)

for items in jobs:
    print ("********************************************************************************************")
    print(items)
