if __name__=='__main__':
  
  a=open("C:\\Users\\joels\\OneDrive\\Desktop") #Reads the file
  b=a.readline()                                     
  b=b.split()
  D=int(b[0])
  I=int(b[1])
  S=int(b[2])
  V=int(b[3])
  F=int(b[4])
  l1=list()
  for x in range(S):                                
    c=a.readline()      
    c=c.split()
    l1.append(c)
  l2=list()
  for x in range(V):
    e=a.readline()
    e=e.split()
    l2.append(e)
  print(l2)