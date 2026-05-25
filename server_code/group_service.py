import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_group(name, code):
  app_tables.groups.add_row(
    name=name,
    code=code
  )
  user = anvil.users.get_user()
  user['group_name'] = name

@anvil.server.callable
def check_group(name, code):
  group = app_tables.groups.get(name=name, code=code)
  if group:
    user = anvil.users.get_user()
    user['group_name'] = name
    return True
  return False
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