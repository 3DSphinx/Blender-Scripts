#####This is script is coded to extract the shapekeys of the first item selected and export to .obj
#####  WARNING:PLEASE SAVE YOUR PROJECT BEFORE RUNNING THIS SCRIPT!!
#####  DISCLAIMER: Be aware that you use this script at your own risk the owner cannot be held responsible for any
#####              misuse or script problems. This comes without warranty of any kind.

##This is to transfer shapekeys from one model to another with the same vertices
import bpy

##get the two selected object first object is the reference for ShapeKey transfer and 
##second object getting the shape keys
try:
    refObj=bpy.context.selected_objects[0].name
    transferObj=bpy.context.selected_objects[1].name
        
    ##get the number of shapekeys
    refShapeKeys=len(bpy.data.meshes[refObj].shape_keys.key_blocks)
            
    ##let's make sure the vertex count is the same
    if len(bpy.context.selected_objects[1].data.vertices)==len(bpy.context.selected_objects[0].data.vertices):
            
        ##let's start the transfer process
        for sk in range(1,refShapeKeys):
            refShapeKeyNo=bpy.context.selected_objects[0].active_shape_key_index=sk
            ##Move ShapeKeys
            bpy.ops.object.shape_key_transfer()
        
    else:
        print("TRANSFER CANCELLED: Vertex count don't match")
except:
    print("Process failed! Make sure two items are selected")
