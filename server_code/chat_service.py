import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_messages(subject, group_name):
  """Return all messages for a given subject and group, sorted by most recent first."""
  return app_tables.chat.search(
    tables.order_by('time_sent', ascending=False),
    subject=subject,
    group_name=group_name
  )

@anvil.server.callable
def add_message(user, content, subject, time_sent):
  """Add a new message to the chat table."""
  current_user = anvil.users.get_user()
  group_name = current_user['group_name'] if current_user else None

  app_tables.chat.add_row(
    content=content,
    user=user,
    time_sent=time_sent,
    subject=subject,
    group_name=group_name
  )

@anvil.server.callable
def delete_message(message_id):
  """Delete a message by its row ID."""
  message = app_tables.chat.get_by_id(message_id)
  if message:
    message.delete()

@anvil.server.callable
def update_message(message_id, content):
  """Edit the content of an existing message."""
  message = app_tables.chat.get_by_id(message_id)
  if message:
    message['content'] = content