### 
# A program that checks if the PIN code entered in the payment terminal is correct
#

correct_pin = '0805'
attempts = 3

for attempt in range(attempts):
    pin = input('Enter the PIN code: ')
    if pin == correct_pin:
        print('Access granted.')
        break
    else:
        print('Incorrect...')
else:
    print('Sorry, your payment card has been blocked.')