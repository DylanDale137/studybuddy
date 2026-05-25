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
    self.image_preloader.source = self.item['file']
  

  @handle("button_download", "click")
  def button_download_click(self, **event_args):
    download(self.item['file'])
