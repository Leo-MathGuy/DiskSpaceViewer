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
9. "tkinter" PyPi package required
