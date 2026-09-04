# Схема 1 — контекст системы

Схема показывает границу продукта и внешние зависимости, но не порядок обработки сообщения.

~~~mermaid
flowchart TB
    user[Пользователь] --> messengers[VK / MAX / Telegram]
    staff[Оператор или администратор] --> admin[Admin UI]
    messengers <--> core[Ассистент «Волга»]
    admin <--> core
    core --> privacy[Privacy Gateway]
    core <--> db[(PostgreSQL)]
    core <--> redis[(Redis)]
    core -->|NLU для обычного текста| nlu[Dialogflow ES]
    core -.->|Только через Action Dispatcher| ai[AI Providers]
    core --> operations[Мониторинг и backup]
~~~
