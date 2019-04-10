# Representation of volunteers at an organization

#Represents a Volunteer - Parent Class
class Volunteer:

	#Constructor used for instantiating an instance.'self' represents the instance
	def __init__(self, first_name, last_name, status, committee_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name + " " + self.last_name
		self.status = status
		self.committee_name = committee_name
		#print("created a volunteer instance: {}".format(self.full_name))
		# print("{} has officially joined the team!".format(self.full_name))

	#Returns a string representation of the instance	
	def __repr__(self):
		return self.full_name + ": " + self.committee_name

	def get_email(self):
		return "{}.{}@org.com".format(self.first_name,self.last_name)

	def print_profile(self):
		profile = """
		Full Name: {}
		Email: {}
		Committee: {}
		Volunteer Status: {}
		""".format(self.first_name, self.get_email(),self.committee_name ,self.status)
		print(profile)
		

#Represents a CommitteeManager - Subclass. Inherits from Volunteer.
class CommitteeManager(Volunteer):
	
	def __init__(self, first_name, last_name, status, committee_name, stipend, committee_members=None):
		super().__init__(first_name, last_name, status, committee_name)
		self.stipend = stipend
		if committee_members == None:
			self.committee_members = []
		else:
			self.committee_members = committee_members	

# volunteer1 = Volunteer('Jamie', 'Gullbrand', 'Active', 'Special Events')
# volunteer1.print_profile()


# manager1 = CommitteeManager('Lara', 'Gech', 'Active', 'Special Events', 10000)

# manager1.print_profile()


#print(volunteer1)
#print(manager1)