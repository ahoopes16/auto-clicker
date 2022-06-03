# This is based off the code example found at https://nitratine.net/blog/post/python-auto-clicker/#final-code

from configparser import ConfigParser
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from random import uniform
import time
import threading

settings = {"max_delay_seconds": 10, "min_delay_seconds": 0}
try:
    config = ConfigParser()
    config.read('settings.ini')
    settings['max_delay_seconds'] = config.getint(
        'DEFAULT', 'max_delay_seconds')
    settings['min_delay_seconds'] = config.getint(
        'DEFAULT', 'min_delay_seconds')
except Exception as e:
    print('Could not read configuration file. Continuing with default settings.' + e)

button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
mouse = Controller()


class ClickMouse(threading.Thread):
    def __init__(self, min_delay, max_delay, button):
        super(ClickMouse, self).__init__()
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                delay = round(uniform(self.min_delay, self.max_delay), 2)
                time.sleep(delay)
            time.sleep(0.1)


click_thread = ClickMouse(
    settings['min_delay_seconds'], settings['max_delay_seconds'], button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
