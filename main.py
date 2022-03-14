from pathlib import Path
print(Path.cwd())

if True:
  import subprocess, sys, glob, os, psutil, sqlite3, math
  from subprocess import Popen, PIPE
  from webserver import keep_alive
  
  for proc in psutil.process_iter():
      if proc.name() == 'python3.8':
          proc.terminate()
  for p in psutil.process_iter():
      print(p)



  conn = sqlite3.connect("Tg.db", check_same_thread=False)
  cursor = conn.cursor()
  keep_alive()
  cursor.execute("""CREATE TABLE IF NOT EXISTS online_bot(
    "id"  INT, 
    "name"  TEXT); 
  """)


  dels = []
  all = []
  # & python3 Premium_script.py 
  text = "python3 bot.py "
  for row in cursor.execute(f"SELECT * FROM online_bot;"):
    if os.path.isfile(f'User_self_bot/{row[1]}'):
      if row in all:
        dels.append(row[1])
      else:
        all.append(row)
      
    else:
      print("F")
      dels.append(row[1])
      

  for row in dels:
    sql_update_query = """DELETE from online_bot where name = ?"""
    cursor.execute(sql_update_query, (row[1], ))
    conn.commit()

  for xx in all:
    text = text + f"& python3 User_self_bot/{xx[1]}"
  print(len(all))
  print(text)
  print("-=-=-=-=-=-=-=-=-=-=")
  subprocess.run(text, shell=True)
  








# ll_f = glob.glob("User_self_bot/*.py")
# # all_f.remove('main.py')
# # all_f.remove('bot.py')



# for x in all_f:
#   text = text + f"& python3 {x} "






# 

# for file in glob.glob("*.py"):
#   print(file)
#   if file != "bot.py" or file != "main.py":
#     text = text + f"& python3 {file}"

# print(text)
# subprocess.run(text, shell=True)

# dir = os.path.abspath(os.curdir)

# fa = [sys.executable]
# os.chdir(dir)
# for file in glob.glob("*.py"):
#     fa.append(file)
# fa.remove('main.py')
# subprocess.run(fa, shell=True)
# print(fa)
# # subprocess.Popen(fa)