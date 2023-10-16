#liansip_3.py

factor = []
while True:
	try:
		number = input("請提供一个數字：")
		if number == "":
			break
		number = int(number)
		i = 1
		for i in range(1, number + 1):
			if number % i == 0:
				factor.append(i)

		print(number, "的因數有：", end = " ")
		for j in factor:
			print(j, end = " ")

		print("")
		factor = []

	except ValueError:
		continue