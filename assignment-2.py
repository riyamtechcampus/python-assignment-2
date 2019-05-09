num = int(input('enter tbe number : '))

for i in range(2, num):
    if num % i == 0:
        print('not prime number ')
        break
else:
    print('its prime number ')
