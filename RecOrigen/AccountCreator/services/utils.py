import secrets
import string



def generate_password()->str:
    '''
        Will generate a password with a len of 20
    '''
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password