# Payment-System-RR :raised_hands:
Тестовое задание на позицию Python-разработчика в компанию "Рабочие Руки"
## Технологии :pager:
- Python 
- mysqlclient
- Django 
- python-dotenv
- poetry 

Конкретные версии можете увидеть в файле `pyproject.toml`

## Запуск :dizzy:

Для работы требуется версия **Python 3.9.22** и Poetry

Для установки зависимостей выполните следующие шаги.

1. Установите дев пакет 
```bash
sudo apt install python3.9-dev
```
2. А также следущие зависимости
```bash
sudo apt-get install pkg-config default-libmysqlclient-dev build-essential
```
3. Теперь можно установить непосредственно все указанное в `pyproject.toml`
```bash
poetry lock;
poetry install;
```

