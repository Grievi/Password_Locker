
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

def main():
    print('')
    print('-'*60)
    while True:
        print("\u001b[32;1mHello! Welcome to Password locker\u001b[0m")
        print('-'*60)
        print("Choose a short code to navigate through:\n :To create new user select type -'\u001b[32;1mnew\u001b[0m'\n :To sign in to your account type -'\u001b[32;1msn \u001b[0m'\n :To create a credential select -'\u001b[32;1mcr\u001b[0m'  \n:To display credentials type -'\u001b[32;1m dc\u001b[0m'")
        print (" :or '\u001b[31;1mq\u001b[0m' to quit")
        print('\u001b[36;1m Enter your selected choice:\n\u001b[0m')
        short_code = input().lower()
        print('\n')

        if short_code == 'new':
            print('\u001b[36;1mCreate Username\u001b[0m')
            created_username = input()


            print('\u001b[36;1mCreate password\u001b[0m')
            created_password = input()

            print('\u001b[36;1mconfirm password\u001b[0m')
            confirm_password =input()

            save_user(create_user(created_username, created_password))
            print(' ')
            print('\u001b[32;1mNew Account created succesfully\u001b[0m')

            while confirm_password != created_password:
                print('\u001b[31;1mPassword did not match Try again!\u001b[0m')
                print('\u001b[36;1mEnter Your Password\u001b[0m')
                created_username = input()
                print('\u001b[36;1mconfirm password\u001b[0m')
                confirm_password =input()

            else:
                print(f'\u001b[32;1mCongratulations {created_username}!Account creation was successful\u001b[0m')
                print('\n')
                print('\u001b[36;1mLogin into your Created Account\u001b[0m')
                print('\u001b[36;1mEnter Username\u001b[0m')
                entered_username = input()
                print('\u001b[36;1mEnter Your Password\u001b[0m')
                entered_password = input()

                while entered_username != created_username or entered_password != created_password:
                    print('\u001b[36;1mEntered Username or password is invalid\u001b[0m')
                    print('\n')
                    print('\u001b[36;1mEnter Username\u001b[0m')
                    entered_username = input()
                    print('\u001b[36;1mEnter Your Password\u001b[0m')
                    entered_password = input()


                else:
                    print(f'\u001b[32;1mWelcome! {entered_username} To Your Lockers Account\u001b[0m')
                    print('\n')

        elif short_code == 'sn':    
            print('\u001b[32;1mWelcome To Password locker\u001b[0m')
            print('\u001b[36;1mEnter Username\u001b[0m')
            user_name = input()
            print('\u001b[36;1mEnter Your Paasword\u001b[0m')
            password = input()
            user_exist = verify_user(user_name, password)

            if user_exist == user_name:
                print(" ")
                print(f'\u001b[32;1mWelcome {user_name}. Please select an option to continue.\u001b[0m')
				
                while True:
                    print("-"*100)
                    print('\u001b[32;1mSelect codes: \n cr-Create a Credential \n dc-Display Credentials \n and ex-Exit\u001b[0m')
                    short_code = input().lower()
                    print('\n')
                    if short_code == 'ex':
                        print('\u001b[36;1mYou have logged out\u001b[0m')
                        break
                    else:
                        print('\u001b[36;1mEnter Your Username and Password\u001b[0m')
        elif short_code == 'cr':
            
            print('')
            print('\u001b[36;1mEnter your credential details:')
            print('Enter your user_name\u001b[0m')
            user_name = input()
            print('\u001b[36;1mEnter Website name\u001b[0m')
            website_name = input()
            print('\u001b[36;1mEnter Your Account username\u001b[0m')
            account_username = input()
            print('\u001b[36;1mEnter your password\u001b[0m')
            password = input()    

            # else: 
            save_credential(create_credential(user_name, website_name, account_username, password))
            print('')
            print(f'\u001b[33;1mUser Credential created for: username {user_name} ; Website name: {website_name};Account Name:{account_username}- Password   {password}\u001b[0m')
            print(' ')
        elif short_code == 'dc':
            print('Enter Username')
            user_name=input()
            if display_credentials(user_name):
                print('Here is a list of all your credentials')
                print(' ')
                for credential in display_credentials(user_name):
                    print(f'Site Name: {credential.website_name}; Account Name: {credential.account_name} password: {credential.password}')
                    print('  ')
            else:
                print('\u001b[31;1mSomething went Wrong!Try Again')
                print('\n')
                print('\n')

        elif short_code == 'q':
                break
        else:
            print('\u001b[36;1mEnter a valid code to conitinue\u001b[0m')
            print('-'*100)


if __name__ == '__main__':
	main()
