class Calculator:
	def __init__(self):
		pass
	def add(self, *values):
		return sum(values)
	def subtract(self, *values):
		total = values[0]
		for value in values[1:]:
			total -= value
		return total
cal = Calculator()
print(cal.add(1,2))
print(cal.subtract(1,2)) #subtract added


