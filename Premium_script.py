import datetime, time, sqlite3
from datetime import datetime
import bot

conn = sqlite3.connect("Tg.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS all_hel(
  "id"  INT, 
  "token" TEXT, 
  "pod" INT,
  "name_self" TEXT,
  "prefix"  TEXT); 
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time(
  "vr"  INT); 
""")



print("[СТАРТ] Отсчёт премиума запущен!")

if True:
  current_datetime = datetime.now()
  cursor.execute(f'INSERT INTO time VALUES ({current_datetime.hour})')
  conn.commit()

while True:
  current_datetime = datetime.now()
  for row in cursor.execute(f"SELECT * FROM time;"):
    roma = row[0]

  if roma == current_datetime.hour:
    pass
  else:
    print("[ОТКЛАДКА] Прошёл 1 час")
    for row in cursor.execute(f"SELECT * FROM all_hel;"):
      if row[2] != 0:
        wat = int(row[2]) - int(1)
        cursor.execute('UPDATE all_hel SET pod=? where id=?', (wat, row[0]))
        if wat == 0:
          bot.sendd(row[0], "*💫 У вас закончился Premium, если у вас был бот с ним то изменён на тыстовый*")
          
  time.sleep(120)

  