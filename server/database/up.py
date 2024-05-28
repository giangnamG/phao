from migrate import questions_table, users_table
from seeding import questions, users

# migrate
questions_table()
users_table()

# seeding
questions()
users()