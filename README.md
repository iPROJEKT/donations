# приложение QRKot
### Описание
Благотворительный фонд поддержки котиков - QRKot. 
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
### Проекты
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
### Так же появилас возможность
QRKot может формировать отчёт в гугл-таблице. В таблице будут закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму
### Пользователи
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
### Пример env
```python
APP_AUTHOR= Автор
AUTHOR_PASS= Пароль
DEADLINE_DATE= Время
DATABASE_URL= База (sqlite+aiosqlite:///./fastapi.db)
SECRET = Секрет
FIRST_SUPERUSER_EMAIL= Имя супер юзера
FIRST_SUPERUSER_PASSWORD = Пароль от супер юзера
type: Optional[str] = None              |
project_id: Optional[str] = None        |
private_key_id: Optional[str] = None    |
private_key: Optional[str] = None       |  Параметры из json google
client_email: Optional[str] = None      |
client_id: Optional[str] = None         |
auth_uri: Optional[str] = None          |
token_uri: Optional[str] = None         |
auth_provider_x509_cert_url:            |
client_x509_cert_url:                   |
email твой маил
```

### python + FastAPI + SQLAlchemy + google 
