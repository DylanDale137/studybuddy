import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_group(name, code):
  user = anvil.users.get_user()
  
  
  app_tables.groups.add_row(name= name,
                                 code=code,
                                 user= user)
  
  
  