"""Синтетическая граница приватности. Это не production-код."""

from typing import Protocol


class SanitizerUnavailable(RuntimeError):
    pass


class Sanitizer(Protocol):
    async def sanitize(self, raw_text: str) -> str: ...


class ExternalProcessor(Protocol):
    async def process(self, sanitized_text: str) -> str: ...


async def process_safely(
    raw_text: str,
    *,
    sanitizer: Sanitizer,
    external: ExternalProcessor,
) -> str:
    try:
        safe_text = await sanitizer.sanitize(raw_text)
    except Exception as exc:
        raise SanitizerUnavailable("Внешняя обработка заблокирована") from exc

    # Намеренного fallback на raw_text здесь нет.
    return await external.process(safe_text)
