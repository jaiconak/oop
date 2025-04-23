# System inventory
import os
import platform
import psutil

info = []

def inventory():
    numCpu = os.cpu_count()
    osVersion = platform.version()
    pythonVersion = platform.python_version()
    mem_info = psutil.virtual_memory().total
    gb = mem_info /(1024 ** 3)
    return [numCpu, osVersion, pythonVersion, gb,]
 

def main ():

    if 'Windows' in (platform.platform()):
        print ("This is a windows System!")
        inventoryPrint = inventory()
        # print(inventoryPrint)
        for i in inventoryPrint:
            print(i)
    else:
        print ("This is a Linux System!")
        inventoryPrint = inventory()
        # print(inventoryPrint)
        for i in inventoryPrint:
            print(i)

if __name__ == '__main__':
    main()