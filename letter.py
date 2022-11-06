salutation = 'Mr.'
name = 'Xen Chen'
product = 'Blockchain automated curtain blinds'
verb = 'malfunctioned'
room = 'bedroom'
animals = 'cats'
amount = '$5000'
percentage = '12'
spokesman = 'Kim Jung Kun'
job_title = 'Customer Support'

letter = f'''
    Dear {salutation} {name},
    
    Thank you for your letter, we are sorry that our {product}
    {verb} in your {room}. Please note that it should never be used in a {room},
    especially near any {animals}.
    
    Send us your receipt and {amount} for shipping and handling.
    We will send you another {product} that, in our tests,
    is {percentage}% less likely to have {verb}.
    
    Thank you for your support.
    
    sincerely,
    {spokesman}
    {job_title}
'''

print(letter)

new_letter = '{} yes? You\'d have to pay me {} for that to happen'.format('Kiyotaka', '12,000 private points')
print(new_letter)
