"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   -Abstraction: Hiding details that's not needed and focus on what is needed.

   -Encapsulation: Keeping everything together. The data and functions should be paired together.
   
   -Polymorphism: Interchangeability of components. A method in parent class used
   again in child classes therefore the method has the same behavior in different classes.
   
   -Inheritance: a concept. you can call the parent class in the child class to use
   its instances (parente class's instances).

2. What is a class? 
a way to keep a function and all of its related data structure together. 

3. What is an instance attribute? 
attribute is data. instance attribute is when the attribute is specific to that class.
4. What is a method?
another way of saying function when it's used in class.

5. What is an instance in object orientation?
concrete occurance of any object (object can be a variable, data structure or a function).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   class attribute when you want to hard code a piece of information to the class, for example
   a variable that's passed in a value to where you know it will be used throughout; although
   you can still over write it but it has to be called out again in sub class with its new value.
   It is written outside of the methods right after the class. instance attribute is inside a method

"""


# Parts 2 through 5:
# Create your classes and class methods


class Chile_Peppers(object):
	def __init__(self, name, color, weight_in_pounds, health_remedy, country_origin):
		
		self.name = name
		self.color = color
		self.weight_in_pounds = weight_in_pounds
		self.health_remedy =  health_remedy
		self.country_origin = country_origin


	def base_price(self):

		# green chile peppers are more expensive than red or orange chile peppers.

		if color == "green":
			price = 4
		else:
			price = 2




	def get_total(self):


			# base_price = self.base_price()
		
		if country_origin == "Spain":
			total = (self.weight_in_pounds) * (price * 1.5)

		else:
			total = (self.weight_in_pounds) * price
		
		return total

	def is_it_spicy():
		""" determine if the chile pepper is spicy based on the name entered. """

		if self.name == "Cayenne" or "Serrano" or "Habanero":
			print "Eat this chile pepper with caution!"

		if self.name == "Poblano" or "Chilaca" or "Hot Banana" or "Jalapeno":
			print "This chile pepper is semi-spcicy!"

		if self.name == "Guindilla Verde" or "Basque Fryer" or "Anaheim" or "Guernica" :
			print "Enjoy this sweet chile pepper!"
		else:
			print "I don't know the type of pepper entered."



	def get_country_origin(self):
		""" which country is this chile pepper from?"""

		return self.country_origin

	class Spicy_Peppers(Chile_Peppers):
		""" Create a class specifically for spicy chile peppers."""
		def __init__(self, name, color):

		def hotness(self):
			print "It will burn through your gloves!"

			super(Spicy_Peppers, self).__init__(weight_in_pounds, "Say good-bye to your sinus issues!", "America")


	class Sweet_Peppers(Chile_Peppers):
		""" Create a class specifically for sweet peppers."""
		def __init__(self, name, color):

			super(Sweet_Peppers, self).__init__(weight_in_pounds,"Say good_bye to your aches and pain", "Spain")

		# def health_remedy(self):