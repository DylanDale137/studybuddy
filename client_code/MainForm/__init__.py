from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.server
from ..HomeComponent import HomeComponent
from ..AddComponent import AddComponent
from ..AccountComponent import AccountComponent
from ..SetDetailsComponent import SetDetailsComponent
from ..WelcomeComponent import WelcomeComponent
from ..ChatComponent import ChatComponent


class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  
    # Any code you write here will run before the form opens.
  
  
  @handle("link_register", "click")
  def link_register_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here

  @handle("link_login", "click")
  def link_login_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here

  @handle("link_account", "click")
  def link_account_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass  # Write Code Here

  @handle("link_home", "click")
  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(HomeComponent())

  @handle("link_chat", "click")
  def link_chat_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(ChatComponent())

  @handle("link_subjects", "click")
  def link_subjects_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.repeating_panel_subjects.visible = not self.repeating_panel_subjects.visible
      # Write Code Here
