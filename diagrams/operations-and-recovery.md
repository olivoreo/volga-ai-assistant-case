# Схема 5 — развёртывание и восстановление

Схема показывает жизненный цикл версии без раскрытия реальной сети и инфраструктурных адресов.

~~~mermaid
flowchart LR
    revision[Ревизия кода] --> ci[Сборка и проверки]
    ci --> images[Неизменяемые образы]
    images --> migrations[Миграции базы данных]
    migrations --> deploy[Запуск новой версии]
    deploy --> readiness{Readiness успешен?}
    readiness -- Да --> runtime[Обработка запросов]
    readiness -- Нет --> rollback[Возврат предыдущей версии]
    runtime --> monitoring[Health и мониторинг очередей]
    runtime --> backups[Резервные копии]
    backups --> restore[Проверяемая процедура restore]
~~~
