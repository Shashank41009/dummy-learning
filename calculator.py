class Calculator:
	def __init__(self):
		pass
	def add(self, *values):
		return sum(values)
	def subtract(self, *values):
		return values[0] - values[1]
cal = Calculator()
print(cal.add(1,2))
print(cal.subtract(1,2)) #subtract added


