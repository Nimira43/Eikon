import customtkinter as ctk

class Menu(ctk.CTkTabview):
  def __init__(self, parent):
    super().__init__(master = parent)
    self.grid(row = 0, column = 0, sticky = 'nsew')

    self.add('Position')
    self.add('Colour')
    self.add('Effects')
    self.add('Export')

    PositionFrame(self.tab('Position'))
    ColourFrame(self.tab('Colour'))

class PositionFrame(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(master = parent, fg_color = 'blue')
    self.pack(expand = True, fill = 'transparent')

class ColourFrame(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(master = parent, fg_color = 'green')
    self.pack(expand = True, fill = 'transparent')