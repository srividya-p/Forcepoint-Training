try:
    file = open('test.txt', 'r') #a+
    file.write('Test String 1\n')
    file.seek(0)
    print(file.read())
except Exception as e:
    print(e)
finally:
    file.close()