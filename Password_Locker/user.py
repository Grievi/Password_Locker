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
    this class creates usser credentials
    '''