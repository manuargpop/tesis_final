import bpy
import json

f = open('./scripts/datos_modelo.json')
data = json.load(f)

# Borrar los objetos
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# construir el modelo

bpy.context.scene.mblab_character_name = data['preset']
bpy.context.scene.mblab_use_eevee = True

bpy.ops.mbast.init_character()

if data['tpac'] == 'Adulto':
    bpy.context.object.character_age = data['edad']
    bpy.context.object.character_mass = data['grasa']
    bpy.context.object.character_tone = data['musculatura']
    bpy.context.object.Armpit_PosZ = data['subescapular']
    bpy.context.object.Abdomen_Mass = data['profundidad-abdominal']
    bpy.context.object.Elbows_Size = data['triceps']
    bpy.context.object.Arms_UpperarmMass = data['biceps']
    bpy.context.object.Torso_Vshape = data['cresta']
    bpy.context.object.Arms_UpperarmSize = data['pbr']
    bpy.context.object.Arms_ForearmSize = data['pbf']
    bpy.context.object.Wrists_Size = data['pm']
    bpy.context.object.Waist_Size = data['minimo-cintura']
    bpy.context.object.Stomach_Volume = data['profundidad-abdominal']
    bpy.context.object.Pelvis_Girth = data['pc']
    bpy.context.object.Arms_ForearmTone = data['brazo-musculatura']
    bpy.context.object.Arms_UpperarmTone = data['brazo-musculatura']
elif data['tpac'] == 'Atleta':
    bpy.context.object.character_mass = data['grasa']
    bpy.context.object.character_tone = data['musculatura']
    bpy.context.object.Arms_ForearmTone = data['brazo-musculatura']
    bpy.context.object.Arms_UpperarmTone = data['brazo-musculatura']
    bpy.context.object.character_age = data['edad']
    bpy.context.object.Stomach_Volume = data['profundidad-abdominal']
    bpy.context.object.Arms_ForearmLength = data['lad']
    bpy.context.object.Elbows_Size = data['triceps']
    bpy.context.object.Armpit_PosZ = data['subescapular']
    bpy.context.object.Arms_UpperarmMass = data['biceps']
    bpy.context.object.Torso_Vshape = data['cresta']
    bpy.context.object.Shoulders_Size = data['supraespinal']
    bpy.context.object.Legs_UpperlegsTone = data['muslo-frontal']
    bpy.context.object.Legs_LowerlegsTone = data['pantorrilla']
    bpy.context.object.Waist_Size = data['pm']
    # pal cabezon  bpy.context.object.data['pcefalico']
    bpy.context.object.Chest_Girth = data['ptorax']
    bpy.context.object.Neck_Size = data['pcuello']
    bpy.context.object.Legs_UpperlegLength = data['pmuslomedio']
    bpy.context.object.Legs_CalfGirth = data['ppantorrilla']
    bpy.context.object.Legs_AnkleSize =  data['pmtobillo']
    bpy.context.object.Arms_UpperarmLength = data['acromialeradiale']
    bpy.context.object.Arms_ForearmSize = data['radiale_stylion']
    bpy.context.object.Hands_Length = data['midstylion_dactylion']
    bpy.context.object.Torso_Length = data['altura_iliospinale']
    #bpy.context.object. = data['altura-tronchanterion']
    bpy.context.object.Legs_UpperlegSize = data['tronchanterion_tl']
    bpy.context.object.Legs_LowerlegSize = data['altura_tl']
    bpy.context.object.Shoulders_Length = data['diametro_biacromial']
    bpy.context.object.Waist_Size = data['diametro_biliocristal']
    bpy.context.object.Feet_SizeX = data['largo_pie']
    bpy.context.object.Torso_SizeX = data['anchura_torax']
    bpy.context.object.Torso_SizeY = data['profundidad_toraxt']
    bpy.context.object.Elbows_Size = data['diametro_bch']
    bpy.context.object.Legs_KneeSize = data['diametro_bcf']



bpy.ops.export_scene.obj(filepath='C:/Users/Usuario/PycharmProjects/Tesis/test/exported_model.obj')
