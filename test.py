def hoge1():
    raise Error('error!!')

def hoge2():
    hoge1()

print('python desu.')
hoge2()

