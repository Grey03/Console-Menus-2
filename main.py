import json
import math
global Info

#https://www.rapidtables.com/code/text/unicode-characters.html
#Good place for unicode

# MenuPrinter()
# MenuPrinter("DefaultMenu")
# MenuPrinter("LayerTypes")



def savejson(Data,FileName):
  FileName = (FileName + ".json")
  json_object = json.dumps(Data, indent = len(Data))
  with open(FileName, "w") as outfile:
      outfile.write(json_object)
  outfile.close()
  


def Materials():
  print ("Go to https://www.rapidtables.com/code/text/unicode-characters.html\nAny thing you want can be a material for example \"\u2B1C\" use the escape sequences.")

def getjson(FileName):
  FileName = (FileName + ".json")
  f = open(FileName)
  data = json.load(f)
  f.close()
  return data

def RefreshInfo():
  global Info
  Info = getjson("quicksave")

def SaveMenus():
  Temp = getjson("quicksave")
  savejson(Temp,"mainsave")

def LoadMenus():
  Temp = getjson("mainsave")
  savejson(Temp,"quicksave")

def addtoquicksave(Data):
  Old = getjson("quicksave")
  Old.update(Data)
  savejson(Old,"quicksave")
  RefreshInfo()

def UpdateMenuValues(MenuToUpdate,NewValues):
  global Info
  RefreshInfo()
  if len(Info[MenuToUpdate]["Layout"]) != len(NewValues):
    print ("List Lengths Dont Match!")
    return None
  else:
    Info[MenuToUpdate]["Values"] = NewValues
    savejson(Info,"quicksave")

def TempMenuValues(MenuToUpdate,NewValues):
  global Info
  RefreshInfo()
  if len(Info[MenuToUpdate]["Layout"]) != len(NewValues):
    print ("List Lengths Dont Match!")
    return None
  else:
    Info[MenuToUpdate]["Values"] = NewValues

def UpdateMenuTypes(MenuToUpdate,NewTypes):
  global Info
  RefreshInfo()
  if len(Info[MenuToUpdate]["Layout"]) != len(NewTypes):
    print ("List Lengths Dont Match!")
    return None
  else:
    Info[MenuToUpdate]["Layout"] = NewTypes
    savejson(Info,"quicksave")

def MenuPrinter(*args):
  global Info
  
  if len(args) < 1:
    print (Info.keys())
    return None
  if len(args) == 1:
    MenuName = args[0]
    ShowNum = False
  if len(args) == 2:
    MenuName = args[0]
    ShowNum = args[1]
    
  Menu = Info[MenuName]
  Width = 0
  for i in range(len(Menu["Values"])):
    i = int(len(Menu["Values"][i]))
    if i > Width:
      Width = (i)
  if Width % 2 != 0:
    Width = Width + 1
  Width = Width + 4
  
  def Roof(Menu,Width):
    CornerMat = Menu["Corners"]
    RoofMat = Menu["Roof"]
    print (CornerMat, end = "")
    for i in range(Width - 2):
      print (RoofMat, end = "")
    print (CornerMat)
    
  def Floor(Menu,Width):
    CornerMat = Menu["Corners"]
    FloorMat = Menu["Floor"]
    print (CornerMat, end = "")
    for i in range(Width - 2):
      print (FloorMat, end = "")
    print (CornerMat)
    
  def Bar(Menu,Width):
    LeftMat = Menu["Left"]
    RightMat = Menu["Right"]
    BarMat = Menu["Bar"]
    print (LeftMat, end = "")
    for i in range(Width - 2):
      print (BarMat, end = "")
    print (RightMat)

  def LeftBased(Menu,Width,Input):
    Left = Menu["Left"]
    Right = Menu["Right"]
    print (Left,end = "")
    print (Input,end = "")
    for i in range(Width-len(Input)-2):
      print (" ", end = "")
    print (Right)

  def RightBased(Menu,Width,Input):
    Left = Menu["Left"]
    Right = Menu["Right"]
    print (Left,end = "")
    for i in range(Width-len(Input)-1):
      print (" ", end = "")
    print (Input,end = Right)
    print("")

  def CenterBased(Menu,Width,Input):
    Width = Width - 2
    Left = Menu["Left"]
    Right = Menu["Right"]
    print (Left, end = "")
    Spacing = math.floor((Width - len(Input))/2)
    if len(Input) % 2 != 0:
      print (" ", end = "")
    for i in range(Spacing):
      print (" ", end = "")
    print (Input, end = "")
    for n in range(Spacing):
      print (" ", end = "")
    print (Right)
    
  #1 
  #5 Material Settings
  #6
  #3 Roof: 
  #3 Floor: 
  #3 Left:
  #3 Right:
  #3 Bar:
  #3 Corners:
  #2 

  

  Layout = (Menu["Layout"])
  Values = (Menu["Values"])
  for i in range(len(Menu["Layout"])):
    Input = Values[i]
    if ShowNum == True:
      print (i + 1, end = "")
    #Roof
    if 1 == Layout[i]:
      Roof(Menu,Width)
      #Floor
    if 2 == Layout[i]:
      Floor(Menu,Width)
      #Left Based
    if 3 == Layout[i]:
      LeftBased(Menu, Width, Input)
    #Right Based
    if 4 == Layout[i]:
      RightBased(Menu, Width, Input)
    #Center Based
    if 5 == Layout[i]:
      CenterBased(Menu, Width, Input)
    #Bar
    if 6 == Layout[i]:
      Bar(Menu, Width)
    if Layout[i] > 6 or Layout[i] < 1:
      print ("")


