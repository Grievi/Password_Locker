
from credentials import User, Credential

def create_user(user_acc, password):
    '''
    a new user account function
    ''' 
    new_user  = User(user_acc, password)
    return new_user

def save_user(user):
    '''
    A Function that saves th user
    '''
    User.save_user(user)
def verify_user(user_acc, password):
    '''
    verify user function that checks user credentials
    '''
    checking_user = Credential.check_user(user_acc, password)
    return checking_user

def create_credential(user_name, website_name, account_username, password):
    '''
    A function that creates the users credentials that is website, account username and account password
    '''
    new_credential = Credential(user_name, website_name, account_username, password)
    return  new_credential

def save_credential(credential):
    	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)

def main():
    print('')
    print('-'*100)
    while True:
        print("Hello! Welcome to Password locker")
        print('\n')
        print('-'*100)
        print("Choose a short code to navigate through: to create new user select 'nw': To sign in to your account 'sn' ")
        print('\n')
        print (" or 'q' to quit")
        short_code = input().lower()
        print('\n')

        if short_code == 'nw':
            print('Create Username')
            created_username = input()


            print('Create password')
            created_password = input()

            print('confirm password')
            confirm_password =input()

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
            default_username = input()
        
            print('Enter Password')
            default_user_password = input()
            print('\n')

            while default_username!= 'user' or default_user_password!= 0000:
                print('Wrong username or password. username "user" and pasword "0000"')
                print('Enter Username')
                default_username = input()

                print('Enter Paswword')
                default_user_password = input()
                print('\n')

            else:
                print('Sign-in Successfully')
                print('\n')
                print('\n')

        elif short_code == 'q':
                break
        else:
            print('Enter a valid code to conitinue')


if __name__ == '__main__':
	main()
