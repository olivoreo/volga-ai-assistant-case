# Схема 3 — граница приватности

Схема показывает место Privacy Gateway в общем pipeline и разделяет исходный и очищенный текст.

~~~mermaid
flowchart LR
    subgraph local[Контролируемый контур]
        incoming[Входящий текст] --> history[(Исходная история)]
        incoming --> gateway[Privacy Gateway]
        gateway --> clean[(Очищенный текст)]
        history --> staff[Авторизованный сотрудник]
        clean --> dialogflow[Dialogflow ES]
    end
    dialogflow --> dispatcher[Action Dispatcher]
    dispatcher --> ai[AI Modules]
    gateway -. ошибка .-> blocked[Внешний вызов запрещён]
    history -. запрещено .-> dialogflow
    history -. запрещено .-> ai
~~~
