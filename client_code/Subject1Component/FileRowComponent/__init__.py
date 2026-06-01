from ._anvil_designer import FileRowComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class FileRowComponent(FileRowComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    file = self.item['File']
    self.image_preloader.source = file
    
    self.label_file_name.text = file.name

  @handle("button_download", "click")
  def button_download_click(self, **event_args):
    download(self.item['File'])
  @handle("button_delete", "click")
  def button_delete_click(self, **event_args):
    anvil.server.call('delete_file', self.item.get_id())
    self.parent.raise_event('x-refresh-files')

  
