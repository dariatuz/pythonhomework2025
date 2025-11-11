bl_info = {
    "name": "STP-FBX Simplifier",
    "blender": (4, 0, 0),
    "category": "Object",
    "version": (1, 2, 0),  # Bumped version to 1.2.0
    "author": "Maksim Lukinykh for Lunas",
    "description": "Automatically renames objects and assigns materials based on their names.",
}

import bpy
import re
import time

# Debug flag
DEBUG = True

# Global variable for the timer
rename_timer = None

def get_loaded_file():
    return bpy.data.filepath if bpy.data.is_saved else ""

def rename_objects():
    if not bpy.data.objects:
        return
    
    for obj in bpy.data.objects:
        # Skip objects that are directly in the Scene Collection (root collection)
        if not obj.users_collection or obj.users_collection[0].name == "Scene Collection":
            continue
        
        collection = obj.users_collection[0]
        parts = collection.name.split('_')
        prefix = parts[0] if len(parts) > 1 else ""
        suffix = parts[-1] if len(parts) > 1 else ""
        
        # Extract the unique part of the object name
        obj_name_parts = obj.name.split('_')
        if len(obj_name_parts) > 2:
            # If the object name has multiple parts, assume the middle part is the unique name
            unique_name = obj_name_parts[1]
        else:
            # If the object name has only one or two parts, use the first part as the unique name
            unique_name = obj_name_parts[0]
        
        # Fallback to a default name if the unique name is empty or invalid
        if not unique_name or unique_name in (prefix, suffix):
            unique_name = "Object"
        
        # Build the new name
        if prefix and suffix:
            new_name = f"{prefix}_{unique_name}_{suffix}"
        elif prefix:
            new_name = f"{prefix}_{unique_name}"
        elif suffix:
            new_name = f"{unique_name}_{suffix}"
        else:
            new_name = unique_name
        
        # Rename the object and its data if necessary
        if obj.name != new_name:
            if DEBUG:
                print(f"Renaming {obj.name} to {new_name}")
            obj.name = new_name
            if obj.data:
                obj.data.name = new_name
        
        # Assign materials based on the unique name (only if no materials exist)
        if not obj.data.materials:
            if "Sink" in unique_name or "sink" in unique_name:
                if DEBUG:
                    print(f"Assigning materials Sink1, Sink2 to {obj.name}")
                assign_material(obj, ["Sink1", "Sink2"])
            elif "Drain" in unique_name or "drain" in unique_name:
                if DEBUG:
                    print(f"Assigning material Drain1 to {obj.name}")
                assign_material(obj, ["Drain1"])

def assign_material(obj, material_names, clear_existing=True):
    if not obj or obj.type != 'MESH' or not obj.data or not hasattr(obj.data, "materials"):
        return
    
    if clear_existing:
        obj.data.materials.clear()
    
    for mat_name in material_names:
        mat = bpy.data.materials.get(mat_name)
        if mat is None:
            mat = bpy.data.materials.new(name=mat_name)
        obj.data.materials.append(mat)

# Throttle updates to once per second
last_update_time = 0

def update_handler(scene):
    global last_update_time
    current_time = time.time()
    if current_time - last_update_time > 1.0:  # Throttle to once per second
        last_update_time = current_time
        rename_objects()

def start_monitoring():
    global rename_timer
    if update_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(update_handler)
        print("[Stp-Fbx Simplifier] ✅ Monitoring started")
    if rename_timer is None:
        rename_timer = bpy.app.timers.register(rename_objects, first_interval=1.0)

def stop_monitoring():
    global rename_timer
    if update_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(update_handler)
    if rename_timer is not None:
        bpy.app.timers.unregister(rename_timer)
        rename_timer = None
        print("[Stp-Fbx Simplifier] ⛔ Monitoring stopped")

# New function to force material changes on selected objects
def force_material_changes(context):
    selected_objects = context.selected_objects
    if not selected_objects:
        print("No objects selected.")
        return
    
    for obj in selected_objects:
        if obj.users_collection:
            collection = obj.users_collection[0]
            parts = collection.name.split('_')
            prefix = parts[0] if len(parts) > 1 else ""
            suffix = parts[-1] if len(parts) > 1 else ""
            
            # Extract the unique part of the object name
            obj_name_parts = obj.name.split('_')
            if len(obj_name_parts) > 2:
                unique_name = obj_name_parts[1]
            else:
                unique_name = obj_name_parts[0]
            
            if not unique_name or unique_name in (prefix, suffix):
                unique_name = "Object"
            
            # Assign materials based on the unique name
            if "Sink" in unique_name or "sink" in unique_name:
                if DEBUG:
                    print(f"Assigning materials Sink1, Sink2 to {obj.name}")
                assign_material(obj, ["Sink1", "Sink2"])
            elif "Drain" in unique_name or "drain" in unique_name:
                if DEBUG:
                    print(f"Assigning material Drain1 to {obj.name}")
                assign_material(obj, ["Drain1"])

class StartOperator(bpy.types.Operator):
    bl_idname = "stp_fbx.start"
    bl_label = "Start"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        start_monitoring()
        return {'FINISHED'}

class StopOperator(bpy.types.Operator):
    bl_idname = "stp_fbx.stop"
    bl_label = "Stop"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        stop_monitoring()
        return {'FINISHED'}

class ForceMaterialsOperator(bpy.types.Operator):
    bl_idname = "stp_fbx.force_materials"
    bl_label = "Change Materials Anyway"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        force_material_changes(context)
        return {'FINISHED'}

class StpFbxPanel(bpy.types.Panel):
    bl_label = "STP-FBX Simplifier"
    bl_idname = "STP_FBX_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'STP-FBX'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Automatically rename objects and assign materials.")
        layout.operator("stp_fbx.start")
        layout.operator("stp_fbx.stop")
        layout.separator()
        layout.label(text="Force material changes on selected objects:")
        layout.operator("stp_fbx.force_materials")

def register():
    print("[Stp-Fbx Simplifier] Registering addon")
    bpy.utils.register_class(StartOperator)
    bpy.utils.register_class(StopOperator)
    bpy.utils.register_class(ForceMaterialsOperator)
    bpy.utils.register_class(StpFbxPanel)

def unregister():
    bpy.utils.unregister_class(StartOperator)
    bpy.utils.unregister_class(StopOperator)
    bpy.utils.unregister_class(ForceMaterialsOperator)
    bpy.utils.unregister_class(StpFbxPanel)
    stop_monitoring()
    print("[Stp-Fbx Simplifier] ❌ Addon unregistered")

if __name__ == "__main__":
    register()