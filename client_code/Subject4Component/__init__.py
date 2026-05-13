from ._anvil_designer import Subject4ComponentTemplate
from anvil import *

class Subject4Component(Subject4ComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
