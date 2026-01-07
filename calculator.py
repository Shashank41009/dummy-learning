class Calculator:
	def __init__(self):
		pass
	def add(self, *values):
		return sum(values)
cal = Calculator()
print(cal.add(1,2))
