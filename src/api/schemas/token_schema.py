from pydantic import BaseModel

from typing import Annotated


class TokenSchema(BaseModel):
    """
    Token schema for the API.
    """
    model_config = {'extra': 'forbid'}

    value: Annotated[str, "JWT token"]

    @property
    def with_typo(self) -> str:
        return "Bearer " + self.value
