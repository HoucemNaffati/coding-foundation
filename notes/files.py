storage = open('water.txt', 'w')

date_str = str(datetime.datetime.now())
storage.write(date_str)

storage.close()

# ==========================

storage = open('water.txt', 'r')

for line in storage.readlines():
    print(line)

storage.close()
