# CASH BOX SCHEMA
cash_box_create_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 30},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "client_id": {"type": "number"},
      },
    "required": ["name", "description"]
}
