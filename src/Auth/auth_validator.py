# USER SCHEMA
resset_password_schema = {
    "type": "object",
    "properties": {
        "new_password": {"type": "string", "minLength": 6, "maxLength": 32},
        "ticket_code": {"type": "string", "minLength": 10, "maxLength": 50},
        "old_password": {"type": "string", "minLength": 6, "maxLength": 50},
      },
    "required": ["new_password"]
}

request_resset_password_schema = {
    "type": "object",
    "properties": {
        "email_address": {"type": "string", "minLength": 6, "maxLength": 32, 'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}
      },
    "required": ["email_address"]
}