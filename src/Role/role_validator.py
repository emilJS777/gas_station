# ROLE
role_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 2, "maxLength": 30},
        "permission_ids": {"type": "array"},
      },
    "required": ["name", "permission_ids"]
}

