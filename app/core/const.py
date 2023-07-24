from datetime import datetime, timedelta


FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')
TO_TIME = (
    datetime.now() + timedelta(hours=1)
).isoformat(timespec='minutes')
MIN_LEGTH_PROJEKT = 1
MAX_LEGTH_PROJEKT = 100
START_INVERSED_AMOUNT = 0
EXAMPLE_FULL_AMOUNT = 10000
EXAMPLE_INVERSET_AMOUNT = 100
EXAMPLE_DESCRIPTION = 'На помощь бэкенд разрабам'
A1 = 'Отчет от'
A2 = 'Топ проектов по скорости закрытия'
A3 = 'Название проекта'
B3 = 'Время сбора'
C3 = 'Описание'
FORMAT = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_TITLE = 'Отчет от {}'
LOCALE = 'ru_RU'
SHEET_TITLE = 'Закрытые проекты'
ROW_COUNT = 30
COLUMN_COUNT = 3
RANGE = 'A1:C30'
