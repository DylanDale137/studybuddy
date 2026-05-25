from ._anvil_designer import Subject5ComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Subject5Component(Subject5ComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_files()

  @handle("file_loader_subject1", "change")
  def file_loader_subject1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if not file:
      return
    user = anvil.users.get_user()
    if not user:
      alert("You must be logged in to upload a file.")
      return
    anvil.server.call("add_file", file, "subject5")
    self.load_files()

  def load_files(self):
    user = anvil.users.get_user()
    if not user:
      return
    group_name = user["group_name"]
    files = anvil.server.call("get_files", "subject5", group_name)
    self.repeating_panel_1.items = files
