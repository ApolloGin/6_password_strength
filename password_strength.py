import re

def get_password_strength(password):
    patterns = [r'[A-Z]', r'[a-z]', r'[0-9]', r'[^a-zA-Z0-9]']
    pwd_length = len(password)
    
    pwd_strength = int(pwd_length > 7) + int(pwd_length > 11)
    for x in (len(re.findall(pattern, password)) for pattern in patterns):
        pwd_strength += int(x > 0) + int(x > 2)

    return pwd_strength



if __name__ == '__main__':
    password_strength = get_password_strength(input('Enter password: '))
    print('Password strength is {0} out of 10'.format(password_strength))
    