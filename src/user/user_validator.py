# USER SCHEMA
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6, "maxLength": 18},
        "password": {"type": "string", "minLength": 6, "maxLength": 32},
        "first_name": {"type": "string", "minLength": 3, "maxLength": 15},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 15},
        "ticket": {"type": "string", "minLength": 30, "maxLength": 50},
      },
    "required": ["name", "password", "first_name", "last_name"]
}