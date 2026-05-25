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
from ..GroupComponent import GroupComponent
from ..Subject1Component import Subject1Component
from ..Subject2Component import Subject2Component
from ..Subject3Component import Subject3Component
from ..Subject4Component import Subject4Component
from ..Subject5Component import Subject5Component
from ..Subject6Component import Subject6Component
from ..Subject7Component import Subject7Component
from ..Subject8Component import Subject8Component

class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.
    self.content_panel.add_component(HomeComponent())
    self.set_active_link("home")
  def switch_label(self, change):
    self.headline_group_name.text = change
    
  def switch_component(self, state):
    if state == "home":
      cmpt = HomeComponent()
    elif state == "account":
      cmpt = AccountComponent()
    elif state == "add":
      cmpt = AddComponent()
    elif state == "chat":
      cmpt = ChatComponent()
    elif state == "details":
      cmpt = SetDetailsComponent()
    elif state == "group":
      cmpt = GroupComponent()
    elif state == "subject1":
      cmpt = Subject1Component()
    elif state == "subject2":
      cmpt = Subject2Component()
    elif state == "subject3":
      cmpt = Subject3Component()
    elif state == "subject4":
      cmpt = Subject4Component()
    elif state == "subject5":
      cmpt = Subject5Component()
    elif state == "subject6":
      cmpt = Subject6Component()
    elif state == "subject7":
      cmpt = Subject7Component()
    elif state == "subject8":
      cmpt = Subject8Component()
    self.repeating_panel_subjects.visible = False
    self.content_panel.clear()
    self.content_panel.add_component(cmpt)
    self.set_active_link(state)
  
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
    if state == "add":
      self.link_add.role = "selected"
    else:
      self.link_add.role = None
    if state == "group":
      self.link_group.role = "selected"
    else:
      self.link_group.role = None

    self.link_register.visible = not anvil.users.get_user()
    self.link_login.visible = not anvil.users.get_user()
    self.link_account.visible = anvil.users.get_user()
    self.link_logout.visible = anvil.users.get_user()

  @handle("link_register", "click")
  def link_register_click(self, **event_args):
    anvil.users.signup_with_form(allow_cancel=True)
    self.switch_component("details")
    self.set_active_link("home")
    
  @handle("link_login", "click")
  def link_login_click(self, **event_args):
    anvil.users.login_with_form(allow_cancel=True)
    self.switch_component("home")
    
    
  @handle("link_logout", "click")
  def link_logout_click(self, **event_args):
    anvil.users.logout()
    self.switch_component("home")
    


  @handle("link_account", "click")
  def link_account_click(self, **event_args):
    """This method is called when the link is clicked"""
    
    
    self.switch_component("account")

  @handle("link_home", "click")
  def link_home_click(self, **event_args):
    self.switch_component("home")

  @handle("link_chat", "click")
  def link_chat_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.switch_component("chat")

  @handle("link_subjects", "click")
  def link_subjects_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.repeating_panel_subjects.visible = not self.repeating_panel_subjects.visible
      # Write Code Here
    
    self.set_active_link("subjects")
    self.load_subjects()

  @handle("link_add", "click")
  def link_add_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.switch_component("add")
  
  def load_subjects(self):
    self.repeating_panel_subjects.items = anvil.server.call('get_subjects')

  @handle("link_group", "click")
  def link_group_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.switch_component("group")
