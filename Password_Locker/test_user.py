import unittest
from user import User, Credentials

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
        self.assertEqual(len(User.users_list),0)


class TestCredentials(unittest.TestCase):

    def test__init__(self):
         '''
         Test to if check the initialization/creation of credential instances is properly done
         '''
         self.assertEqual(self.new_credential.user_name,'Grievin')
         self.assertEqual(self.new_credential.website_name,'Facebook')
         self.assertEqual(self.new_credential.account_name,'Babaa')
         self.assertEqual(self.new_credential.password,'password')

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credentials('Grievin','Facebook','Babaa',  'password')

    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User('JoJo','password')
        self.new_user.save_user()
        user2 = User('Sabuni','jamaa')
        user2.save_user()
        current_user = 'JoJo'
        for user in User.users_list:
            if user.user_name == user2.user_name and user.password == user2.password:
                current_user = user.user_name
        return current_user

    def test_save_credential(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        # self.new_credentials.save_credentials()
        facebook = Credentials('Grievin','Facebook','Babaa','0000')
        facebook.save_credentials()
        # self.assertEqual(len(Credentials.credentials_list),2)

    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credentials.credentials_list = []
        User.users_list = []

if __name__ == '__main__':
    unittest.main(verbosity=2)