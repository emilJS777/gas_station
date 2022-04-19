# DEVICE
device_create_schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "minLength": 2, "maxLength": 120},
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "cash_box_id": {"type": "number"},
      },
    "required": ["key", "name", "cash_box_id"]
}

