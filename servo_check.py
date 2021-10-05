# for testing servo positions

global servo
global direction
servo = 0
direction = 1
servo_value = 100


print('Enter 1, 2 or 3 for sun, mask or moon')
print('Enter f for forward or r for reverse for servo direct')
print('Enter exit to exit')
while 1:
    key_press = input('Press a key ')

    if key_press == 'exit':
        exit()

    if key_press == '1':
        servo = 0
        servo_value = 100
        print('Servo sun has been selected, servo_value set to 100')

    if key_press == '2':
        servo = 2
        servo_value = 100
        print('Servo mask has been selected, servo_value set to 100')

    if key_press == '3':
        servo = 3
        servo_value = 100
        print('Servo moon has been selected, servo_value set to 100')

    if key_press == 'f':
        print('Direction set to forward')
        direction = 1

    if key_press == 'r':
        print('Direction set to reverse')
        direction = -1

    if len(key_press) == 0:
        servo_value += direction
        print('move servo {} in the direction {} with value {}'.format(servo, direction, servo_value))
