from backend.db import engine, Base
from models import user, task 

Base.metadata.create_all(bind=engine)
print("Таблицы успешно созданы!")
