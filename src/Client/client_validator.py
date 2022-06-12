# CLIENT SCHEMA
client_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 30},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "device_ids": {"type": "array"}
      },
    "required": ["name", "description", "device_ids"]
}
