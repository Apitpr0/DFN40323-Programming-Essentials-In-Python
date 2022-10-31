#This can be useful to close object and clean up resources
try:
    f=open("file.txt",'a'),
    f.write("Politeknik METrO Tasek Gelugor")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

