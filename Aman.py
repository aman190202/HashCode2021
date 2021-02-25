if __name__=='__main__':
  
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\a.txt") #Reads the file
  b=a.readline()                                     
  b=b.split()
  D=int(b[0])
  I=int(b[1])
  S=int(b[2])
  V=int(b[3])
  F=int(b[4])
  l=list()
  for x in range(S):                                
    c=a.readline()      
    c=c.split()
    l.append(c)
  print(l)