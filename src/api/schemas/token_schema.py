from pydantic import BaseModel


class TokenHeaderSchema(BaseModel):
    """
    Token schema for the API.
    """
    model_config = {'extra': 'forbid'}

    key: str
    value: str

    @property
    def with_typo(self) -> str:
        return "Bearer " + self.value
