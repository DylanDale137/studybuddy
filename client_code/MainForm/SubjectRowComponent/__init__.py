from ._anvil_designer import SubjectRowComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class SubjectRowComponent(SubjectRowComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.link_subject.text = self.item['subject_name']

  @handle("link_subject", "click")
  def link_subject_click(self, **event_args):
    main_form = get_open_form()
    main_form.switch_component(f"subject{self.item['order']}")
  
  
