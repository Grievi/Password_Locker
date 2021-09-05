import unittest
from user import Credentials, User

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Grievin','password')

    def test__init__(self):
        '''
        test for initialization of creation of user instance
        '''
        self.assertEqual(self.new_user.user_name,'Grievin')
        self.assertEqual(self.new_user.password,'password')