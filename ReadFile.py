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

if __name__=='__main__':
  
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\HashCode2021\\a_example") #Reads the file
  b=a.readline()                                     
  b=b.split()                                       
  l=list()
  T=[[2],[3],[4]]                     
  for x in range(int(b[0])):                                
    c=a.readline()      
    c=c.split()
    l.append(c)
 
  #Functions modified and added on 8/1/2021
  ing=uniqueIngredients(l) #Picking out the unique ingredients used in all the pizzas in the variabe "ing"
  l=convStrtoInt(l)      #Converting the string part of the list into integer
  l=addNumbering(l)        #Added numbering to pizza list for easy naviagtion of a pizza
  #l- [pizza number,number of pizza ingredients,pizza ingredients.......]
  l.sort(reverse=True,key=len)
  print(l)