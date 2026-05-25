from ._anvil_designer import GroupComponentTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GroupComponent(GroupComponentTemplate):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.name = ""
    self.code = ""

  @handle("button_create_confirm", "click")
  def button_create_confirm_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.text_box_create_name.text:
      self.display_error("Group name needed")
    elif not self.text_box_create_code.text:
      self.display_error("Group password needed")
    else:
      self.name = self.text_box_create_name.text
      self.code = self.text_box_create_code.text
      anvil.server.call('add_group', self.name, self.code)
      self.display_save(f"{self.name} created with the password: {self.code}")
      self.reset_form()

  def display_error(self, message):
    self.label_message.visible = True
    self.label_message.foreground = "#ff0000"
    self.label_message.icon = "fa:exclamation-triangle"
    self.label_message.bold = True
    self.label_message.text = message

  def display_save(self, message):
    self.label_message.visible = True
    self.label_message.foreground = "#000000"
    self.label_message.icon = "fa:save"
    self.label_message.bold = False
    self.label_message.text = message

  def reset_form(self):
    self.name = ""
    self.code = ""
    self.text_box_create_name.text = ""
    self.text_box_create_code.text = ""

  @handle("button_create", "click")
  def button_create_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_create.visible = not self.card_create.visible

  @handle("button_create_cancel", "click")
  def button_create_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_create.visible = not self.card_create.visible

  

  @handle("button_join", "click")
  def button_join_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_join.visible = not self.card_join.visible

  @handle("button_join_cancel", "click")
  def button_join_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_join.visible = not self.card_join.visible

  
  @handle("button_join_confirm", "click")
  def button_join_confirm_click(self, **event_args):
    if not self.text_box_join_name.text:
      self.display_error("Group name needed")
    elif not self.text_box_join_code.text:
      self.display_error("Group password needed")
    else:
      name = self.text_box_join_name.text
      code = self.text_box_join_code.text
      success = anvil.server.call('check_group', name, code)
      if success:
        self.display_save(f"Successfully joined {name}!")
        self.text_box_join_name.text = ""
        self.text_box_join_code.text = ""
        self.card_join.visible = False
      else:
        self.display_error("No group found with that name and password.")

  
