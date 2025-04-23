from awsCodeBoto3 import listInstances, stopInstance

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
stopInstance(listInstances(dev_filter))