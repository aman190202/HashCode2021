import random
if __name__=='__main__':
  
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\b.txt") #Reads the file
  b=a.readline()                                     
  b=b.split()

  D=int(b[0]) #DURATION
  I=int(b[1]) #NUMBER OF INTERSECTION
  S=int(b[2]) #NUMBER OF STREETS
  V=int(b[3]) #NUMBER OF CARS
  F=int(b[4]) #BONUS POINT

  l1=list()
  l2=list()
  for x in range(S):                                
    c=a.readline()      
    c=c.split()
    c[0]=int(c[0])
    c[1]=int(c[1])
    c[3]=int(c[3])
    l1.append(c)

  l2=list()
  for x in range(V):
    e=a.readline()
    e=e.split()
    e[0]=int(e[0])
    l2.append(e)
  #l1[i][0]- beginning of the street l1[i][1]- end of the street l1[i][2]- name of the street l l1[i][3]- time taken
 
  n=random.randint(1,I)
  print(n)
  for _ in range(n):
    print(random.randint(0,I))
    m=random.randint(0,I)
    print(m)
    for x in range(m):
      print(l1[random.randint(0,S)][2],end=' ')
      print(random.randint(0,D))
 
