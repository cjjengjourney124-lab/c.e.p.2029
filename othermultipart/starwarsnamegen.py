def starwarsnamegen():
  import os, time
  print("STAR WARS NAME GENERATOR")
  swn = []
  def stwng():
    print()
    for name in swn:
      print(f"{name} is your STAR WARS name!")
      print()

  first = input("FIRST NAME: ").strip().lower().capitalize()
  last = input("LAST NAME: ").strip().lower().capitalize()
  maiden = input("MOTHERS MAIDEN NAME: ").strip().lower().capitalize()
  city = input("CITY YOU WERE BORN IN: ").strip().lower().capitalize()
  os.system("clear")
  name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"
  swn.append(name)
  print("loading...")
  time.sleep(3)
  os.system("clear")
  stwng()
  time.sleep(3)
  os.system("clear")
  swn = []
