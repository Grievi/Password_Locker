class User:

    '''
    Create an instance of an object or blueprint for users
    '''

    user_list = []

    def __init__(self,user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        Save user method saves a new user
        '''

        User.user_list.append(self)

class Credentials:
    '''
    this class creates usser credentials and save their information
    '''
    credential_list = []
    user_credentials_list = []

    @classmethod
    def check_user(cls, first_name, password):
        '''
		Method that checks if the username and password entered match entries in the users_list
		'''
        current_user = ''
        for user in User.user_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        This will create an instance of the different site names and the user credentials
        '''
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Creates a function that saves a new user's credentials
        '''
        Credentials.credential_list.append(self)

    @classmethod
    def display_credentials(cls, user_name):
        '''
        This is a class method that displays user's credentials
        '''
        user_credentials_lists = []
        for credential in cls.user_credentials_list:
            if credential.user_name == user_name:
                user_credentials_lists.append() #pass in credentials






