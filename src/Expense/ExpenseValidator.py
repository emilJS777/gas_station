# EXPENSE CREATE SCHEMA
expense_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2, "maxLength": 80},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "price": {"type": "number"},
      },
    "required": ["name", "price"]
}
