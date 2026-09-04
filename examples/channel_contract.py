"""Синтетический пример для публичного кейса. Это не production-код."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Mapping, Protocol


class Channel(StrEnum):
    ALPHA = "alpha"
    BETA = "beta"


@dataclass(frozen=True)
class Address:
    channel: Channel
    conversation_id: str


@dataclass(frozen=True)
class IncomingEvent:
    provider_event_id: str
    sender: Address
    text: str
    metadata: Mapping[str, Any]


class EdgeAdapter(Protocol):
    """Интерфейс, за которым остаются особенности конкретной платформы."""

    def verify(self, headers: dict[str, str], body: bytes) -> None: ...

    def normalize(self, body: bytes) -> IncomingEvent: ...

    async def send(self, target: Address, text: str) -> str: ...
