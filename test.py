def hoge1():
    raise ValueError('error!!')

def hoge2():
    hoge1()

print('python desu.')
hoge2()

