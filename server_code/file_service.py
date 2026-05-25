import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timezone, timedelta

@anvil.server.callable
def add_file(file, subject):
  user = anvil.users.get_user()
  group_name = user['group_name'] if user else None
  print(f"Saving file with subject: '{subject}' and group_name: '{group_name}'")
  app_tables.files.add_row(
    File=file,
    subject=subject,
    group=group_name,
    time_sent=datetime.now(tz=timezone.utc)
  )

@anvil.server.callable
def get_files(subject, group_name):
  
  return app_tables.files.search(
    tables.order_by('time_sent', ascending=False),
    subject=subject,
    group=group_name
  )
