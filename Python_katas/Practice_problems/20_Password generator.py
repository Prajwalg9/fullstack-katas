import random
import string
ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
def generate_password(inp):
    password = []
    if inp<5:
        raise ValueError
    else:
        password.append(random.choice(ascii_lowercase))
        password.append(random.choice(ascii_uppercase))
        password.append(random.choice(punctuation))
        password.append(random.choice(digits))
        allchars=ascii_uppercase+digits+punctuation+ascii_lowercase
        K=inp-4
        password.extend(random.choices(allchars,k=K))
        random.shuffle(password)
        return "".join(password)
print(generate_password(8))