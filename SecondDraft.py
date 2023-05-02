import random
import requests
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from windows import GreetingWindow

def main():
    win = GreetingWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
