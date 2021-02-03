class RevealAccess(object):
    """通常と同じようにデータの設定を行うが、アクセスされたログメッセージを残すデータディスクリプタ"""
    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name
    def __get__(self, obj, ovjtype):
        print("取得", self.name)
        print(self.val)
    def __set__(self, obj, val):
        print("更新", self.name)
        self.val = val
        print(self.val)

class MyClass(object):
    x = RevealAccess(10, '変数 "x"', )
    y = 5

m = MyClass()
m.x      
m.x = 20  
m.x                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       