def uniqueIngredients(l):
  ing=list()
  for x in l:
    for y in x:
      if(y.isnumeric()):
        continue
      if(y in ing):
        continue
      else:
        ing.append(y)
  return ing #Function to pick out all the ingredients
def addNumbering(l):
  i=0
  for x in l:
    x.insert(0,i)
    i+=1
  return l      
def convStrtoInt(l):
  for x in l:
    x[0]=int(x[0])
  return l
def twotothree(l,ing):
  for x in l:
    b=x[2:len(x)]
    x.append(b)
  for x in l:
    for y in x:
      if y in ing:
        x.remove(y)
    x.remove(x[2])
  return l     
def ranking(l):
  a=list()
  for x in range(len(l)):
    a.append(l[x][2])
  return a
def ranking1(e,l):
  o=list()
  for x in e:
    z=list()
    for y in e:
      a=len(set(x)&set(y))
      z.append(a)
    o.append(z)
  for x in range(len(l)):
    g=l[x][1]/2
    for x1 in range(len(o[x])):
      if(o[x][x1]>=g):
        o[x][x1]=0
      else:
        o[x][x1]=1
  return o
def feeder(o,l):
  i=0
  for x in o:
    l[i].append(x)
    i+=1
  return l

if __name__=='__main__':
  
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\HashCode2021\\a_example") #Reads the file
  b=a.readline()                                     
  b=b.split()                                       
  l=list()                     
  for x in range(int(b[0])):                                
    c=a.readline()      
    c=c.split()
    l.append(c)
 
  #Functions modified and added on 8/1/2021
  ing=uniqueIngredients(l) #Picking out the unique ingredients used in all the pizzas in the variabe "ing"
  l=convStrtoInt(l)      #Converting the string part of the list into integer
  l=addNumbering(l)        #Added numbering to pizza list for easy naviagtion of a pizza
  #l- [pizza number,number of pizza ingredients,pizza ingredients.......]
  l=twotothree(l,ing)
  e=ranking(l)
  o=ranking1(e,l)
  l=feeder(o,l)
  
  
  