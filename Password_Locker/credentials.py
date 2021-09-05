
from user import Credentials, User

def create_user(username, password):
    '''
    a new user account function
    ''' 
    new_user  = User(username, password)
    return new_user

def save_user(user):
    '''
    A Function that saves th user
    '''
    User.save_user(user)
def verify_user(username, password):
    '''
    verify user function that checks user sCredentialss
    '''
    checking_user = Credentials.check_user(username, password)
    return checking_user

def create_credential(user_name, website_name, account_username, password):
    '''
    A function that creates the users credentials that is website, account username and account password
    '''
    new_credential = Credentials(user_name, website_name, account_username, password)
    return  new_credential

def save_credential(credential):
    '''
	Function to save a newly created credential
	'''
    Credentials.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credentials.display_credentials(user_name)

# def copy_credential(site_name):
# 	'''
# 	Function to copy a credentials details to the clipboard
# 	'''
# 	return Credentials.copy_Credentials(site_name)

def main():
    print('')
    print('-'*100)
    while True:
        print("Hello! Welcome to Password locker")
        print('\n')
        print('-'*100)
        print("Choose a short code to navigate through:\n :To create new user select type -'nw'\n :To sign in to your account type 'sn'\n :To create a credential select -'cr'  ")
        print('\n')
        print (" :or 'q' to quit")
        short_code = input().lower()
        print('\n')

        if short_code == 'new':
            print('Create Username')
            created_username = input()


            print('Create password')
            created_password = input()

            print('confirm password')
            confirm_password =input()

            save_user(create_user((created_username, created_password)))
            print(' ')
            print('New Account created succesfully')

            while confirm_password != created_password:
                print('Password did not match Try again!')
                print('Enter Your Password')
                created_username = input()
                print('confirm password')
                confirm_password =input()

            else:
                print(f'Congratulations {created_username}! Account creation was succesful')
                print('\n')
                print('Login into your Created Account')
                print('Enter Username')
                entered_username = input()
                print('Enter Your Password')
                entered_password = input()

            while entered_username != created_username or entered_password != created_password:
                print('Entered Username or password is invalid')
                print('\n')
                print('Enter Username')
                entered_username = input()
                print('Enter Your Password')
                entered_password = input()


            else:
                print(f'Welcome! {entered_username} To Your Lockers Account')
                print('\n')

        elif short_code == 'sn':    
            print('Welcome To Password locker')
            print('Enter Username')
            user_name = input()
            print('Enter Your Paasword')
            password = input()
            user_exist = verify_user(user_name, password)

            if user_exist == user_name:
                print(" ")
                print(f'Welcome {user_name}. Please select an option to continue.')
				
                while True:
                    print("-"*100)
                    print('Select codes: \n cr-Create a Credential \n dc-Display Credentials \n and ex-Exit')
                    short_code = input().lower()
                    print('\n')
                    if short_code == 'ex':
                        print('You have logged out')
                        break
                    else:
                        print('Enter Your Username and Password')
        elif short_code == 'cr':
            print('')
            print('Enter your credential details:')
            print('Enter Website name')
            website_name = input()
            print('Enter Your Account username')
            account_username = input()
            print('Enter your password')
            password = input()
                
            save_credential(create_credential(user_name, website_name, account_username, password))
            print('')
            print(f'User Credential created for : Website name {website_name}  - Account Name:{account_username}- Password{password}')
            print(' ')
        elif short_code == 'dc':
            print(' ')
            if display_credentials(user_name):
                print('Here is a list of all your credentials')
                print(' ')
                for credential in display_credentials(user_name):
                    print(f'Site Name: {credential.account_name}- password:{credential.password}')
                    print('  ')
            else:
                print('Something went Wrong!Try Again')
                print('\n')
                print('\n')

        elif short_code == 'q':
                break
        else:
            print('Enter a valid code to conitinue')
            print('-'*100)


if __name__ == '__main__':
	main()