def MenuCreator(*args):
  global Info
  #name of page
  #number of layers
  #the type of the layers in order top to bottom
  #the value for the later top to bottom
  try:
    name = args[0]
    layercount = args[1]
    layertypes = args[2]
    layervalues = args[3]
  except:
    name = (input("Give the name of the menu: "))
    layercount = (input("Enter the number of layers for the menu: "))
    while layercount.isalnum() == False:
      layercount = (input("Enter the number of layers for the menu: "))
    layercount = int(layercount)
    if layercount < 1:
      layercount = 0
    if layercount > 0:
      MenuPrinter("LayerTypes")
      layertypes = []
      for i in range(layercount):
        temp = int(input("Enter the type of layer, layer " + str(i + 1) + " should be: "))
        layertypes.append(temp)
      layervalues = []
      for n in range(layercount):
        temp = (input("Enter the value of layer, layer " + str(n + 1) + " should be: "))
        layervalues.append(temp)
    newmenu = {
      (name):{
    "Roof":"\u2b1a",
    "Floor":"\u2b1a",
    "Left":"\u2b1a",
    "Right":"\u2b1a",
    "Bar":"\u2b1a",
    "Corners":"\u2b1a",
    "Layout":(layertypes),
    "Values":(layervalues)
      }
    }
    addtoquicksave(newmenu)
    RefreshInfo()

def MenuEditor(*args):
  global Info
  #1 is menu to edit
  #2 is if it should edit the 1: values or 2: types
  #3 is new values list or new types list
  if len(args) == 3:
    MenuToEdit = args[0]
    ValuesOrTypes = args[1]
    NewStuff = args[2]
    
  else:
    print (Info.keys())
    MenuToEdit = input("Enter Menu to Edit: ")
    ValuesOrTypes = input("Select Which to Edit\n1: Values\n2: Types\n: ")
    
    if ValuesOrTypes == 1:
      NewStuff = []
      for i in range(len(Info[MenuToEdit]["Values"])):
        temp = input("Enter New Value: ")
        NewStuff.append(temp)
      
    if ValuesOrTypes ==2:
      NewStuff = []
      for i in range(len(Info[MenuToEdit]["Layout"])):
        temp = int(input("Enter New Layout Number: "))
        NewStuff.append(temp)
  if ValuesOrTypes == 1:
    UpdateMenuValues(MenuToEdit,NewStuff)
  if ValuesOrTypes == 2:
    UpdateMenuTypes(MenuToEdit,NewStuff)

