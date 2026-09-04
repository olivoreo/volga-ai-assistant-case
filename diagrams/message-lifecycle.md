# Схема 2 — жизненный цикл сообщения

Главная схема кейса: приём и очистка сообщения, Dialogflow ES, выполнение action и доставка через Outbox → Channel Router → Channel Adapter.

~~~mermaid
sequenceDiagram
    actor user as Пользователь
    participant platform as Платформа
    participant adapter as Channel Adapter
    participant privacy as Privacy Gateway
    participant db as PostgreSQL
    participant inbox as Inbox Worker
    participant dialogflow as Dialogflow ES
    participant dispatcher as Action Dispatcher
    participant ai as AI Module
    participant serviceBot as Service Bot
    participant outbox as Outbox Worker
    participant router as Channel Router

    user->>platform: Сообщение
    platform->>adapter: Событие платформы
    adapter->>privacy: Исходный текст
    privacy-->>adapter: Очищенный текст
    adapter->>db: Транзакция: сообщение + Inbox job
    db-->>adapter: Commit
    adapter-->>platform: Подтверждение

    inbox->>db: Получить Inbox job
    inbox->>dialogflow: Очищенный текст
    dialogflow-->>inbox: intent + action + fulfillment
    inbox->>dispatcher: Action и параметры

    alt Action вызывает AI Module
        dispatcher->>ai: Ограниченный контекст
        ai-->>dispatcher: Ответ
    else Action включает Manual Support
        dispatcher->>db: Изменить состояние диалога
        dispatcher-->>serviceBot: Уведомить сотрудника
    else Обычный сценарий
        dispatcher->>dispatcher: Подготовить обычный ответ
    end

    dispatcher-->>inbox: Результат сценария
    inbox->>db: Транзакция: ответ + Outbox job
    outbox->>db: Получить Outbox job
    outbox->>router: Готовое сообщение
    router->>adapter: Выбрать adapter по платформе
    adapter->>platform: Отправить ответ
    platform-->>user: Ответ
~~~
