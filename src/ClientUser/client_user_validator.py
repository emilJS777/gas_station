# CLIENT USER SCHEMA
client_user_schema = {
    "type": "object",
    "properties": {
        "client_id": {"type": "number"},
        "user_id": {"type": "number"},
      },
    "required": ["client_id", "user_id"]
}
