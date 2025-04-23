try:
    print(a)
except Exception as e:
    print ("Something went wrong")
    error = e
    
print (f"""This was the issue: 
       
{error}""")