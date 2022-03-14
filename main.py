import time

def bahceli(n):
  n = str(n)
  v = n.replace("0", "")
  m = v
  o = []
  for i in m:
    o.append(i)  
  f = ""
  for i in o:
    i = str(i)
    f = f + i     
  o = list(map(int, o))
  o = sum(o)

  f = int(f)

  print(f"{n} deki sifirlari sildiniz, ne kaldi")
  time.sleep(1)
  print(v)
  time.sleep(1)
  print("topladiniz ne geldi")
  time.sleep(1)
  print(o)
  time.sleep(1)
  print(f"{v} ile {o} toplayin ne yapar?????")
  time.sleep(2)
  print(f"{o+f} YAPAR!!!!!!!!!!! ve milliyetci hareket partisinin {o+f}. yili kutlu olsun")
  

bahceli(int(input('give n\n')))
