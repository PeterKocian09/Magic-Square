try:
	a = int(input("value of a: "))
	b = int(input("value of b: "))
except:
	print("Invalid value for a or b")
	quit()

print ("Sum of magic square: ",a*21+b)
print ("----------------Magic Square---------------------")
print (a+b,a,12*a,7*a)
print (11*a,8*a,b,2*a)
print (5*a,10*a,3*a,3*a+b)
print (4*a,2*a+b,6*a,9*a)
print ("--------------------------------------------------")
