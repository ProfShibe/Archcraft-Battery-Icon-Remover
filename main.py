from pathlib import Path
from shutil import copy2  # For backups

# DISCLAIMER: THIS SCRIPT WILL ONLY RUN ONCE
# ENSURE THE "CONTENT" VARIABLE CONTAINS WHAT YOU ACTUALLY WANT THE ICON TO BE REPLACED BY!

def main():
    all_themes = find_polybar_folder()
    CONTENT = "Archcraft" # Change this to whatever! It will replace the battery icon on every theme!

    for theme in all_themes:
        fix_modules_file(theme, CONTENT)
########################################################
def find_polybar_folder():
    all_themes = []
    '''Searches current DIR for every file with a Polybar folder'''
    for dir in Path(".").iterdir():
        if dir.is_dir():
            if dir.iterdir():
                for item in dir.iterdir():
                    if item.name.lower() == "polybar":
                       all_themes.append(item)
    return all_themes
########################################################
def fix_modules_file(folder, _CONTENT):
    try:
        '''Changes the battery icon to CONTENT'''
        for file in folder.iterdir():
            if file.name == "modules.ini":
                # Generate a backup first!
                backup_file = str(file) + ".backup"
                copy2(file, backup_file)
                print(f"Created backup of {file} as {backup_file}.")

                with open(file) as modules:
                    lines = modules.readlines()

                modified = False
                for num, line in enumerate(lines, 1):
                    if "content-prefix = " in line:
                        print(f"Changing battery icon at line {num} in file {file}.")
                        modified = True

                        lines[num] = ''
                        lines[num - 2] = f'content = "{_CONTENT}"'
                        lines[num - 1] = ''
                        lines[num + 1] = f'\n'
                        lines[num + 2] = 'content-background = ${color.BACKGROUND3}'
                    # For the Gray theme with a vertical icon
                    elif "content-prefix = 󰂎" in line:
                        print(f"Changing battery icon at line {num} in file {file}.")
                        modified = True
                        lines[num - 2] = f'content = "{_CONTENT}"'
                        lines[num - 1] = '\n'
                        lines[num] = 'content-background = ${color.BACKGROUND3}'
                    elif 'content = ""' in line:
                        modified = True
                        print(f"Changing battery icon at line {num} in file {file}.")
                        lines[num - 1] = f'content = "{_CONTENT}"'
                        lines[num] = f'\n'

                if modified:
                    with open(file, "w") as modules:
                        modules.writelines(lines)
                        print(f"Properly modified {file}!\n")
                else:
                    print(f"No changes made in {file}. Likely already modified.\n")

    except IndexError as error:
        print(f"Something went wrong processing {folder}. {error}")
    except IOError as error:
        print(f"Something went wrong processing {folder}. {error}")
########################################################
if __name__ == "__main__":
    main()
