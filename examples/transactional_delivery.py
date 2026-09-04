"""Синтетический пример транзакции. Это не production-код."""

from dataclasses import dataclass
from types import TracebackType
from typing import Protocol


@dataclass(frozen=True)
class StoredMessage:
    id: str
    text: str


class UnitOfWork(Protocol):
    async def __aenter__(self) -> "UnitOfWork": ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None: ...
    async def add_message(self, text: str) -> StoredMessage: ...
    async def add_delivery_job(self, message_id: str) -> None: ...


async def persist_reply(uow: UnitOfWork, text: str) -> StoredMessage:
    """История и намерение доставки фиксируются вместе либо не фиксируются."""
    async with uow:
        message = await uow.add_message(text)
        await uow.add_delivery_job(message.id)
        return message
