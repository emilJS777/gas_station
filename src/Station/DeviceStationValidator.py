# DEVICE
device_create_schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "minLength": 2, "maxLength": 120},
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "client_id": {"type": "number"},
        "cash_box_id": {"type": "number"},
      },
    "required": ["key", "name", "client_id", "cash_box_id"]
}

device_update_schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "minLength": 2, "maxLength": 120},
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "cash_box_id": {"type": "number"},
      },
    "required": ["key", "name", "cash_box_id"]
}
