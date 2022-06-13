# USER SCHEMA
resset_password_schema = {
    "type": "object",
    "properties": {
        "password": {"type": "string", "minLength": 6, "maxLength": 32},
        "ticket": {"type": "string", "minLength": 30, "maxLength": 50},
      },
    "required": ["new_password", "ticket"]
}