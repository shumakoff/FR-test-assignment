Тестовое задание для Фабрики Решений
===

Деплой
===
1. ```virtualenv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. В каталоге проекта: ```./manage.py migrate```
5. В каталоге проекта: ```./manage.py createsuperuser```
6. В каталоге проекта: ```./manage.py test```

Описание API
===

Авторизация
====
* **POST /api-token-auth/** - Эндпоинт для авторизации, возвращает токен для авторизации; 
    Пример запроса: ```{"username": <username>, "password" <password>}```
    Полученный токен необходимо передавать в заголовке HTTP ```Authorization```, например так: ```curl 'http://127.0.0.1:8000/api/v1/surveys/' -X GET -H 'Content-Type: application/json' -H 'Authorization: Token <token>'```

Опросы
====
* **GET /api/v1/surveys/** - Возвращает список опросов;
* **GET /api/v1/surveys/<survey_id>/** - Возвращает информацию о конкретном опросе;
* **POST /api/v1/surveys/** - Создает опрос; Пример запроса: ```{"name":"Test survey","start_date":"2021-09-07","end_date":"2021-09-10","description":"No description"}```; Пример ответа: ```{"status":"OK","survey_id":9}```
* **PUT /api/v1/surveys/<survey_id>/** - Изменяет опрос;
* **DELETE /api/v1/surveys/<survey_id>/** - Удаляет опрос;

Вопросы
====
* **GET /api/v1/survey/<survey_id/questions/** - Возвращает вопросы в опросе;
* **POST /api/v1/questions/** - Создает новый вопрос для опроса; 
    Пример запроса: ```{"survey":<survey_id>,"text":<question_text>,"qtype":<type_of_question>```;
    Примечания: ```type_of_question``` может быть ```text```, ```select```, ```select_multiple```, для текстового ответа, ответа с выбором одного варианта и ответа с выбором нескольких вариантов, соответственно;
* **PUT /api/v1/questions/<question_id>/** - Изменяет вопрос;
* **DELETE /api/v1/questions/<question_id/** - Удаляет вопрос;

Варианты ответов
====
* **GET /api/v1/question/<question_id>/choices/** - Возвращает варианты ответов в вопросе; 
* **POST /api/v1/choices/** - Создает вариант ответа для вопроса; Пример запроса: ```{"question":<question_id>,"answer":<anwer_text>}```
* **PUT /api/v1/choices/<choice_id>/** - Изменяет вариант ответа для вопроса; Пример запроса: ```{"question":<question_id>,"answer": <anwer_text>}```
* **DELETE /api/v1/choices/<choice_id>/** - Удаляет вариант ответа для вопроса;

Голосование
====
* **GET /api/v1/surveys/active/** - Возвращает активные опросы;
* **POST /api/v1/voting/** - Передача информации и выбранном варианте в вопросе; Пример запроса: ```{"user_id":<user_id>,"question":<question_id>,"answer": [<choice_id>]}``` или ```{"user_id":<user_id>,"question":<question_id>,"answer": "<text_answer>"}```;
* **GET /api/v1/voting/<user_id>/** - Возвращает пройденные пользователем опросы с детализацией по ответам;
