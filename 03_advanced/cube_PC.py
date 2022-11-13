# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

class Cube:
   cube_scale = [1, 1, 1]
   cube_color = [0, 0, 0]
   cube_rotate = [0, 0, 0]
   cube_translate = [0, 0, 0]

   def __init__(self, name):
      self.name = name

   def translate(self, *args):
      self.cube_translate = args
      return self.cube_translate

   def rotate(self, *args):
      self.cube_rotate = args
      return self.cube_rotate

   def scale(self, *args):
      self.cube_scale = args
      return self.cube_scale

   def color(self, *args):
      self.cube_color = args
      return self.cube_color

   def update_transform(self, ttype, value):
      self.ttype = ttype
      self.value = value

   def print_status(self):
      info = [
             f"Name : {self.name}",
             f"Translate : {self.cube_translate}",
             f"Rotate : {self.cube_rotate}",
             f"Scale : {self.cube_scale}",
             f"Color : {self.cube_color}"
             ]

      print("\n".join(info))
      return True

cube1 = Cube("Container")
cube1.update_transform("scale", [50, 50, 50])
cube1.print_status()


cube2 = Cube("Package")
cube2.translate([10,20,30])
cube2.print_status()


cube3 = Cube("Tesseract")
cube3.rotate([90,5,10])
cube3.print_status()