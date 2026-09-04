# Схема 4 — Dialogflow ES и Action Dispatcher

Схема показывает автоматический flow обычного текстового сообщения. Dialogflow ES определяет intent/action, а Action Dispatcher выполняет соответствующий сценарий.

~~~mermaid
flowchart TD
    message[Очищенное текстовое сообщение<br/>в Assistant mode] --> dialogflow[Dialogflow ES]
    dialogflow -->|intent + action + fulfillment| dispatcher[Action Dispatcher]
    dispatcher --> standard[Обычный сценарий]
    dispatcher --> eventExpert[Event Expert AI Module]
    dispatcher --> assistantAI[Assistant AI Module]
    dispatcher --> manual[(Manual Support<br/>состояние диалога)]
    standard --> reply[Ответ]
    eventExpert --> reply
    assistantAI --> reply
    manual --> admin[Admin UI]
    admin --> reply
    reply --> outbox[(Outbox)]
~~~
