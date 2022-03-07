# FIRM SCHEMA
firm_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 30},
        "description": {"type": "string", "minLength": 6, "maxLength": 100}
      },
    "required": ["title"]
}
