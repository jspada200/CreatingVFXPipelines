"""
Script to check in a maya file from commandline.
"""
import maya.standalone
maya.standalone.initialize()

import argparse
from JPipe.command_line_checkin import CommandLineCheckin

parser = argparse.ArgumentParser(description="Check in a maya file from commandline.")
parser.add_argument("scene_file", help="Path to the scene file.")
parser.add_argument("--settings_file", help="Override the path to the settings file.")

args = parser.parse_args()

clc = CommandLineCheckin(args.settings_file, "maya", args.scene_file)
clc.checkin()