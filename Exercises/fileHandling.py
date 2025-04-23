try:
    with open("python.txt",'w') as fileski:
        fileski.write("MAYBE WE'LL MEET AT A BAR! WE'LL RIDE A FUNKY CARRRR X2")
except Exception as e:
    print(f"Slow down twin you got shit twisted\n {e}")

try:
    with open("python.txt",'r') as f2:
        print(f2.readlines())
except:
    pass