from core.config import settings
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr
from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    """
    adding a base id through the class IntIdPkMixin mixin in the int_id_pk.py file
    """
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"
