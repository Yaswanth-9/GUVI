import random
import string


def get_random_alpha_numeric_string(string_length = 16):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(string_length)))


def get_random_mail():
    mail = get_random_alpha_numeric_string(4) + "@" + get_random_alpha_numeric_string(3) + ".com"
    return mail
