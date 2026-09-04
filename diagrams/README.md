# Архитектурные схемы

Во всех схемах используются одни и те же названия компонентов: Channel Adapters, Privacy Gateway, Inbox, Dialogflow ES, Action Dispatcher, AI Modules, Manual Support, Outbox, Channel Router и Admin UI.

Схемы расположены в порядке технического обзора:

1. [Контекст системы](system-context.md) — пользователи, границы продукта и внешние зависимости.
2. [Жизненный цикл сообщения](message-lifecycle.md) — надёжный путь от приёма до доставки.
3. [Граница приватности](privacy-boundary.md) — разделение исходного и очищенного текста.
4. [Маршрутизация NLU и AI](hybrid-routing.md) — Dialogflow ES, Action Dispatcher, AI Modules и состояние Manual Support.
5. [Развёртывание и восстановление](operations-and-recovery.md) — выпуск версии, readiness, откат и backup.

Каждая схема отвечает на один вопрос и не раскрывает production-топологию, адреса, размеры инфраструктуры и данные аккаунтов.
