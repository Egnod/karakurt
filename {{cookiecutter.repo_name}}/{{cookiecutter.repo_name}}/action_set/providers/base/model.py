from typing import Any

import ujson
from pydantic import BaseModel as PydanticModel


class BaseActionModelConfig:
    validate_assignment = True
    json_loads = ujson.loads
    json_dumps = ujson.dumps


class BaseActionModel(PydanticModel):
    @classmethod
    def get_field_info(cls, alias=False) -> list[dict[str, Any]]:
        fields_info = []

        for field_name in cls.__fields__.keys():
            fields_info.append(
                {
                    "name": field_name,
                    "type": cls.__fields__[field_name].type_,
                    "default": cls.__fields__[field_name].get_default(),
                }
            )

        return fields_info

    class Config(BaseActionModelConfig):
        pass


class BaseActionOptionsModelConfig(BaseActionModelConfig):
    pass


class BaseActionOptionsModel(BaseActionModel):
    class Config(BaseActionOptionsModelConfig):
        pass
