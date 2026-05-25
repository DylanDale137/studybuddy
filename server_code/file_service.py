import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_file(file, subject):
  user = anvil.users.get_user()
  group_name = user['group_name'] if user else None
  from datetime import datetime, timezone
  app_tables.files.add_row(
    file=file,
    subject=subject,
    group_name=group_name,
    time_sent=datetime.now(tz=timezone.utc)
  )

@anvil.server.callable
def get_files(subject, group_name):
  """Return all files for a given subject and group, sorted by most recent first."""
  return app_tables.files.search(
    tables.order_by('time_sent', ascending=False),
    subject=subject,
    group=group_name
  )
