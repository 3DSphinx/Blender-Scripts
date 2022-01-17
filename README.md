# Blender-Scripts
Scripts that I created for Blender to help with my CG work

#####This is script is coded to extract the shapekeys of the first item selected and export to .obj
#####  WARNING:PLEASE SAVE YOUR PROJECT BEFORE RUNNING THIS SCRIPT!!
#####  DISCLAIMER: Be aware that you use this script at your own risk the owner cannot be held responsible for any
#####              misuse or script problems. This comes without warranty of any kind.


I created this for creating morphs for Reallusion Character Creator Software and iClone 7.

Blender_Batch_ShapeKey_Export.py - is for exporting all the Shapekeys in a Blender object in a obj format. The formating is focus on creating custom morphs for Reallusion Character Creator 3.

Usage:
Save your blender file before running the script being that the script locates the current working directory and create a new directory for storing the new exported Shape Keys. 
Select the object that you would like to export shape keys. If you run the script more than once it will overwrite anything in the directory created. 

Blender_Bach_ShapeKey_Transfer.py - is for transfering all the Shapekeys in a Blender object to another object with the same vertices as the original object. This tool was built
for users of Reallusion Character Creator 3 and iClone 7.
