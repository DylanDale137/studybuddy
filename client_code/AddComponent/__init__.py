from ._anvil_designer import AddComponentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class AddComponent(AddComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name = ""
    self.type = ""
    self.draft = None
    self.final = None
    self.description = ""

    # Any code you write here will run before the form opens.
    self.label_message.visible = False

  @handle("button_add", "click")
  def button_add_click(self, **event_args):
    # validation
    if not self.text_box_name.text:
      self.display_error("Subject name needed")
    elif not self.text_box_type.text:
      self.display_error("Assessment type needed")
    elif not self.date_picker_draft.date:
      self.display_error("Draft due date needed")
    elif not self.date_picker_final.date:
      self.display_error("Final due date needed")
    elif not self.text_box_description.text:
      self.display_error("Assessment details needed")
    else:
      self.name = self.text_box_name.text
      self.type = self.text_box_type.text
      self.draft = self.date_picker_draft.date
      self.final = self.date_picker_final.date
      self.description = self.text_box_description.text
      self.display_save(f"{self.name} subject is {self.type}: draft due: {self.draft}, final due: {self.final}, with a description of {self.description} recorded")
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
    self.type = ""
    self.draft = None
    self.final = None
    self.description = ""
    self.text_box_name.text = ""
    self.text_box_type.text = ""
    self.date_picker_draft.date = None
    self.date_picker_final.date = None
    self.text_box_description.text = ""
