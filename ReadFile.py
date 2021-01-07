
if __name__=='__main__':
  #Creating an extension to read a file and extract its elements
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\HashCode2021\\a_example") #Reads the file
  b=a.readline()                 #Reads the first line of the file
  b=b.split()                    #Splits the contents of the file
  l=list()                      
  for x in range(int(b[0])):    
    c=a.readline()      
    c=c.split()
    l.append(c)
  #Picking out the unique ingredients used in all the pizzas in the variabe "ing"
  ing=list()
  for x in l:
  	for y in x:
  		if(y.isnumeric()):
  			continue
  		if(y in ing):
  			continue
  		else:
  			ing.append(y)
  print(ing)

