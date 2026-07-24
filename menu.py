import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
  def __init__(self, parent, pos_vars):
    super().__init__(master = parent)
    self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

    self.add('Position')
    self.add('Colour')
    self.add('Effects')
    self.add('Export')

    PositionFrame(self.tab('Position'), pos_vars)
    ColourFrame(self.tab('Colour'))

class PositionFrame(ctk.CTkFrame):
  def __init__(self, parent, pos_vars):
    super().__init__(master = parent, fg_color = 'transparent')
    self.pack(expand = True, fill = 'both')

    SliderPanel(self, 'Rotation', pos_vars['rotate'], 0, 360)  
    SliderPanel(self, 'Zoom', pos_vars['zoom'], 0, 200)  

class ColourFrame(ctk.CTkFrame): 
  def __init__(self, parent):
    super().__init__(master = parent, fg_color = 'transparent')
    self.pack(expand = True, fill = 'both')