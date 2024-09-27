from pydantic import BaseModel

class SchemaBaseTodo(BaseModel):
    title: str
    complete: bool = False

class SchemaTodo(SchemaBaseTodo):
    id: int

class SchemaUpdateTodo(BaseModel):
    title: str | None = None
    complete: bool | None = None