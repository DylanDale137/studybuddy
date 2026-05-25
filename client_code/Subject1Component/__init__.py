from ._anvil_designer import Subject1ComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Subject1Component(Subject1ComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_subject()
    self.load_files()

  def load_subject(self):
    subject = anvil.server.call('get_subject_by_order', 1)
    if subject:
      self.label_subject_name.text = subject['subject_name']
      self.label_assessment_type.text = subject['assessment_type']
      self.label_draft_due.text = subject['draft_due'].strftime('%d/%m/%Y')
      self.label_final_due.text = subject['final_due'].strftime('%d/%m/%Y')
      self.label_description.text = subject['assessment_description']

  @handle("file_loader_subject1", "change")
  def file_loader_subject1_change(self, file, **event_args):
    if not file:
      return
    user = anvil.users.get_user()
    if not user:
      alert("You must be logged in to upload a file.")
      return
    anvil.server.call('add_file', file, 'subject1')
    self.load_files()

  def load_files(self):
    user = anvil.users.get_user()
    if not user:
      return
    group_name = user['group_name']
    files = anvil.server.call('get_files', 'subject1', group_name)
    print(f"Files found: {len(list(files))}")
    self.repeating_panel_1.items = files  
    
