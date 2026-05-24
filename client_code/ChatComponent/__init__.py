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

  def load_messages(self):
    messages = anvil.server.call('get_messages', 'chat')
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
    anvil.server.call('add_message', user['first_name'], message, 'chat', local_time)
    self.text_box_message.text = ""
    self.load_messages()