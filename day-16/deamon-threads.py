import threading
import time

def log_timer():
    count = 0
    print()
    print()
    while True:
        time.sleep(1)
        count += 1
        print('U logged in for: ' + str(count) + 'seconds')

x = threading.Thread(target=log_timer, daemon=True)
x.start()

agr = input('Do u want to exit?: ')
