"""Синтетический жизненный цикл AI-квоты. Это не production-код."""

from typing import Protocol


class Reservation(Protocol):
    async def commit(self) -> None: ...
    async def release(self) -> None: ...


class Quota(Protocol):
    async def reserve(self, actor_id: str) -> Reservation: ...


class Model(Protocol):
    async def answer(self, prompt: str) -> str: ...


async def answer_with_quota(
    actor_id: str,
    prompt: str,
    quota: Quota,
    model: Model,
) -> str:
    reservation = await quota.reserve(actor_id)
    try:
        answer = await model.answer(prompt)
    except BaseException:
        # Квота освобождается и при отмене coroutine, а не только при обычной ошибке.
        await reservation.release()
        raise
    else:
        await reservation.commit()
        return answer
