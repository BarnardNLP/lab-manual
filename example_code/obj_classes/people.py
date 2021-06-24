class Person:

	def __init__(self, name: str):
		self.name = name
		self.partner = None

	def __str__(self):
		return self.name


	def marry(self, spouce): #: Person):
		self.partner = spouce
		spouce.partner = self



class Student(Person):

	def __init__(self, name, ID: int):
		self.name = name
		self.ID = ID

