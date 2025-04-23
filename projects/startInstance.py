from awsCodeBoto3 import listInstances, startInstance

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
startInstance(listInstances(dev_filter))