from ._anvil_designer import GroupComponentTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GroupComponent(GroupComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_join", "click")
  def button_join_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("button_join_cancel", "click")
  def button_join_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("button_join_confirm", "click")
  def button_join_confirm_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("button_create", "click")
  def button_create_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here
    
  @handle("button_create_cancel", "click")
  def button_create_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("button_create_confirm", "click")
  def button_create_confirm_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  
