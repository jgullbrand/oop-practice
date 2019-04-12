# Representation of volunteers at an organization

class Volunteer:
	"""Represents a Volunteer - Parent Class"""	

	num_volunteers = 0

	#Constructor used for instantiating an instance.'self' represents the instance
	def __init__(self, first_name, last_name, status, committee_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name + " " + self.last_name
		self.status = status
		self.committee_name = committee_name
		Volunteer.num_volunteers += 1
		print("{} has officially joined the team!".format(self.full_name))

	#Returns a string representation of the instance	
	def __repr__(self):
		return self.full_name

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
		

class CommitteeManager(Volunteer):
	"""Represents a CommitteeManager. Inherits from Volunteer."""
	
	def __init__(self, first_name, last_name, status, committee_name, stipend, committee_members=None):
		super().__init__(first_name, last_name, status, committee_name)
		self.stipend = stipend
		if committee_members is None:
			self.committee_members = []
		else:
			self.committee_members = committee_members	

	def add_volunteer(self, vol):
		if vol not in self.committee_members:
			self.committee_members.append(vol)
			print(f'added {vol} to the team')

	def remove_volunteer(self, vol):
		if vol in self.committee_members:
			self.committee_members.remove(vol)	

	def print_volunteer_team(self):
		for vol in self.committee_members:
			print(f'Name: {vol.full_name}')		
				


volunteer1 = Volunteer('Jamie', 'Gullbrand', 'Active', 'Special Events')
# volunteer1.print_profile()

manager1 = CommitteeManager('Lara', 'Gech', 'Active', 'Special Events', 10000)

manager1.add_volunteer(volunteer1)

print(manager1.committee_members)

print(manager1.print_volunteer_team())

# manager1.print_volunteer_team()

# print(Volunteer.num_volunteers)