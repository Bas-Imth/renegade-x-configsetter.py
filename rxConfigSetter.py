#!/usr/bin/python3

# This script will automatically fill in the Renegade X server config based on its directory name.
# For example, over @ CT, we name stuff Marathon, PUG, Custom, etc.
# Based on that name, the script will match it to the template directory template/<gamemode>/ and load it up.
# After that, it tries to set all the correct values.

# ======================= Preamble =====================================

# <To be filled in later>

# ======================= Imports =====================================

import re

# For interaction with the host OS
import sys

from pathlib import Path, PureWindowsPath

# ======================= Metadata =====================================

AUTHOR = "Bas Imth"
LICENSE = "GPL-3"
SCRIPT_VERSION = 1.0
HEADERTEXT = """rxConfigSetter"""

# ======================= Functions =====================================


def version_information():
    print(
        "Author: {}\nLicense: {}\nVersion: {}\n".format(AUTHOR, LICENSE, SCRIPT_VERSION)
    )
    return


# This function sets all the paths and calls the "setter" function.
def load_rx_config(gamemode, rx):
    template_path = "templates/" + gamemode + "/"
    target = rx + "/UDKGame/Config/"
    config_files = Path(template_path).glob("*.ini")
    for file in config_files:
        config = file.stem + ".ini"
        print(config)
        set_rx_config(target, template_path, config)


# This is the function that actually sets the configs correctly, using the given data, it will load the template config and then open the target config and overwrite the selected lines.
def set_rx_config(target, template, config):
    path_get = Path(template + config)
    path_set = Path(target + config)
    setting = []
    variable = []
    # This.. Function doesn't care about memory. Which is fine for RX config files, but NOT SUITABLE FOR BIG FILES OR MEMORY EFFICIANCY, APOLLO WILL NOT REACH THE MOON!
    with open(path_get, "r") as getter:
        # Read a list of lines into memory.
        get = getter.readlines()
        for line in get:
            # We split the line on '&', and assign the first part of the line (for example GamePassword=) to 'settin' variable, the the second part (for example: ILoveSho) to the 'var' variable.
            settin, var = line.split("&")
            # Now we add the variable from settin to the array "setting", we use this weird method because this is how Python makes array's longer. Deal with it.
            setting.append(settin)
            variable.append(var)  # Same for variable
    with open(path_set, "r") as loader:
        load = loader.readlines()
    for x in range(len(setting)):
        for i, line in enumerate(load):
            # If the line of the file starts with for example: GamePassword=, we will overwrite it.
            if line.startswith(setting[x]):
                print(setting[x] + variable[x])  # Just a safety print.
                # We now overwrite the line and add a new line to make sure no weird config fuck ups happen. (Does cause weird random empty lines)
                load[i] = setting[x] + variable[x] + "\n"
    # And write everything back.
    with open(path_set, "w") as setter:
        setter.writelines(load)


def main():
    # Make all system normal at functioning parameters.
    # https://youtu.be/uXgiqBdfSz8?t=75
    version_information()
    try:
        directory_name = sys.argv[1]
        print(directory_name)
    except:
        print("Please pass directory_name")
    # We ask for a directory at launch, we will look at its name to determine what gamemode it is, using that, we apply the correct config.
    if re.match("marathon", directory_name):
        print("Loading Marathon")
        load_rx_config("marathon", directory_name)
        exit()
    else:
        print("No clue what game-mode this is, bye!")
        exit()


# ======================= Main =====================================
main()
