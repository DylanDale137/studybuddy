from ._anvil_designer import ChatRowComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class ChatRowComponent(ChatRowComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    item = self.item
    self.label_name.text = item['user']
    self.label_time.text = item['time_sent'].strftime('%H:%M')
    self.label_text.text = item['content']


    
