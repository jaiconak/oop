import shutil

source = "chart.yaml"
destination = "/Users/jaicosethnakpil/Desktop/Utrains/wk22-python/backup"

def versionMod(buildNum):
    with open("chart.yaml", "r") as file:
        content = file.readlines()
        backup = shutil.copy(source,destination)
        print(f"backup location: {backup}")

    with open("chart.yaml", "w") as file2:
        for line in content:
            if 'version' in line:
                file2.write(f'version: {buildNum} \n')
                print ("changed")
            else:
                file2.write(line) #keep it unchanged if build is same
                
                
versionMod(4.0)