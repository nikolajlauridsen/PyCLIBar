from PyCLIBar.CLIBar import CLIBar
import time

bar = CLIBar()

steps = 15

bar.set_max(steps)
bar.start()

print('Taking 15 steps, 1 pr. 0.5 seconds.')

for n in range(steps):
    bar.step()
    print(bar.get_bar(), end='\r')
    time.sleep(0.5)

print('Test complete')
