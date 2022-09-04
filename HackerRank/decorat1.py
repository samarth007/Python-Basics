


def main_wel(func):

    def sub_func():
      print('Inside Function')
      func()
      print('Inside done')
    return sub_func

@main_wel
def child():
    print('Child function')

print(child())