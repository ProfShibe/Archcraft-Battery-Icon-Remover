# Archcraft-Battery-Remover
Python script that automatically removes the battery icon on the Archcraft Polybar, replacing it with whatever you want.

Intended for Archcraft users who are on a Desktop, but still see the battery icon on Polybar.

Drop the main.py file in ~/.config/openbox/themes/

CD into that same directory in a terminal

From here, change the "CONTENT" variable in the "main" function of main.py to whatever text you want to replace the battery icon with.
Then, execute the script by running "python3 main.py", or "python main.py" in a terminal.

**The script will automatically generate backups of all files it modifies. So in case anything goes wrong and the theme changes, you can revert everything.**

You can then change themes. All themes that had a battery icon that was displaying as N/A for Desktop users will be replaced with your desired text (you can leave it blank if you want nothing there).

If you want to change the text it displays as after running it, replace all the newly made files with the backups and run it again.

**Known Bugs: Doesn't work on the "Easy" theme. Can't figure out how the battery icon is displaying on it.
            Some padding issues on the "Default" theme. Will fix soon.**
