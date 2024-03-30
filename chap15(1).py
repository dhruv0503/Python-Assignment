import time
import pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-c to quit.')

input()
print('Started.')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        lap = 'lap # {} {} ({})'.format((str(lap_num)+ ':').ljust(3),
                                         str(total_time).rjust(5),
                                         str(lap_time).rjust(6))
        print(lap, end='')


        lap_num += 1
        last_time = time.time()
        pyperclip.copy(lap)
except KeyboardInterrupt:
    print('\nDone.')