def MaterialDisplay(MenuName):
  global Info
  Roof = str("Roof: " + Info[MenuName]["Roof"] + "  ")
  Floor = str("Floor: " + Info[MenuName]["Floor"] + "  ")
  Left = str("Left: " + Info[MenuName]["Left"] + "  ")
  Right = str("Right: " + Info[MenuName]["Right"] + "  ")
  Bar = str("Bar: " + Info[MenuName]["Bar"] + "  ")
  Corners = str("Corners: " + Info[MenuName]["Corners"]+ "  ")

  NewValues = [
    "",
    "Material Values",
    "",
    Roof,
    Floor,
    Left,
    Right,
    Bar,
    Corners,
    ""
  ]
  TempMenuValues("MaterialDisplay",NewValues)
  MenuPrinter("MaterialDisplay")

def MaterialEditor(*args):
  global Info
  #Menu Name
  MenuName = ""
  if len(args) == 1:
    MenuName = args[0]
  else:
    print (Info.keys())
    MenuName = input("Enter Menu to Edit: ")
    MaterialDisplay(MenuName)

def AddorRemoveLine(Menu,Location,AddorRemove):
  global Info
  Values = Info[Menu]["Values"]
  Layout = Info[Menu]["Layout"]
  if AddorRemove == 1:
    Values.insert(Location,"")
    Layout.insert(Location,6)
  if AddorRemove == 0:
    del Values[Location]
    del Layout[Location]
  Info[Menu]["Values"] = Values
  Info[Menu]["Layout"] = Layout
  savejson(Info,"quicksave")
  #adding inserts a line, #removing removes it.

def MenuFunctionHelp(*args):
  #Add basic info for just using the help
  #Then add info explaining each function
  #Add a first time start menu
  #aka a main menu that can lead u to all the functions basically such as editing etc...
  
  if len(args) == 0:
    print ("temp")
  else:
    FunctionQuestioned = args[0]
  

def FirstTime():
  FIRSTTIMEJSON={
   "DefaultMenu": {
      "Roof": "\u2b1a",
      "Floor": "\u2b1a",
      "Left": "\u2b1a",
      "Right": "\u2b1a",
      "Bar": "\u2b1a",
      "Corners": "\u2b1a",
      "Layout": [
         1,
         5,
         2
      ],
      "Values": [
         "",
         "tester",
         ""
      ]
   },
   "LayerTypes": {
      "Roof": "\u2b1a",
      "Floor": "\u2b1a",
      "Left": "\u2b1a",
      "Right": "\u2b1a",
      "Bar": "\u2b1a",
      "Corners": "\u2b1a",
      "Layout": [
         1,
         5,
         6,
         3,
         3,
         3,
         3,
         3,
         3,
         2
      ],
      "Values": [
         "",
         "Layer Types",
         "",
         " 1: Roof",
         " 2: Floor",
         " 3: Left Based Text",
         " 4: Right Based Text",
         " 5: Centered Text",
         " 6: Bar",
         ""
      ]
   },
   "MaterialDisplay": {
      "Roof": "\u2b1a",
      "Floor": "\u2b1a",
      "Left": "\u2b1a",
      "Right": "\u2b1a",
      "Bar": "\u2b1a",
      "Corners": "\u2b1a",
      "Layout": [
         1,
         5,
         6,
         3,
         3,
         3,
         3,
         3,
         3,
         2
      ],
      "Values": [
         "",
         "Material Settings",
         "",
         "Roof:",
         "Floor:",
         "Left:",
         "Right:",
         "Bar:",
         "Corners:",
         ""
      ]
   }
}
  savejson(FIRSTTIMEJSON,"quicksave")
  savejson(FIRSTTIMEJSON,"mainsave")

try:
  RefreshInfo()
except:
  FirstTime()
  RefreshInfo()