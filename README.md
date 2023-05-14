# Disk Space Viewer

## What is it
Something I made in 30 minutes. Shows 10000 5px squares on a 500x550 screen, red to green, looking at the df output.

Works by:
(systemd service) --starts--> (sh script) --sends data--> (/var file) --used by--> (python app)

## How to setup

1. Copy the .service file into /etc/systemd/system (or equivalent)
2. Set 744 permissions to the file
3. Replace the { REPLACE } with the place you will copy the script to. (For example, /home/{user}/.local/bin/disk-space-updater)
4. Copy the script into that location
5. Replace the 1 in "sed '1q;d'" on lines 5 and 6 to the line on which the desired partrition in df shows up.
6. Add 700 permissions to the script
7. Run "systemctl (start or enable, your choice) disk-space-updater" or eqivalent
8. Check journal to see if configured correctly
9. "tkinter" PyPi package required (pip3 install tkinter)
10. Run "python3 disk-space-viewer.py" while in same directory to run program

## Additional

* Add application to KDE:
  1. Open Menu Editor
  2. Click "Utilities"
  3. Click "Add"
  4. Write "python3" in "Program"
  5. Write python program location in "Command-Line Arguments"
  6. Click blank square in top right
  7. Find an icon (for example, ksysguard icon)
  8. Ctrl-S
  9. Congrats you can now launch this from the KDE menu

## Troubleshooting

* /var/ File not showing
  1. Make sure service is started
  2. Check journal
    * If shows syntax error:
    * Probably script is configured wrong
* Stuck on Loading...
  1. Make sure service is started
  2. Make sure read perms are in the /var/ file
