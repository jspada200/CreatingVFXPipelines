"""
Script to check in a maya file from commandline.
"""
import maya.standalone
maya.standalone.initialize()

import maya.cmds as cmds
import argparse
from JPipe.checkin_controllers.command_line_checkin import CommandLineCheckin

parser = argparse.ArgumentParser(description="Check in a maya file from commandline.")
parser.add_argument("scene_file", help="Path to the scene file.")
parser.add_argument("entity_type", help="The entity type to check in to.", choices=["asset", "shot"])
parser.add_argument("entity_name", help="The name of the entity to check in to.")
parser.add_argument("--settings_file",
                    help="Override the path to the settings file.")
parser.add_argument("--force", action="store_true", help="Force the checkin even if validations fail.")
parser.add_argument("--project_directory",
                    help="Override the project directory.",
                    default=cmds.workspace( q=True, dir=True ))

args = parser.parse_args()

if not args.settings_file:
    raise ValueError("No settings file found.")

clc = CommandLineCheckin(
    args.settings_file,
    "maya",
    args.scene_file,
    args.entity_type,
    args.entity_name,
    args.project_directory,
    force=args.force)
clc.checkin()