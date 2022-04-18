# USER SCHEMA
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6, "maxLength": 18},
        "password": {"type": "string", "minLength": 6, "maxLength": 32},
        "ticket": {"type": "string", "minLength": 30, "maxLength": 50},
      },
    "required": ["name", "password"]
}

# USER TICKET SCHEMA
user_ticket_schema = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string", "minLength": 3, "maxLength": 18},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 18},
        # "cash_box_id": {"type": "number"}
    },
    "required": ["first_name", "last_name"]
}