from ._anvil_designer import ChatComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timezone, timedelta

BRISBANE_OFFSET = timezone(timedelta(hours=10))

class ChatComponent(ChatComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_messages()
    user = anvil.users.get_user()
    if user and user["group_name"]:
      self.card_access.visible = True
      self.card_no_access.visible = False
    elif user and not user["group_name"]:
      self.card_access.visible = False
      self.card_no_access.visible = True
      self.display_error("User is not in a group. Please join or create a group")
    elif not user:
      self.card_access.visible = False
      self.card_no_access.visible = True
      self.display_error("User is not logged in. Please login to access")
    
  def load_messages(self):
    user = anvil.users.get_user()
    if not user:
      return
    group_name = user['group_name']
    messages = anvil.server.call_s('get_messages', 'chat', group_name)
    self.repeating_panel_chat.items = messages

  @handle("button_send", "click")
  def button_send_click(self, **event_args):
    message = self.text_box_message.text
    if not message:
      return
    user = anvil.users.get_user()
    if not user:
      alert("You must be logged in to send a message.")
      return
    local_time = datetime.now(tz=BRISBANE_OFFSET)
    anvil.server.call_s('add_message', user['first_name'], message, 'chat', local_time)
    self.text_box_message.text = ""
    self.load_messages()
  def display_error(self, message):
    self.label_message.visible = True
    self.label_message.foreground = "#ff0000"
    self.label_message.icon = "fa:exclamation-triangle"
    self.label_message.bold = True
    self.label_message.text = message
  @handle("repeating_panel_chat", "x-refresh-message")
  def refresh_messages(self, **event_args):
    self.load_messages()

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.load_messages()
  