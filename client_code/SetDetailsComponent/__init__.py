from ._anvil_designer import SetDetailsComponentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..GroupComponent import GroupComponent


class SetDetailsComponent(SetDetailsComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if not anvil.users.get_user():
      self.headline_error.visible = True
      self.card_1.visible = False
      self.button_save.visible = False
    else:
      self.card_1.visible = True
      self.button_save.visible = True
      self.headline_error.visible = False
      user = anvil.users.get_user()
      if user["first_name"]:
        self.text_box_first_name.text = user["first_name"]
      if user["last_name"]:
        self.text_box_last_name.text = user["last_name"]
    # Any code you write here will run before the form opens.
  @handle('button_save', 'click')
  def button_save_click(self, **event_args):

    if self.text_box_first_name.text == "":
      self.label_error.text = "First name cannot be blank"
      self.label_error.visible = True
      return

    if self.text_box_last_name.text == "":
      self.label_error.text = "Last name cannot be blank"
      self.label_error.visible = True
      return

    self.label_error.visible = False
    anvil.server.call("update_user", 
                      self.text_box_first_name.text, 
                      self.text_box_last_name.text)

    main_form = get_open_form()
    user = anvil.users.get_user()
    if not user["group_name"]:
      main_form.switch_component("group")
    else:
      main_form.switch_component("account")
    
    