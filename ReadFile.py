if __name__=='__main__':
  a=open("//content//a_example") #Reads the file
  b=a.readline()                 #Reads the first line of the file
  b=b.split()                    #Splits the contents of the file
  l=list()                       
  for x in range(int(b[0])):    
    c=a.readline()      
    c=c.split()
    l.append(c)
#This is Aditya Agrawal 