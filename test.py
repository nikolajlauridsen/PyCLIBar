from PyCLIBar.CLIBar import CLIBar
import time

def test_bar(bar):
    for n in range(steps):
        print(bar.get_progress_bar(), end='\r', flush=True)
        time.sleep(0.5)
        bar.step()

steps = 15


print('Taking 15 steps, nothing but progress')
# You can either set the maximum elements on it's own
# bar.set_max(steps)
# bar.start()
# or pass it as a keyword argument on start
bar = CLIBar(bar_width=0, est=False)
bar.start(_max=steps)
test_bar(bar)

print('Taking 15 step, with nothing but bar')
bar = CLIBar(est=False, progress=False)
bar.start(_max=steps)
test_bar(bar)

print('Taking 15 steps with the whole shebang')
bar = CLIBar()
bar.start(_max=steps)
test_bar(bar)

print('\nTest complete')
