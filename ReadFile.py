#Function to pick out all the ingredients
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
  return ing


if __name__=='__main__':
  
  #Creating an extension to read a file and extract its elements
  a=open("C:\\Users\\agarw\\OneDrive\\Desktop\\HashCode2021\\a_example") #Reads the file
  b=a.readline()                 #Reads the first line of the file
  b=b.split()                    #Splits the contents of the file b[1]-number of 2; b[2]- number of 3 ; b[3]-number of 4
  l=list()
  T=[[2],[3],[4]]                     
  for x in range(int(b[0])):    
    c=a.readline()      
    c=c.split()
    l.append(c)
  
  #Picking out the unique ingredients used in all the pizzas in the variabe "ing"
  ing=uniqueIngredients(l)
