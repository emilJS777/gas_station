# USER SCHEMA
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6, "maxLength": 18},
        "password": {"type": "string", "minLength": 6, "maxLength": 32},
        "ticket": {"type": "string", "minLength": 30, "maxLength": 50},
        # "email_address": {"type": "string", 'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}
      },
    "required": ["name", "password", "email_address"]
}

# USER TICKET SCHEMA
user_ticket_schema = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string", "minLength": 3, "maxLength": 18},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 18},
        # "cash_box_id": {"type": "number"},
        # "cashier": {"type": "boolean"},
        # "salary": {"type": "number"}
    },
    "required": ["first_name", "last_name"]
}