import unittest
from unittest.case import TestCase
from user import Credentials, User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class   behaviours.
    
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

    def test_save_user(self):
        '''
        Test to check if users info is saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest, TestCase):

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credentials('Grievin','Twitter','Babaa',  'password')

    def test__init__(self):
         '''
         Test to if check the initialization/creation of credential     instances is properly don
         '''
         self.assertEqual(self.new_credential.user_name,'Grievin')
         self.assertEqual(self.new_credential.site_name,'Facebook')
         self.assertEqual(self.new_credential.account_name,'Okush')
         self.assertEqual(self.new_credential.password,'okush')

    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credentials.credentials_list = []
        User.users_list = []

if __name__ == '__main__':
    unittest.main()