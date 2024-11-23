from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import GUID
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from core.models import Base
from core.models.types.user_id_type import userIdType


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class AccessToken(Base, SQLAlchemyBaseAccessTokenTableUUID[userIdType]):
    user_id = mapped_column(
            GUID, ForeignKey("users.id", ondelete="cascade"), nullable=False
        )
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)