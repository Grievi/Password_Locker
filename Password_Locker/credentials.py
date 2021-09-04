from user import User

def main():
    while True:
        print("Hello! Welcome to Password locker")
        print('\n')
        print("Choose a short code to navigate through: to create new user select 'nw': To sign in to your account 'sn' or 'q' to quit")
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
            created_username = input()
            print('Enter Your Password')

if __name__ == '__main__':
	main()
