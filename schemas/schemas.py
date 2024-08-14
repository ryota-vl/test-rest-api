from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_schema(data: dict or list, schema: dict or list) -> tuple[bool, str | None]:
    try:
        validate(data, schema)
    except ValidationError as e:
        return False, e.message
    return True, None


post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

comment_schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["postId", "id", "name", "email", "body"]
}

album_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"}
    },
    "required": ["userId", "id", "title"]
}

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "object",
                    "properties": {
                        "lat": {"type": "string"},
                        "lng": {"type": "string"}
                    },
                    "required": ["lat", "lng"]
                }
            },
            "required": ["street", "suite", "city", "zipcode", "geo"]
        },
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"}
            },
            "required": ["name", "catchPhrase", "bs"]
        }
    },
    "required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
}