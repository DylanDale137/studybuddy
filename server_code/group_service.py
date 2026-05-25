import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_group(name, code):
  existing = app_tables.groups.get(name=name)
  if existing:
    return 'name_taken'

  user = anvil.users.get_user()
  if not user:
    return 'not_logged_in'

  app_tables.groups.add_row(
    name=name,
    code=code
  )
  user['group_name'] = name
  return 'success'

@anvil.server.callable
def check_group(name, code):
  user = anvil.users.get_user()
  if not user:
    return 'not_logged_in'

  group = app_tables.groups.get(name=name, code=code)
  if group:
    user['group_name'] = name
    return 'success'
  return 'not_found'
@anvil.server.callable
def get_group_code(name):
  group = app_tables.groups.get(name=name)
  if group:
    return group['code']
  return None
@anvil.server.callable
def leave_group():
  user = anvil.users.get_user()
  if user:
    user['group_name'] = None