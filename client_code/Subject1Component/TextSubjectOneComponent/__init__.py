from ._anvil_designer import TextSubjectOneComponentTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TextSubjectOneComponent(TextSubjectOneComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    item = self.item
    self.label_name.text = item['user']
    self.label_time.text = item['time_sent'].strftime('%H:%M')
    self.label_text.text = item['content']
  @handle("button_delete", "click")
  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_message', self.item.get_id())
    self.parent.raise_event('x-refresh-message')
