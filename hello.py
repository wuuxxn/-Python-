def square(y):
	print("{} 的平方為 {},三次方是{}".format(y, y*y,y*y*y))
	
x = int(input("請輸入整數："))

print("python程式測試", x)

if(x<0):
	print("輸入的值負數")
elif(x==0):
	print("輸入的值為0")
else:
	for i in range(1,x+1):
		square(i)
