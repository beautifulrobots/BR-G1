#BEAUTIFUL ROBOTS GENERATOR ONE BY DIEGO BELTRAN v31 27/03/2023 ALL RIGHTS RESERVED

import maya.cmds as cmds
import random
import mtoa.aovs as aovs
import maya.mel as mel

# INTERFACE 01 -----------------------------------------------------------------------------------------------------------------

if cmds.window("BRGWindow2",exists = True):
    
    cmds.deleteUI("BRGWindow2")

myWindow = cmds.window("BRGWindow2",title = "BR-G1", width = 300, height = 500, sizeable = True)

scrollLayout = cmds.scrollLayout(
	horizontalScrollBarThickness=16,
	verticalScrollBarThickness=16)

cmds. columnLayout(columnAttach = ("both", 5), rowSpacing = 10, columnWidth = 400)

cmds.separator(height = 5)

cmds.text(label = "BR-G1", fn = "boldLabelFont")
cmds.text(label = "Coded by @beautiful_robots")

cmds.text(label = "CH Shapes", al = "left")

shapesGroup1 = cmds.checkBoxGrp("shapesGroupOne", numberOfCheckBoxes=4, labelArray4=['Cube', 'Sphere', 'Cylinder','Cone'], cl4 = ['left', 'left', 'left','left'], v1 = True)

shapesGroup2 = cmds.checkBoxGrp("shapesGroupTwo",numberOfCheckBoxes = 2, labelArray2=['Torus','Pyramid'], cl2 = ['left','left'])

cmds.text(label = "CH Shapes Iterations", al = "left")

inputTextIterations = cmds.intField("inputTextIterations2", v = 3)

cmds.text(label = "BG Iterations", al = "left")

inputTextIterationsBG = cmds.intField("inputTextIterationsBG2", v = 0)

cmds.text(label = "CH Scale", al = "left")

inputTextScale = cmds.floatField("inputTextScale2", v = 1)

cmds.text(label = "CH Height", al = "left", ann="Type between 0 and 6")

sliderHeight = cmds.floatSliderGrp("sliderHeight2",min = -8.0, max = 8, f = True, cl2 = ("left","left"))

cmds.text(label = "CH Elemental Transforms", al = "left")

changePerspective = cmds.checkBox("changePerspective2", label='Cubism Perspective', align='left', onc = "change_perspective_function(1)", ofc = "change_perspective_function(0)")

# FUNCTIONS ----------------------------------------------------------------------------------------------------------------- 

def shape_cleaner_function(*args):
       
    transforms =  cmds.ls(type='transform')
    
    deleteList = []
    
    for j in transforms:
        
        if cmds.nodeType(j) == 'transform':
            
            children = cmds.listRelatives(j, c=True) 
            
            if children == None:

                deleteList.append(j)
                
    cmds.delete(deleteList)
    
    for i in cmds.ls(type = "transform"):
        
        cmds.select(i)
        
        cmds.delete(ch=1)
        
        cmds.select(cl = True)
        
def change_perspective_function(*args):
    
    inputPerspective = cmds.checkBox("changePerspective2", q = True, v = 1)
    
    if inputPerspective == 1:
    
        persp = random.uniform(-360.0,360.0)
        
	for i in range (0, 360, 45):
            
            if persp <= i and persp > i-45:
                
                persp = i-22.5
                
            elif persp >= i and persp < i+45:
                
                persp = i+22.5
        
    if inputPerspective == 0:
    
        persp = 0
    
    return persp
    
