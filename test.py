from PyCLIBar.CLIBar import CLIBar
import time

bar = CLIBar()

steps = 15

# You can either set the maximum elements on it's own
# bar.set_max(steps)
# bar.start()
# or pass it as a keyword argument on start
bar.start(_max=steps)

print('Taking 15 steps, 1 pr. 0.5 seconds.')

for n in range(steps):
    bar.step()
    print("{} {}".format(bar.get_bar(), bar.get_progress()), end='\r')
    time.sleep(0.5)

print('\nTest complete')
