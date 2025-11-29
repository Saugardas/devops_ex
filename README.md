## Описание
Репозиторий для итогового задания по "Методам DevОps": Воспроизводимый DevOps-проект с нагрузочным тестированием

Для работы с ADR используется adr-tools, необходимо склонить в корне проекта: `git clone https://github.com/npryce/adr-tools.git`

Список решений лежит в [ard_records](https://github.com/Saugardas/devops_ex/tree/main/adr_records)

В качестве задачи выбрана задачи классификации ирисов с помощью метода k-ближайших соседеей.

## API

Сервис предоставляет следующие эндпоинты:

### `GET /health`
Проверка работоспособности сервиса.

Ответ:
```json
{"status": "ok"}
```

### `GET /predict`

Параметры:
* sepal_length — длина чашелистика (число)
* sepal_width — ширина чашелистика (число)

Пример запроса: `/predict?sepal_length=5.1&sepal_width=3.4`

Ответ:
```json
{"prediction": "Setosa"}
```

## Установка:

Ставим библиотеки:

`pip install -r requirements.txt`

Запускаем сервер:

`uvicorn app.main:app --reload`


## Анализ дрефа данных

Выполнен с помощью EvidentlyAI

Отчет сохранаяется в reports/evidently_report.html

Запуск анализа: `python scripts/generate_monitoring_report.py`