def shape_creator_function(iterations,displacement,shapeSelection,secondShapeSelection,randPerspective):
    
    inputPerspective = cmds.checkBox("changePerspective2", q = True, v = 1)
    
    if randPerspective == 1:
    
        persp = random.uniform(-360.0,360.0)
            
        for i in range (0, 360, 45):
            
            if persp <= i and persp > i-45:
                
                persp = i-22.5
                
            elif persp >= i and persp < i+45:
                
                persp = i+22.5
        
    if randPerspective == 0:
    
        persp = 0
        
    perspective = change_perspective_function()
     
    for i in range(0,int(iterations)):
          
        randNumRadius = random.uniform(4, 8)
        randNumXRot = random.uniform(-45, 45)
        randNumXRot2 = random.uniform(-45, 45)
        randNumXZ = random.uniform(-8, 8)
        randNumXZ2 = random.uniform(-8, 8)
        randNumY = random.uniform(-16, 8)
        randNumY2 = random.uniform(-16, 8)
        randNumZ = random.uniform(-8, 8)
        randWidth = random.uniform(1, 16)
        randWidth2 = random.uniform(1, 16)
        randHeight = random.uniform(1, 16)
        randDepth = random.uniform(1, 16)
        randNumRadius = random.uniform(1, 8)
        randNumCylinderRadius = random.uniform(4, 8)
        randNumCylinderHeight = random.uniform(1, 16)
        randNumConeRadius = random.uniform(4, 8)
        randNumConeHeight = random.uniform(4, 16)
        randNumZRot = random.uniform(-45, 45)
        randNumSelection = round(random.uniform(1, 2))
        randNumSelection2 = round(random.uniform(1, 2))
        randNumTorusRadius = random.uniform(4, 8)
        randSectionRadius = random.uniform(1, 4)
                
        if cmds.checkBoxGrp('shapesGroupOne', q=True, value1=True) or shapeSelection == 1 or secondShapeSelection == 1:
                
            cmds.polyCube(name = "Cubo_centro" + str(i), d = randDepth, h = randHeight, w = randWidth,sx = 8, sy = 8, sz = 8) 
            
            if displacement >= 0:
    
                cmds.setAttr( 'Cubo_centro' + str(i) + '.translateZ', randNumXZ  - displacement/4)
                cmds.setAttr( 'Cubo_centro' + str(i) + '.translateY', randNumY  + (displacement*i))
                cmds.setAttr( 'Cubo_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cubo_centro' + str(i) + '.rotateX', randNumXRot )
                
            else:
                
                cmds.setAttr( 'Cubo_centro' + str(i) + '.translateZ', randNumXZ  + (-displacement)*i)
                cmds.setAttr( 'Cubo_centro' + str(i) + '.translateY', randNumY) 
                cmds.setAttr( 'Cubo_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cubo_centro' + str(i) + '.rotateX', randNumXRot )   
                       
            cmds.polyCube(name = "Cubo_lateral" + str(i), d = randDepth, h = randHeight, w = randWidth,sx = 8, sy = 8, sz = 8)
    
            if displacement >= 0:
    
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.translateX', randNumXZ  - displacement/4)
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.translateY', randNumY  + (displacement*i))   
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.rotateX', randNumXRot )
                
            else:
                
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.translateX', randNumXZ  + (-displacement)*i)
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.translateY', randNumY)
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cubo_lateral' + str(i) + '.rotateX', randNumXRot )
    
           
            cmds.setAttr('Cubo_centro'+ str(i) + '.displaySmoothMesh', 2)
            cmds.setAttr('Cubo_lateral' + str(i) + '.displaySmoothMesh', 2)


            boundingBoxCuboCentro = cmds.xform("Cubo_centro" + str(i), q=True, bb=True, ws=True)
            x1Min = boundingBoxCuboCentro[0] - randNumXZ
            x1Max = boundingBoxCuboCentro[3] - randNumXZ
                
            boundingBoxCuboLateral = cmds.xform("Cubo_lateral" + str(i), q=True, bb=True, ws=True)
            x2Min = boundingBoxCuboLateral[0]
            x2Max = boundingBoxCuboLateral[3]
                
            if x1Max > x2Min and x1Min < x2Max:
                
                cmds.polyBoolOp( "Cubo_centro" + str(i), "Cubo_lateral" + str(i), op=1, n="Cubo_merged" + str(i)) 
    
                cmds.setAttr( 'Cubo_merged' + str(i) + '.rotateY', 0 - (perspective/2) - (persp/2))
                
                cmds.setAttr("Cubo_merged" + str(i) + ".inheritsTransform", 0)
                
                cmds.polyRetopo("Cubo_merged" + str(i), faceUniformity = 0, targetFaceCount = 500)
                
                cmds.polyAutoProjection('Cubo_merged' + str(i) + '.f[*]')
                
                cmds.setAttr("Cubo_merged" + str(i) + '.displaySmoothMesh', 2)   
                
                
            
        

            cmds.xform("Cubo_centro"+ str(i), ws = True, piv = (0,0,0)) 
            cmds.xform("Cubo_lateral"+ str(i), ws = True, piv = (0,0,0))


            cmds.setAttr( 'Cubo_centro' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Cubo_lateral' + str(i) + '.rotateY',0 + perspective + persp)
        

            cmds.xform("Cubo_centro"+ str(i),cp=True) 
            cmds.xform("Cubo_lateral"+ str(i), cp=True)
            
            
        if cmds.checkBoxGrp('shapesGroupOne', q=True, value2=True) or shapeSelection == 2 or secondShapeSelection == 2:
        
            cmds.polySphere(name = "Esfera_centro" + str(i), r = randNumRadius, sx = 8, sy = 8)      
            
            if displacement >= 0:
    
                cmds.setAttr( 'Esfera_centro' + str(i) + '.translateZ', randNumXZ  - displacement/4)
                cmds.setAttr( 'Esfera_centro' + str(i) + '.translateY', randNumY + (displacement*i))
                cmds.setAttr( 'Esfera_centro' + str(i) + '.rotateY', 0 + perspective + persp)
    
            else:
                
                cmds.setAttr( 'Esfera_centro' + str(i) + '.translateZ', randNumXZ  + (-displacement)*i)
                cmds.setAttr( 'Esfera_centro' + str(i) + '.translateY', randNumY)
                cmds.setAttr( 'Esfera_centro' + str(i) + '.rotateY', 0 + perspective + persp)
            
            cmds.polySphere(name = "Esfera_lateral" + str(i), r = randNumRadius, sx = 8, sy = 8)
            
            if displacement >= 0:
    
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.translateX', randNumXZ - displacement/4)
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.translateY', randNumY  + (displacement*i))
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.rotateY', 0 + perspective + persp)
                
            else:
                
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.translateX', randNumXZ + (-displacement)*i)
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.translateY', randNumY)
                cmds.setAttr( 'Esfera_lateral' + str(i) + '.rotateY', 0 + perspective + persp)
                
            cmds.xform("Esfera_lateral"+ str(i), ws = True, piv = (0,0,0))  
            cmds.xform("Esfera_centro"+ str(i), ws = True, piv = (0,0,0))
            
            cmds.setAttr( 'Esfera_centro' + str(i) + '.rotateY', -45 - perspective - persp)
            cmds.setAttr( 'Esfera_lateral' + str(i) + '.rotateY', -45 - perspective - persp)
            
            cmds.xform("Esfera_lateral"+ str(i), cp=True)  
            cmds.xform("Esfera_centro"+ str(i),cp=True) 
            
            cmds.setAttr('Esfera_centro'+ str(i) + '.displaySmoothMesh', 2)  
            cmds.setAttr('Esfera_lateral' + str(i) + '.displaySmoothMesh', 2)
            
            
        if cmds.checkBoxGrp('shapesGroupOne', q=True, value3=True) or shapeSelection == 3 or secondShapeSelection == 3:
                
            cmds.polyCylinder(name = "Cilindro_centro" + str(i), r = randNumCylinderRadius, h = randNumCylinderHeight,sx = 8, sy = 8, sz = 8)
              
            if displacement >= 0:
    
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.translateZ', randNumXZ2  - displacement/4)
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.translateY', randNumY2  + (displacement*i))
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.rotateX', randNumXRot )
                
            else:
                
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.translateZ', randNumXZ2  + (-displacement)*i)
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.translateY', randNumY2) 
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cilindro_centro' + str(i) + '.rotateX', randNumXRot )   
                       
            cmds.polyCylinder(name = "Cilindro_lateral" + str(i), r = randNumCylinderRadius, h = randNumCylinderHeight,sx = 8, sy = 8, sz = 8)
    
            if displacement >= 0:
    
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.translateX', randNumXZ2  - displacement/4)
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.translateY', randNumY2  + (displacement*i))   
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.rotateX', randNumXRot )
                
            else:
                
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.translateX', randNumXZ2  + (-displacement)*i)
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.translateY', randNumY2)
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cilindro_lateral' + str(i) + '.rotateX', randNumXRot )
    
           
            cmds.setAttr('Cilindro_centro'+ str(i) + '.displaySmoothMesh', 2)
            cmds.setAttr('Cilindro_lateral' + str(i) + '.displaySmoothMesh', 2)
               

            cmds.xform("Cilindro_centro"+ str(i), ws = True, piv = (0,0,0)) 
            cmds.xform("Cilindro_lateral"+ str(i), ws = True, piv = (0,0,0))


            cmds.setAttr( 'Cilindro_centro' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Cilindro_lateral' + str(i) + '.rotateY',0 + perspective + persp)
        

            cmds.xform("Cilindro_centro"+ str(i),cp=True) 
            cmds.xform("Cilindro_lateral"+ str(i), cp=True)
            
        if cmds.checkBoxGrp('shapesGroupOne', q=True, value4=True) or shapeSelection == 4 or secondShapeSelection == 4:
                
            cmds.polyCone(name = "Cono_centro" + str(i), r = randNumConeRadius, h = randNumConeHeight,sx = 4, sy = 4, sz = 4)
            
            if randNumSelection == 1:
            
                randSelection = randNumXZ
                randSelection2 = randNumY2
                
            if randNumSelection == 2:
            
                randSelection = randNumXZ2
                randSelection2 = randNumY2
              
            if displacement >= 0:
    
                cmds.setAttr( 'Cono_centro' + str(i) + '.translateZ', randSelection  - displacement/4)
                cmds.setAttr( 'Cono_centro' + str(i) + '.translateY', randSelection2  + (displacement*i))
                cmds.setAttr( 'Cono_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cono_centro' + str(i) + '.rotateX', randNumXRot )
                
                
            else:
                
                cmds.setAttr( 'Cono_centro' + str(i) + '.translateZ', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Cono_centro' + str(i) + '.translateY', randSelection2) 
                cmds.setAttr( 'Cono_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cono_centro' + str(i) + '.rotateX', randNumXRot )
                
                       
            cmds.polyCone(name = "Cono_lateral" + str(i), r = randNumConeRadius, h = randNumConeHeight,sx = 4, sy = 4, sz = 4)
    
            if displacement >= 0:
    
                cmds.setAttr( 'Cono_lateral' + str(i) + '.translateX', randSelection  - displacement/4)
                cmds.setAttr( 'Cono_lateral' + str(i) + '.translateY', randSelection2  + (displacement*i))   
                cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateX', randNumXRot )
                
                
            else:
                
                cmds.setAttr( 'Cono_lateral' + str(i) + '.translateX', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Cono_lateral' + str(i) + '.translateY', randSelection2)
                cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateX', randNumXRot )
                
    
           
            cmds.setAttr('Cono_centro'+ str(i) + '.displaySmoothMesh', 2)
            cmds.setAttr('Cono_lateral' + str(i) + '.displaySmoothMesh', 2)
               

            cmds.xform("Cono_centro"+ str(i), ws = True, piv = (0,0,0)) 
            cmds.xform("Cono_lateral"+ str(i), ws = True, piv = (0,0,0))


            cmds.setAttr( 'Cono_centro' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Cono_lateral' + str(i) + '.rotateZ', randNumZRot )
            cmds.setAttr( 'Cono_centro' + str(i) + '.rotateZ', -randNumZRot )
        

            cmds.xform("Cono_centro"+ str(i),cp=True) 
            cmds.xform("Cono_lateral"+ str(i), cp=True)
            
            
        if cmds.checkBoxGrp('shapesGroupTwo', q=True, value1=True) or shapeSelection == 5 or secondShapeSelection == 5:
                
            cmds.polyTorus(name = "Toroide_centro" + str(i), r = randNumTorusRadius,sr = randSectionRadius, sx = 8, sy = 8)
            
            if randNumSelection == 1:
            
                randSelection = randNumXZ
                randSelection2 = randNumY2
                
            if randNumSelection == 2:
            
                randSelection = randNumXZ2
                randSelection2 = randNumY2
              
            if displacement >= 0:
    
                cmds.setAttr( 'Toroide_centro' + str(i) + '.translateZ', randSelection  - displacement/4)
                cmds.setAttr( 'Toroide_centro' + str(i) + '.translateY', randSelection2  + (displacement*i))
                cmds.setAttr( 'Toroide_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Toroide_centro' + str(i) + '.rotateX', randNumXRot2 )
                
            else:
                
                cmds.setAttr( 'Toroide_centro' + str(i) + '.translateZ', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Toroide_centro' + str(i) + '.translateY', randSelection2) 
                cmds.setAttr( 'Toroide_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Toroide_centro' + str(i) + '.rotateX', randNumXRot2 )  
                       
            cmds.polyTorus(name = "Toroide_lateral" + str(i), r = randNumTorusRadius,sr = randSectionRadius ,sx = 8, sy = 8)
    
            if displacement >= 0:
    
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.translateX', randSelection  - displacement/4)
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.translateY', randSelection2  + (displacement*i))   
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.rotateX', randNumXRot2 )
                
            else:
                
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.translateX', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.translateY', randSelection2)
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Toroide_lateral' + str(i) + '.rotateX', randNumXRot2 )
    
           
            cmds.setAttr('Toroide_centro'+ str(i) + '.displaySmoothMesh', 2)
            cmds.setAttr('Toroide_lateral' + str(i) + '.displaySmoothMesh', 2)
               

            cmds.xform("Toroide_centro"+ str(i), ws = True, piv = (0,0,0)) 
            cmds.xform("Toroide_lateral"+ str(i), ws = True, piv = (0,0,0))


            cmds.setAttr( 'Toroide_centro' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Toroide_lateral' + str(i) + '.rotateY',0 + perspective + persp)
        

            cmds.xform("Toroide_centro"+ str(i),cp=True) 
            cmds.xform("Toroide_lateral"+ str(i), cp=True)
            
        if cmds.checkBoxGrp('shapesGroupTwo', q=True, value2=True) or shapeSelection == 6 or secondShapeSelection == 6:

            cmds.polyPyramid(name = "Piramide_centro" + str(i), numberOfSides=4, sideLength=randWidth2, subdivisionsCaps=4, subdivisionsHeight=4)
            
            if randNumSelection == 1:
            
                randSelection = randNumXZ
                randSelection2 = randNumY2
                
            if randNumSelection == 2:
            
                randSelection = randNumXZ2
                randSelection2 = randNumY2
              
            if displacement >= 0:
    
                cmds.setAttr( 'Piramide_centro' + str(i) + '.translateZ', randSelection  - displacement/4)
                cmds.setAttr( 'Piramide_centro' + str(i) + '.translateY', randSelection2  + (displacement*i))
                cmds.setAttr( 'Piramide_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Piramide_centro' + str(i) + '.rotateX', randNumXRot2 )
                
            else:
                
                cmds.setAttr( 'Piramide_centro' + str(i) + '.translateZ', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Piramide_centro' + str(i) + '.translateY', randSelection2) 
                cmds.setAttr( 'Piramide_centro' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Piramide_centro' + str(i) + '.rotateX', randNumXRot2 )  
                       
            cmds.polyPyramid(name = "Piramide_lateral" + str(i), numberOfSides=4, sideLength=randWidth2, subdivisionsCaps=4, subdivisionsHeight=4)
    
            if displacement >= 0:
    
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.translateX', randSelection  - displacement/4)
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.translateY', randSelection2  + (displacement*i))   
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.rotateX', randNumXRot2 )
                
            else:
                
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.translateX', randSelection  + (-displacement)*i)
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.translateY', randSelection2)
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.rotateY', 45 + perspective + persp)
                cmds.setAttr( 'Piramide_lateral' + str(i) + '.rotateX', randNumXRot2 )
    
           
            cmds.setAttr('Piramide_centro'+ str(i) + '.displaySmoothMesh', 2)
            cmds.setAttr('Piramide_lateral' + str(i) + '.displaySmoothMesh', 2)
               

            cmds.xform("Piramide_centro"+ str(i), ws = True, piv = (0,0,0)) 
            cmds.xform("Piramide_lateral"+ str(i), ws = True, piv = (0,0,0))


            cmds.setAttr( 'Piramide_centro' + str(i) + '.rotateY',0 + perspective + persp)
            cmds.setAttr( 'Piramide_lateral' + str(i) + '.rotateY',0 + perspective + persp)
        

            cmds.xform("Piramide_centro"+ str(i),cp=True) 
            cmds.xform("Piramide_lateral"+ str(i), cp=True)
 

def shape_group_function(scl):
    
    shapes = ['Cubo_centro*', 'Cubo_lateral*', 'Esfera_lateral*', 'Esfera_centro*', 'Cubo_merged*', 
              'Cilindro_centro*', 'Cilindro_lateral*', 'Cono_centro*', 'Cono_lateral*', 'Toroide_centro*', 
              'Toroide_lateral*', 'Piramide_centro*', 'Piramide_lateral*']
    
    cmds.select(clear=True)
    
    for shape in shapes:
        if cmds.objExists(shape):
            cmds.select(shape, add=True)
            
    groupVar = cmds.group(n="CH*")
    
    cmds.setAttr("CH*"+".rotateY", 50)
    cmds.manipPivot(o=[0.0, 0.0, 0.0])
    boundingBox = cmds.xform("CH*", q=True, bb=True, ws=True)
    cmds.move(boundingBox[1], "CH*"+'.scalePivot', y=True, absolute=True)
    cmds.move(boundingBox[1], "CH*"+'.rotatePivot', y=True, absolute=True)
    cmds.setAttr("CH*"+'.translateY', -boundingBox[1])
    cmds.scale(scl, scl, scl, "CH*")
    
    
def BG_shape_function(BG_iterations):
    
    for j in range(BG_iterations):
        # Generate random dimensions and shape
        randShape = random.choice([cmds.polySphere, cmds.polyCube, cmds.polyCylinder, cmds.polyCone])
        randArgs = [random.uniform(0.1, 80) for _ in range(randShape.__code__.co_argcount - 2)]
        randMeshName = f"BG_{randShape.__name__}{j}"
        
        # Create shape
        mesh_type = randShape(n=randMeshName, *randArgs, sx=8, sy=8, sz=8)
        
        # Generate random selection
        randSelection = random.choice([1, 2, 3, 4, 5])
        
        # Get bounding boxes
        boundingBoxCH = cmds.xform("CH*", q=True, bb=True, ws=True)
        boundingBoxMeshType = cmds.xform(mesh_type, q=True, bb=True, ws=True)
        
        # Translate shape
        polyEdgeCH = boundingBoxCH[randSelection - 1]
        polyEdgeMeshType = boundingBoxMeshType[randSelection % 6]
        axis = "XYZ"[randSelection % 3]
        offset = -polyEdgeMeshType + (polyEdgeCH/2) + (polyEdgeCH/4)
        cmds.move(offset, f"{mesh_type[0]}*{'.scalePivot, .rotatePivot'}", **{f"{axis}":True, "absolute":True})
        
        # Set displaySmoothMesh attribute
        cmds.setAttr(mesh_type[0] + '.displaySmoothMesh', 2)
        
def BG_shape_group_function():
       
    BGlist = cmds.ls('BG_Esfera*','BG_Cubo*','BG_Cilindro*','BG_Cono*')
    cmds.select(BGlist)
    BGgroupVar = cmds.group(n= "BG")
    
    cmds.manipPivot(o = [0.0,0.0,0.0])
    
    pivotOrientation = cmds.manipPivot(q=True, o=True)[0]

    BGboundingBox = cmds.xform("BG", q=True, bb=True, ws=True)
    
    cmds. move(BGboundingBox[1], "BG"+ '.scalePivot', y=True, absolute=True)
    cmds. move(BGboundingBox[1], "BG"+ '.rotatePivot', y=True, absolute=True)

def shape_color_function():

    aovs.AOVInterface().addAOV("ambientOcclusion")
    aovs.AOVInterface().addAOV("utility")
    aovs.AOVInterface().addAOV("specular")
    aovs.AOVInterface().addAOV("diffuse")
    
    tmp1 = random.uniform(0.0,1.0)
    tmp2 = random.uniform(0.0,1.0)
    tmp3 = random.uniform(0.0,1.0)
    
    # CH COLOR
    
    shd = cmds.shadingNode('aiStandardSurface', name="shape_color", asShader=True)
    shdSG = cmds.sets(name='%sSG' % shd, empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr('%s.outColor' % shd, '%s.surfaceShader' % shdSG)
    
    shdLayeredTexture = cmds.shadingNode('layeredTexture', name="layeredTexture", asShader=True)
    cmds.connectAttr(shdLayeredTexture + '.outColor', shd + '.baseColor')
    
    shdWriteColor01 = cmds.shadingNode('aiWriteColor', name="writeColor01", asShader=True)
    cmds.setAttr(shdLayeredTexture + '.inputs[0].blendMode', 1)
   
    shdWriteColor02 = cmds.shadingNode('aiWriteColor', name="writeColor02", asShader=True)
    cmds.setAttr(shdLayeredTexture + '.inputs[1].blendMode', 0)
    
    cmds.connectAttr(shdWriteColor01 + '.outColor', shdLayeredTexture + '.inputs[0].color')
    cmds.connectAttr(shdWriteColor02 + '.outColor', shdLayeredTexture + '.inputs[1].color')
    
    shdAmbientOcclusion = cmds.shadingNode('aiAmbientOcclusion', name="ambientOcclusion", asShader=True)
    cmds.connectAttr(shdAmbientOcclusion + '.outColor', shdWriteColor01 + '.input')
    
    shdUtility = cmds.shadingNode('aiUtility', name="utility", asShader=True)
    cmds.setAttr(shdUtility + '.shadeMode', 2)
    cmds.setAttr(shdUtility + '.colorMode', 21)
    cmds.connectAttr(shdUtility + '.outColor', shdWriteColor02 + '.input')
    
    shdRamp = cmds.shadingNode('ramp', name="ramp", asShader=True)
    cmds.setAttr(shdRamp + '.type', 1)
    cmds.setAttr(shdRamp + '.colorEntryList[1].color', tmp1,tmp2,tmp3,type = 'double3')
    cmds.setAttr(shdRamp + '.colorEntryList[1].position', 0.75)
    cmds.setAttr(shdRamp + '.colorEntryList[0].color', 1-tmp1,1-tmp2,1-tmp3,type = 'double3')
    cmds.setAttr(shdRamp + '.colorEntryList[0].position', 0.25)

    cmds.connectAttr(shdRamp + '.outColor', shdWriteColor01 + '.beauty')
    cmds.connectAttr(shdRamp + '.outColor', shdWriteColor02 + '.beauty')
    
    shdSetRange = cmds.shadingNode('setRange', name="setRange", asShader=True)
    cmds.setAttr(shdSetRange + '.oldMaxX', 8.5)
    cmds.setAttr(shdSetRange + '.oldMaxY', 8.5)
    cmds.setAttr(shdSetRange + '.oldMaxZ', 8.5)
    cmds.connectAttr(shdSetRange + '.outValueX', shdRamp + '.uvCoord.vCoord', f = True)
    
    shdSurfaceLuminance = cmds.shadingNode('surfaceLuminance', name="surfaceLuminance", asShader=True)
    cmds.connectAttr(shdSurfaceLuminance + '.outValue', shdSetRange + '.value.valueX')
    
    # BG COLOR
    
    shdBG = cmds.shadingNode('aiStandardSurface', name="BG_shape_color", asShader=True)
    BGshdSG = cmds.sets(name='%sSG' % shdBG, empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr('%s.outColor' % shdBG, '%s.surfaceShader' % BGshdSG)
    cmds.setAttr((shdBG + '.specular'), 0)
    
    BGshdLayeredTexture = cmds.shadingNode('layeredTexture', name="BG_layeredTexture", asShader=True)
    cmds.connectAttr(BGshdLayeredTexture + '.outColor', shdBG + '.baseColor')
    
    BGshdWriteColor01 = cmds.shadingNode('aiWriteColor', name="BG_writeColor01", asShader=True)
    cmds.setAttr(BGshdLayeredTexture + '.inputs[0].blendMode', 1)
   
    BGshdWriteColor02 = cmds.shadingNode('aiWriteColor', name="BG_writeColor02", asShader=True)
    cmds.setAttr(BGshdLayeredTexture + '.inputs[1].blendMode', 0)
    
    cmds.connectAttr(BGshdWriteColor01 + '.outColor', BGshdLayeredTexture + '.inputs[0].color')
    cmds.connectAttr(BGshdWriteColor02 + '.outColor', BGshdLayeredTexture + '.inputs[1].color')
    
    BGshdAmbientOcclusion = cmds.shadingNode('aiAmbientOcclusion', name="BG_ambientOcclusion", asShader=True)
    cmds.connectAttr(BGshdAmbientOcclusion + '.outColor', BGshdWriteColor01 + '.input')
    
    BGshdUtility = cmds.shadingNode('aiUtility', name="BG_utility", asShader=True)
    cmds.setAttr(BGshdUtility + '.shadeMode', 2)
    cmds.setAttr(BGshdUtility + '.colorMode', 21)
    cmds.connectAttr(BGshdUtility + '.outColor', BGshdWriteColor02 + '.input')
    
    BGshdRamp = cmds.shadingNode('ramp', name="BG_ramp", asShader=True)
    cmds.setAttr(BGshdRamp + '.type', 1)
    
    minValue = min([tmp1,tmp2,tmp3])
    
    if minValue == tmp1:
        
        tmp1Comp = tmp1
        tmp2Comp = tmp2
        tmp3Comp = 1-tmp3
        
        cmds.setAttr(BGshdRamp + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    if minValue == tmp2:
        
        tmp1Comp = 1-tmp1
        tmp2Comp = tmp2
        tmp3Comp = tmp3
        
        cmds.setAttr(BGshdRamp + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    if minValue == tmp3:
        
        tmp1Comp = tmp1
        tmp2Comp = 1-tmp2
        tmp3Comp = tmp3
        
        cmds.setAttr(BGshdRamp + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    cmds.setAttr(BGshdRamp + '.colorEntryList[0].color', 1-tmp1Comp,1-tmp2Comp,1-tmp3Comp,type = 'double3')
    
    cmds.setAttr(BGshdRamp + '.colorEntryList[1].position', 0.75)
    cmds.setAttr(BGshdRamp + '.colorEntryList[0].position', 0.25)

    cmds.connectAttr(BGshdRamp + '.outColor', BGshdWriteColor01 + '.beauty')
    cmds.connectAttr(BGshdRamp + '.outColor', BGshdWriteColor02 + '.beauty')
    
    BGshdSetRange = cmds.shadingNode('setRange', name="BG_setRange", asShader=True)
    cmds.setAttr(BGshdSetRange + '.oldMaxX', 8.5)
    cmds.setAttr(BGshdSetRange + '.oldMaxY', 8.5)
    cmds.setAttr(BGshdSetRange + '.oldMaxZ', 8.5)
    cmds.connectAttr(BGshdSetRange + '.outValueX', BGshdRamp + '.uvCoord.vCoord', f = True)
    
    BGshdSurfaceLuminance = cmds.shadingNode('surfaceLuminance', name="BG_surfaceLuminance", asShader=True)
    cmds.connectAttr(BGshdSurfaceLuminance + '.outValue', BGshdSetRange + '.value.valueX')
    
    # AOVs
    
    shdAOVAmbientOcclusion = cmds.createNode('aiAOV', name="AOV_ambientOcclusion", skipSelect=True)
    cmds.connectAttr(shdAmbientOcclusion + '.outColor', 'aiAOV_ambientOcclusion.defaultValue')
    
    shdAOVUtility = cmds.createNode('aiAOV', name="AOV_utility", skipSelect=True)
    cmds.connectAttr(shdUtility + '.outColor', 'aiAOV_utility.defaultValue')
    
    try:cmds.sets('Esfera_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Esfera_lateral*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cubo_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cubo_lateral*', e=True, forceElement=shdSG)
    except: pass
    try: cmds.sets('Cubo_merged*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cilindro_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cilindro_lateral*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cono_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Cono_lateral*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Toroide_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Toroide_lateral*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Piramide_centro*', e=True, forceElement=shdSG)
    except: pass
    try:cmds.sets('Piramide_lateral*', e=True, forceElement=shdSG)
    except: pass
    
    try:cmds.sets('BG_Base', e=True, forceElement=BGshdSG)
    except: pass
    try:cmds.sets("BG_Esfera*", e=True, forceElement=BGshdSG)
    except: pass
    try:cmds.sets("BG_Cubo*", e=True, forceElement=BGshdSG)
    except: pass
    try:cmds.sets("BG_Cilindro*", e=True, forceElement=BGshdSG)
    except: pass
    try:cmds.sets("BG_Cono*", e=True, forceElement=BGshdSG)
    except: pass
    
    return [shd,shdBG]
        

# MAIN --------------------------------------------------------------------------------------------------------------------

def generate_function(inputTextIterations):        
    
    # Delete objects
    objects_to_delete = ["Cubo_centro*", "Cubo_lateral*", "Esfera_centro*", "Esfera_lateral*", "Cubo_merged*", 
                         "Cilindro_centro*", "Cilindro_lateral*", "Cono_centro*", "Cono_lateral*", 
                         "Toroide_centro*", "Toroide_lateral*", "Piramide_centro*", "Piramide_lateral*", 
                         "BG_Esfera*", "BG_Cubo*", "BG_Cilindro*", "BG_Cono*"]
    
    for obj in objects_to_delete:
        if cmds.objExists(obj):
            cmds.delete(obj)
    
    # Shape creator function
    slider_height = cmds.floatSliderGrp("sliderHeight", q=True, v=True)
    input_text_iterations_ui = cmds.intField("inputTextIterations2", q=True, v=1)
    rand_shape_selection, rand_shape_selection2, rand_selection_perspective = 0, 0, 0
    shape_creator_function(input_text_iterations_ui, slider_height, rand_shape_selection, 
                           rand_shape_selection2, rand_selection_perspective)
    
    # Shape group function
    if cmds.objExists("CH*"):
        cmds.delete("CH*")
    shape_group_function(slider_height)
    
    # BG shape creator function
    input_text_iterations_bg_ui = cmds.intField("inputTextIterationsBG2", q=True, v=1)
    if input_text_iterations_bg_ui == 0:
        if cmds.objExists("BG"):
            cmds.delete("BG")
    elif cmds.objExists("BG_Esfera*") or  cmds.objExists("BG_Cubo*") or cmds.objExists("BG_Cilindro*") or cmds.objExists("BG_Cono*"):
        cmds.delete("BG_Esfera*", "BG_Cubo*", "BG_Cilindro*", "BG_Cono*")
        BG_shape_function(input_text_iterations_bg_ui)
    else:
        BG_shape_function(input_text_iterations_bg_ui)
        
    # BG shape group function
    if cmds.objExists("BG"):
        cmds.delete("BG")
    BG_shape_group_function()
    
    # Shape color function
    for obj in ["shape_color", "BG_shape_color"]:
        if cmds.objExists(obj):
            cmds.delete(obj, "layeredTexture", "writeColor01", "writeColor02", "ambientOcclusion", "utility", 
                        "ramp", "setRange", "surfaceLuminance")
    for node in cmds.ls(type="aiAOV"):
        if not cmds.referenceQuery(node, inr=1):
            cmds.delete(node)
    shape_color_function()
        
def emerge_function(*args):
    
    randSelectionPerspective = round(random.uniform(0,1))
    
    # Delete existing objects with specific name patterns
    objs_to_delete = ["Cubo_centro*", "Cubo_lateral*", "Esfera_centro*", "Esfera_lateral*",
                      "Cubo_merged*", "Cilindro_centro*", "Cilindro_lateral*", "Cono_centro*",
                      "Cono_lateral*", "Toroide_centro*", "Toroide_lateral*", "Piramide_centro*",
                      "Piramide_lateral*", "CH*", "shape_color", "BG_shape_color"]
    cmds.delete([obj for obj in objs_to_delete if cmds.objExists(obj)])
        
    randHeight = random.uniform(-8, 8)
    randIterations = round(random.uniform(1, 4))
    randShapeSelection = round(random.uniform(2, 6))
    randConditional = round(random.uniform(0,1))
    randShapeSelection2 = 0 if randConditional == 0 else round(random.uniform(2, 6))
    
    # Call shape creator function
    shape_creator_function(randIterations, randHeight, randShapeSelection, randShapeSelection2, randSelectionPerspective)

    # Delete existing CH* objects and call shape group function
    if cmds.objExists("CH*"):
        cmds.delete("CH*")
    shape_group_function(randHeight)

    # Delete existing shape color objects and AOVs and call shape color function
    if cmds.objExists("shape_color") or cmds.objExists("BG_shape_color"):
        objs_to_delete = ["shape_color", "BG_shape_color", "layeredTexture", "writeColor01", "writeColor02",
                          "ambientOcclusion", "utility", "ramp", "setRange", "surfaceLuminance",
                          "AOV_ambientOcclusion", "AOV_utility"]
        cmds.delete([obj for obj in objs_to_delete if cmds.objExists(obj)])
        for node in cmds.ls(type="aiAOV"):
            if not cmds.referenceQuery(node, inr=1):
                cmds.delete(node)
        shape_color_function()
    else:
        shape_color_function()
        
        
def generate_CH_function(inputTextIterations):        
	
    # CH SHAPE CREATOR
    
    sliderHeightUI = cmds.floatSliderGrp(sliderHeight, q=True, v=True)
    inputTextIterationsUI = cmds.intField("inputTextIterations2", q=True, v=True)
    
    shapes = ["Cubo_centro*", "Cubo_lateral*", "Esfera_centro*", "Esfera_lateral*",
              "Cubo_merged*", "Cilindro_centro*", "Cilindro_lateral*", "Cono_centro*",
              "Cono_lateral*", "Toroide_centro*", "Toroide_lateral*", "Piramide_centro*",
              "Piramide_lateral*"]
    
    for shape in shapes:
        if cmds.objExists(shape):
            cmds.delete(shape)
        
    shape_creator_function(inputTextIterationsUI, sliderHeightUI, 0, 0, 0)
        
    # CH SHAPE GROUP
        
    if cmds.objExists("CH*"):
        cmds.delete("CH*")
    
    shape_group_function(sliderHeightUI)
        
    shapes = ["Cubo_centro*", "Cubo_lateral*", "Esfera_lateral*", "Esfera_centro*",
              "Cubo_merged*", "Cilindro_centro*", "Cilindro_lateral*", "Cono_centro*",
              "Cono_lateral*", "Toroide_centro*", "Toroide_lateral*", "Piramide_centro*",
              "Piramide_lateral*"]
    
    for shape in shapes:
        if cmds.objExists(shape):
            cmds.select(shape, add=True)
            
    cmds.hyperShade(assign="shape_color")
    
    
def subGenerate_function(*args):
        
    slider_height_ui = cmds.floatSliderGrp(sliderHeight, q=True, v=True)
    perspective = change_perspective_function()

    object_names = [
        "Cubo_centro*",
        "Cubo_lateral*",
        "Esfera_lateral*",
        "Esfera_centro*",
        "Cubo_merged*",
        "Cilindro_centro*",
        "Cilindro_lateral*",
        "Cono_centro*",
        "Cono_lateral*",
        "Toroide_centro*",
        "Toroide_lateral*",
        "Piramide_centro*",
        "Piramide_lateral*"
    ]

    for obj_name in object_names:
        if cmds.objExists(obj_name):
            cmds.select(obj_name, add=True)

    ch_item_list = cmds.ls(sl=True, type="mesh")
    ch_item_list_length = len(ch_item_list)

    for i in range(ch_item_list_length):
        rand_num_x_rot = random.uniform(-45, 45)
        rand_num_y_rot = random.uniform(-45, 45)
        rand_num_x = random.uniform(-8, 8)
        rand_num_y = random.uniform(-8, 8)
        rand_num_z = random.uniform(-8, 8)

        for obj_prefix in ["Esfera_centro", "Esfera_lateral", "Cubo_centro", "Cubo_lateral",
                           "Cubo_merged", "Cilindro_centro", "Cilindro_lateral", "Cono_centro",
                           "Cono_lateral", "Toroide_centro", "Toroide_lateral", "Piramide_centro",
                           "Piramide_lateral"]:
            obj_name = f"{obj_prefix}{i}"
            try:
                if "Esfera" in obj_prefix:
                    cmds.setAttr(f"{obj_name}.rotateY", 0)
                    cmds.move(rand_num_y, obj_name, y=True, absolute=True, os=True)
                    cmds.move(-rand_num_x, obj_name, x=True, absolute=True, os=True)
                    cmds.move(rand_num_z, obj_name, z=True, absolute=True, os=True)
                    cmds.setAttr(f"{obj_name}.rotateY", -45)

                elif "Cubo" in obj_prefix or "Cilindro" in obj_prefix or "Cono" in obj_prefix or "Toroide" in obj_prefix or "Piramide" in obj_prefix:
                    cmds.move(rand_num_y, obj_name, y=True, absolute=True, os=True)
                    cmds.move(-rand_num_x, obj_name, x=True, absolute=True, os=True)
                    cmds.move(rand_num_z, obj_name, z=True, absolute=True, os=True)
                    cmds.rotate(rand_num_x_rot, obj_name, x=True, absolute=True, os=True)
            except:
                pass

    try:
        ch_translate_y = cmds.getAttr("CH*.translateY")
    except:
        pass
              
def generate_BG_function(inputTextIterations):        
         
    inputTextIterationsBGUI = cmds.intField("inputTextIterationsBG2", q=True, v=True)
    
    if not inputTextIterationsBGUI and cmds.objExists("BG"):
        cmds.delete("BG")
        return
        
    if inputTextIterationsBGUI and cmds.ls("BG_Esfera*", "BG_Cubo*", "BG_Cilindro*", "BG_Cono*"):
        cmds.delete("BG_Esfera*", "BG_Cubo*", "BG_Cilindro*", "BG_Cono*")
        
    BG_shape_function(inputTextIterationsBGUI)
    
    if cmds.objExists("BG"):
        cmds.delete("BG")
        
    BG_shape_group_function()
        
    BGlist = cmds.ls('BG_Esfera*', 'BG_Cubo*', 'BG_Cilindro*', 'BG_Cono*')
    cmds.select(BGlist)
    cmds.hyperShade(assign="BG_shape_color")
     
 
def reflect_function(reflectIBoolVar):
    
    if reflectIBoolVar == 1:
        
        cmds.setAttr('CH*' + '.rotateY', -20)
        
    if reflectIBoolVar == 0:
        
        cmds.setAttr('CH*' + '.rotateY', 50)
        

def UpsideDown_function(upsideDownIBoolVar):
    
    if upsideDownIBoolVar == 1:
            
        cmds.xform('CH*', cp=1)
        
        cmds.setAttr('CH*' + ".rotateZ", 180)
        cmds.setAttr('CH*' + ".rotateY", -50)
        
        boundingBox3 = cmds.xform("CH*", q=True, bb=True, ws=True)
    
        cmds. move(boundingBox3[4], "CH*"+ '.scalePivot', y=True, absolute=True)
        cmds. move(boundingBox3[4], "CH*"+ '.rotatePivot', y=True, absolute=True)
        
        cmds. move(boundingBox3[1], "CH*"+ '.scalePivot', y=True, absolute=True)
        cmds. move(boundingBox3[1], "CH*"+ '.rotatePivot', y=True, absolute=True)
    
    if upsideDownIBoolVar == 0:
        
        cmds.xform('CH*', cp=1)
    
        cmds.setAttr('CH*' + ".rotateZ", 0)
        cmds.setAttr('CH*' + ".rotateY", 50)
        
        boundingBox2 = cmds.xform("CH*", q=True, bb=True, ws=True)
    
        cmds. move(boundingBox2[1], "CH*"+ '.scalePivot', y=True, absolute=True)
        cmds. move(boundingBox2[1], "CH*"+ '.rotatePivot', y=True, absolute=True)
    

def safeUI(*args):
    
    duplicateGrp = cmds.duplicate("CH*", n = "safe_CH")
    duplicateShader = cmds.duplicate("shape_color", n = "copy_shape_color", un = True)
    cmds.delete("CH*")
    listOfRelatives = cmds.listRelatives(duplicateGrp)
    numGroup = len(cmds.ls("safe_CH*"))

    for i in listOfRelatives:
        
        cmds.rename(i,"safe_CH_" + i + str(numGroup))
        cmds.select("safe_CH_" + i + str(numGroup), add=True)
        cmds.hyperShade(assign="copy_shape_color")

def hideUI(*args):
      
    cmds.hide("safe_CH*")
        
      
def showUI(*args):
    
    cmds.showHidden("safe_CH*")
        
    
def scale_model_function(*args):
    
    inputTextScaleUI = cmds.floatField("inputTextScale2", q=True, v=True)
    bbox = cmds.xform("CH*", q=True, bb=True, ws=True)
    x_min, y_min, z_min, x_max, y_max, z_max = bbox
    for obj in cmds.ls('BG_Esfera*', 'BG_Cubo*', 'BG_Cilindro*', 'BG_Cono*', type='transform'):
        pos = cmds.getAttr(obj + ".translate")[0]
        x, y, z = pos
        if x < x_min:
            cmds.setAttr(obj + ".translateX", (x + (x_min/2)) * inputTextScaleUI)
        elif x > x_max:
            cmds.setAttr(obj + ".translateX", (x + (x_max/2)) * inputTextScaleUI)
        elif y < y_min:
            cmds.setAttr(obj + ".translateY", y_min * inputTextScaleUI)
        elif y > y_max:
            cmds.setAttr(obj + ".translateY", y_max * inputTextScaleUI)
        elif z < z_min:
            cmds.setAttr(obj + ".translateZ", z_min * inputTextScaleUI)
        elif z > z_max:
            cmds.setAttr(obj + ".translateZ", z_max * inputTextScaleUI)              

def clear_system_function(*args):
    
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
    
    cmds.delete(cmds.ls("safe_CH*"))
    

def random_color_function(*args):
    
    tmp1 = random.uniform(0.0,1.0)
    tmp2 = random.uniform(0.0,1.0)
    tmp3 = random.uniform(0.0,1.0)
    
    cmds.setAttr("ramp" + '.colorEntryList[1].color', tmp1,tmp2,tmp3,type = 'double3')
    cmds.setAttr("ramp" + '.colorEntryList[1].position', 0.75)
    cmds.setAttr("ramp" + '.colorEntryList[0].color', 1-tmp1,1-tmp2,1-tmp3,type = 'double3')
    cmds.setAttr("ramp" + '.colorEntryList[0].position', 0.25)
    
    minValue = min([tmp1,tmp2,tmp3])
    
    if minValue == tmp1:
        
        tmp1Comp = tmp1
        tmp2Comp = tmp2
        tmp3Comp = 1-tmp3
        
        cmds.setAttr("BG_ramp" + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    if minValue == tmp2:
        
        tmp1Comp = 1-tmp1
        tmp2Comp = tmp2
        tmp3Comp = tmp3
        
        cmds.setAttr("BG_ramp" + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    if minValue == tmp3:
        
        tmp1Comp = tmp1
        tmp2Comp = 1-tmp2
        tmp3Comp = tmp3
        
        cmds.setAttr("BG_ramp" + '.colorEntryList[1].color', tmp1Comp,tmp2Comp,tmp3Comp,type = 'double3')
        
    cmds.setAttr("BG_ramp" + '.colorEntryList[0].color', 1-tmp1Comp,1-tmp2Comp,1-tmp3Comp,type = 'double3')
       
    cmds.setAttr("BG_ramp" + '.colorEntryList[1].position', 0.75)
    cmds.setAttr("BG_ramp" + '.colorEntryList[0].position', 0.25)
    
    
def invert_color_function(invertColorVar):
    
    if invertColorVar == 1:
        
        cmds.setAttr("ramp" + '.colorEntryList[0].position', 0.75)
        cmds.setAttr("ramp" + '.colorEntryList[1].position', 0.25)
        cmds.setAttr("BG_ramp" + '.colorEntryList[0].position', 0.75)
        cmds.setAttr("BG_ramp" + '.colorEntryList[1].position', 0.25)
        
    if invertColorVar == 0:
        
        cmds.setAttr("ramp" + '.colorEntryList[0].position', 0.25)
        cmds.setAttr("ramp" + '.colorEntryList[1].position', 0.75)
        cmds.setAttr("BG_ramp" + '.colorEntryList[0].position', 0.25)
        cmds.setAttr("BG_ramp" + '.colorEntryList[1].position', 0.75)
        
def change_color_function(changeColorVar):
    
    BGlist = cmds.ls('BG_Esfera*', 'BG_Cubo*', 'BG_Cilindro*', 'BG_Cono*', 'BG_Base')
    object_list = ['Cubo_centro*', 'Cubo_lateral*', 'Esfera_lateral*', 'Esfera_centro*', 
                   'Cubo_merged*', 'Cilindro_centro*', 'Cilindro_lateral*', 'Cono_centro*', 
                   'Cono_lateral*', 'Toroide_centro*', 'Toroide_lateral*', 'Piramide_centro*', 
                   'Piramide_lateral*']
    
    cmds.select(BGlist)
    if changeColorVar == 0:
        cmds.setAttr(('BG_shape_color.specular'), 0)
        cmds.hyperShade(assign="BG_shape_color")
        cmds.setAttr(('shape_color.specular'), 1)
        cmds.hyperShade(assign="shape_color")
    elif changeColorVar == 1:
        cmds.setAttr(('shape_color.specular'), 0)
        cmds.hyperShade(assign="shape_color")
        cmds.setAttr(('BG_shape_color.specular'), 1)
        cmds.hyperShade(assign="BG_shape_color")
    
    cmds.select(clear=True)
    for obj in object_list:
        if cmds.objExists(obj):
            cmds.select(obj, add=True)
    cmds.select(clear=True)

# INTERFACE 02 ----------------------------------------------------------------------------------------------------------------- 

cmds.checkBox( label='Reflect', align='left', onc = "reflect_function(1)", ofc = "reflect_function(0)")

cmds.checkBox( label='Upside Down', align='left', onc = "UpsideDown_function(1)", ofc = "UpsideDown_function(0)")

cmds.checkBox( label='Invert Color', align='left', onc = "invert_color_function(1)", ofc = "invert_color_function(0)")

cmds.checkBox( label='Change Color', align='left', onc = "change_color_function(1)", ofc = "change_color_function(0)")

cmds.button(label = "SCALE CH" ,command = scale_model_function)

cmds.button(label = "RANDOM COLOR", bgc = [0.63,0.12,1.00] ,command = random_color_function)

cmds.button(label = "CLEAN CH", bgc = [0.13,1.31,1.31],command = shape_cleaner_function)

cmds.button(label = "SAFE CH", bgc = [0.12,0.60,0.60],command = safeUI)

cmds.button(label = "HIDE CH", bgc = [0.32,0.60,0.60] ,command = hideUI)

cmds.button(label = "SHOW CH",bgc = [0.42,0.60,0.60] ,command = showUI)

cmds.button(label = "CLEAR SISTEM", bgc = [1.0,0.25,0.14] ,command = clear_system_function)

cmds.button(label = "GENERATE CH",w = 100, h = 25, bgc = [0.0,1.0,0.52] ,command = generate_CH_function)

cmds.button(label = "SUBGENERATE CH",w = 100, h = 25, bgc = [0.0,1.0,0.52] ,command = subGenerate_function)

cmds.button(label = "GENERATE BG",w = 100, h = 25, bgc = [0.0,1.0,0.52] ,command = generate_BG_function)

cmds.button(label = "EMERGE CH",w = 100, h = 50, bgc = [0.0,1.0,0.0] ,command = emerge_function)

cmds.button(label = "GENERATE",w = 100, h = 50, bgc = [0.6565,1.0,0.0] ,command = generate_function)

cmds.showWindow()

#BEAUTIFUL ROBOTS GENERATOR ONE BY DIEGO BELTRAN v31 27/03/2023 ALL RIGHTS RESERVED
        
