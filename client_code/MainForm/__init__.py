from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    self.breadcrumb_stem = self.headline_group_name

    # Any code you write here will run before the form opens.
    self.content_panel.add_component(HomeComponent())
    self.set_active_link("home")
    

  
    # Any code you write here will run before the form opens.
  
  def set_active_link(self, state):
    if state == "home":
      self.link_home.role = "selected"
    else:
      self.link_home.role = None
    if state == "chat":
      self.link_chat.role = "selected"
    else:
      self.link_chat.role = None
    if state == "subjects":
      self.link_subjects.role = "selected"
    else:
      self.link_subjects.role = None

    self.link_register.visible = not anvil.users.get_user()
    self.link_login.visible = not anvil.users.get_user()
    self.link_account.visible = anvil.users.get_user()
    self.link_logout.visible = anvil.users.get_user()

  @handle("link_register", "click")
  def link_register_click(self, **event_args):
    anvil.users.signup_with_form(allow_cancel=True)
    self.content_panel.clear()
    self.content_panel.add_component(SetDetailsComponent())
    
    self.set_active_link("home")
    
  @handle("link_login", "click")
  def link_login_click(self, **event_args):
    anvil.users.login_with_form(allow_cancel=True)
    self.content_panel.clear()
    self.content_panel.add_component(HomeComponent())
    
    self.set_active_link("home")
    
  @handle("link_logout", "click")
  def link_logout_click(self, **event_args):
    anvil.users.logout()
    self.content_panel.clear()
    self.content_panel.add_component(HomeComponent())
    
    self.set_active_link("home")

  @handle("link_account", "click")
  def link_account_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    
    self.content_panel.add_component(AccountComponent())
    
    self.set_active_link(("account"))

  @handle("link_home", "click")
  def link_home_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(HomeComponent())
    
    self.set_active_link("home")

  @handle("link_chat", "click")
  def link_chat_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(ChatComponent())
    
    self.set_active_link("chat")

  @handle("link_subjects", "click")
  def link_subjects_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.repeating_panel_subjects.visible = not self.repeating_panel_subjects.visible
      # Write Code Here
    
    self.set_active_link("subjects")
  
  
