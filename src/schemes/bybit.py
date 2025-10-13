from datetime import datetime
from .kline import KlineScheme
from pydantic import BaseModel, ConfigDict, Field, model_validator, field_validator


class ByBitResponseKlineScheme(BaseModel, KlineScheme):
    @model_validator(mode='before')
    @classmethod
    def get_model_from_list(cls, data: list[str]) -> dict[str, str]:
        return { k: v for k, v in zip(cls.model_fields.keys(), data) }
    
    @field_validator('start_date', mode='before')
    @classmethod
    def start_date_validator(cls, value: str) -> str:
        return datetime.fromtimestamp(int(value) / 1000)


class ByBitResponseScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    symbol: str
    category: str
    data: list[ByBitResponseKlineScheme] | None = Field(alias="list", default=None)
