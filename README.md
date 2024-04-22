# Faremit Anchor Project
Implemented sep1, sep10 and sep24.
## start
python manage.py runserver --nostatic
## command cli
- deposit monitoring
- withdraw monitoring
  python3 manage.py watch_transactions
  python3 manage.py execute_outgoing_transactions --loop
  python3 manage.py poll_outgoing_transactions --loop