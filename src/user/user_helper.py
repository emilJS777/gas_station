import random
import string


# GENERATE TICKET CODE
def generate_ticket_code(length=45, uppercase=True, lowercase=True, numbers=True):
    ticket_code = ''

    if uppercase:
        ticket_code += string.ascii_uppercase
    if lowercase:
        ticket_code += string.ascii_lowercase
    if numbers:
        ticket_code += string.digits

    return ''.join(random.choice(ticket_code) for i in range(length))
