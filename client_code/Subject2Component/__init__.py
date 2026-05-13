from ._anvil_designer import Subject2ComponentTemplate
from anvil import *

class Subject2Component(Subject2ComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
