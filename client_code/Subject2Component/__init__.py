from ._anvil_designer import Subject2ComponentTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timezone, timedelta

BRISBANE_OFFSET = timezone(timedelta(hours=10))


class Subject2Component(Subject2ComponentTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_subject()
    self.load_files()
    self.load_messages()

  def load_subject(self):
    subject = anvil.server.call("get_subject_by_order", 2)
    if subject:
      self.label_subject_name.text = subject["subject_name"]
      self.label_assessment_type.text = subject["assessment_type"]
      self.label_draft_due.text = subject["draft_due"].strftime("%d/%m/%Y")
      self.label_final_due.text = subject["final_due"].strftime("%d/%m/%Y")
      self.label_description.text = subject["assessment_description"]

  @handle("file_loader_subject1", "change")
  def file_loader_subject1_change(self, file, **event_args):
    if not file:
      return
    user = anvil.users.get_user()
    if not user:
      alert("You must be logged in to upload a file.")
      return
    anvil.server.call("add_file", file, "subject2")
    self.load_files()

  def load_files(self):
    user = anvil.users.get_user()
    if not user:
      return
    group_name = user["group_name"]
    files = anvil.server.call("get_files", "subject2", group_name)

    self.repeating_panel_1.items = files

  @handle("repeating_panel_1", "x-refresh-files")
  def refresh_files(self, **event_args):
    self.load_files()

  def load_messages(self):
    user = anvil.users.get_user()
    if not user:
      return
    group_name = user["group_name"]
    messages = anvil.server.call("get_messages", "subject2", group_name)
    self.repeating_panel_2.items = messages

  @handle("button_send", "click")
  def button_send_click(self, **event_args):
    message = self.text_box_subject1.text
    if not message:
      return
    user = anvil.users.get_user()
    if not user:
      alert("You must be logged in to send a message.")
      return
    local_time = datetime.now(tz=BRISBANE_OFFSET)
    anvil.server.call_s(
      "add_message", user["first_name"], message, "subject2", local_time
    )
    self.text_box_subject1.text = ""
    self.load_messages()

  @handle("timer_1", "tick")
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.load_messages()
