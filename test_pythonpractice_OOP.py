import unittest
from pythonpractice_OOP import Volunteer, CommitteeManager

class TestVolunteer(unittest.TestCase):

	def setUp(self):
		self.volunteer_1 = Volunteer('Jamie', 'Gullbrand', 'Active', 'Special Events')

	def test_full_name(self):
		self.assertEqual(self.volunteer_1.full_name, 'Jamie Gullbrand')

	def test_email(self):
		self.assertEqual(self.volunteer_1.get_email(), 'Jamie.Gullbrand@org.com')	


class TestCommitteeManager(unittest.TestCase):

	def setUp(self):
		self.manager1 = CommitteeManager('Lara', 'Gech', 'Active', 'Special Events', 10000)

	def test_email(self):
		self.assertEqual(self.manager1.get_email(), 'Lara.Gech@org.com')	

	def test_stipend_amount(self):
		self.assertEqual(self.manager1.stipend, 10000)	


if __name__ == '__main__':
    unittest.main()		