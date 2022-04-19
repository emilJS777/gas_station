# DEVICE CREATE SCHEMA
device_create_schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "minLength": 2, "maxLength": 120},
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "error_after_minutes": {"type": "number"}
      },
    "required": ["key", "name", "error_after_minutes"]
}

# DEVICE UPDATE SCHEMA
device_update_schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string", "minLength": 2, "maxLength": 120},
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "error_after_minutes": {"type": "number"},
    },
    "required": ["key", "name", "error_after_minutes"]
}
