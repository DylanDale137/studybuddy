import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_subject(name, type, draft, final, description):
  from datetime import datetime
  user = anvil.users.get_user()
  group_name = user['group_name'] if user else None

  # Count existing subjects for this group
  existing = app_tables.subjects.search(group=group_name)
  count = len(list(existing))

  if count >= 5:
    return 'too_many'

  app_tables.subjects.add_row(
    subject_name=name,
    assessment_type=type,
    draft_due=datetime(draft.year, draft.month, draft.day),
    final_due=datetime(final.year, final.month, final.day),
    assessment_description=description,
    order=count + 1,
    group=group_name
  )
  return 'success'
@anvil.server.callable
def get_subjects():
  user = anvil.users.get_user()
  group_name = user['group_name'] if user else None
  return app_tables.subjects.search(
    tables.order_by('order'),
    group=group_name
  )
@anvil.server.callable
def get_subject_by_order(order):
  user = anvil.users.get_user()
  group_name = user['group_name'] if user else None
  return app_tables.subjects.get(group=group_name, order=order)