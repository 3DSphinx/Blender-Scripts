#####This is script is coded to extract the shapekeys of the first item selected and export to .obj
#####  WARNING:PLEASE SAVE YOUR PROJECT BEFORE RUNNING THIS SCRIPT!!
#####  DISCLAIMER: Be aware that you use this script at your own risk the owner cannot be held responsible for any
#####              misuse or script problems. This comes without warranty of any kind.

import bpy
import os

##get the selected object
try:
    exp_Object=str(bpy.context.selected_objects[0].data.name)
    
    newDirName="Exported_ShapeKeys";
    ##Let's make sure object is selected
    if(exp_Object!=None):
        ##get the blend file save location and create a folder
        save_Loc=os.getcwd()
        
        ##make a new directory
        try:
            os.mkdir(newDirName)
        except FileExistsError:
            print("Directory already exist skipping creation.")
            
        
        shapeKey= bpy.data.meshes[exp_Object].shape_keys
        print(shapeKey)
            


        ##let's loop through each shape_key
        loop=len(shapeKey.key_blocks)
        if loop>1:
            ##start the loop at 1 instead of zerp
            for shape in range(1,loop):
                ##this will set the value and then export out
                bpy.data.meshes[exp_Object].shape_keys.key_blocks[shape].value=1;
                bpy.ops.export_scene.obj(filepath=save_Loc+"//"+newDirName+"//"+bpy.data.meshes[exp_Object].shape_keys.key_blocks[shape].name+".obj",check_existing=False,use_selection=True,use_materials=False,use_vertex_groups=True,keep_vertex_order=True)
                ##reset shapekey
                bpy.data.meshes[exp_Object].shape_keys.key_blocks[shape].value=0
        else:
            print("Shapekeys not found.")
except AttributeError:
    print("Script stopped object not selected.")
