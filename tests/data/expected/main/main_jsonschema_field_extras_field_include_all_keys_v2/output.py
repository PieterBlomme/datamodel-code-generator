# generated by datamodel-codegen:
#   filename:  extras.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Extras(BaseModel):
    name: Optional[str] = Field(
        None,
        description='normal key',
        examples=['example'],
        json_schema_extra={
            'key1': 123,
            'key2': 456,
            '$exclude': 123,
            'invalid-key-1': 'abc',
            '-invalid+key_2': 'efg',
            '$comment': 'comment',
            'register': 'hij',
            'schema': 'klm',
            'x-abc': True,
            'readOnly': True,
        },
        repr=True,
    )
    age: Optional[int] = Field(
        None, examples=[13, 20], json_schema_extra={'example': 12, 'writeOnly': True}
    )
