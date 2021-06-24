#from people import Person
#from people import Student

# this is the same as the 
# two lines above
from people import Student, Person 

# Imports everything from people.py
#from people import *

def main():
	adam = Person('adam')

	esha = Student('esha', 123454)
	
	print(esha.name, esha.ID)
	print(adam.name)


	john = Person('john')
	john2 = Person('john2')

	john.marry(john2)
	#import pdb; pdb.set_trace()

if __name__ == '__main__':
	main()