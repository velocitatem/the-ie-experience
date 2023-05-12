import random
import requests
import gi
gi.require_version("Gtk", "3.0") # Make sure we have Gtk 3.0
from gi.repository import Gtk # Import Gtk 3.0

from windows import GreetingWindow

def main():
    # Create a new window to greet the user
    win = GreetingWindow()
    win.connect("destroy", Gtk.main_quit)
    # Display the window
    win.show_all()
    # Start the Gtk main loop
    Gtk.main()

if __name__ == "__main__": # If this file is run directly
    main() # Run the program
