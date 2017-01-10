print(" 1 Add\n 2 Subtract\n 3 Multiply\n 4 Divide\n")
selection = int(raw_input("input selection: "))

if selection  == 1:
		int1= int(input("input the 1st number."))
		int2= int(input("input the 2nd number."))
		print (int1+int2)
elif selection == 2:
		int1= int(input("input the 1st number."))
		int2= int(input("input the 2nd number."))
		print (int1-int2)
elif selection == 3:
		int1= int(input("input the 1st number."))
		int2= int(input("input the 2nd number."))
		print (int1*int2)
elif selection == 4:
		int1= float(input("input the 1st number."))
		int2= float(input("input the 2nd number."))
		print (int1/int2)




