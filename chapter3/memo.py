'''
組み込み型のサブクラス化
スーパークラスのメソッドへのアクセス
プロパティとスロット
メタプログラミング
'''

'''
pythonは組み込み型のサブクラスを作るのが簡単
objectと呼ばれる組み込み型が、全てのクラス組み込み型の共通クラス、
あるいは明示的に親クラスを指定しなかったユーザー定義の親クラスになる
'''

'''
組み込み型と似た挙動をするクラスを定義するときは、その組み込み型の
サブクラスを作るのがベストプラクティス
'''

class DistinctError(ValueError):
    """
    distinctdictに重複した値を追加したときに上がる例外
    """

class distinctdict(dict):
    """重複した値を登録できない辞書"""
    def __setitem__(self, key, value):
        if value in self.values():
            if ((key in self and self[key] != value) or key not in self):
                raise DistinctError("この値はすでに別のキーで登録されています")
        super().__setitem__(key, value)

'''
組み込み型superを使用するとオブジェクトのスーパークラスが持つ属性にアクセスできる
'''

class Mama:
    def says(self):
        print("宿題をしなさい")

class Sister(Mama):
    def says(self):
        Mama.says(self)
        print("後宿題もしなさい")

class Sister(Mama):
    def says(self):
        super(Sister, self).says()
        print("後宿題もしなさい")

class Sister(Mama):
    def says(self):
        super().says()
        print("後宿題もしなさい")


'''
superの重要な点として、2つ目の引数を省略する使い方がある
最初の引数だけが指定された場合、superはインスタンスに束縛されていない型を返す
これは親クラスのclassmethodを呼び出すときに便利
'''
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    def __repr__(self):
        return "と".join(self.toppings) + "がトッピングされたピザです"

    @classmethod
    def recommend(cls):
        """オススメピザの紹介"""
        return cls(['スパム', 'ハム', '卵'])

class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """スパムを大量に追加"""
        recommended = super(VikingPizza).recommend()
        recommended.toppings += ['スパム'] * 5
        return recommended

'''
多重継承階層を使用する場合、主にクラスの初期化が原因でカナリ危険な状態になる
pythonでは基底クラスの__init__()が暗黙的に呼び出されない
基底クラスの__init__()は開発者の責任
'''

'''
多重継承を避ける
superの使用に一貫性を持たせる
階層に含まれる全てのクラスでsuperを使用するか、逆に一切superを使用しないかどちらかにすべき
コードを明示的にするためにsuperは避けられる傾向にある
'''

'''
pythonにプライベートキーワードがない
名前マンドリンぐ
属性の頭に__をつけると裏でインタープリタが違う名前にする
名前マンドリングは継承時の名前衝突を避ける仕組み
属性の名前をクラスの名が頭についた名前にリネームする
パブリックではない属性を表現するためには、一般的に頭に_をつける
これは名前マンドリングせずに、単に開発者に対して、その属性がクラスのプライベート要素であるという意図を伝える表現
'''

'''
pythonにはクラスのパブリックな部分をプライベートなコードと共に構築するための仕組みがある
ディスクリプた
プロパティ
クリーンなAPI設計をするためにはこれらを使用すべき
'''

'''
ディスクリプタを使用するとオブジェクトの属性が参照された時の動作をカスタマイズできる
ディスクリプタはクラスの属性に対するアクセスを制御するためのクラス
ディスクリプタプロトコルを構成する4つの特殊メソッドをベースにしている
'''

'''
__set__(self, object, type=None)
属性がセットされる時に呼ばれる：セッター

__get__(self,obj, value)
属性が読み込まれる時に呼ばれる:ゲッター

__delete__(self, obj)
属性に対してdelが実行された時に呼ばれる

__set_name__(self, owner, name)
ディスクリプタが他のクラスに追加された時に対象のクラスと属性名を伴って呼ばれる
'''

'''
__getattribute__()メソッドが属性を参照する時にこれらのディスクリプタプロトコルを呼び出す
1.インスタンスに設定されているオブジェクトクラスにおいて、この属性がデータディスクリプタであるか検証
2.もしそうであれば、その属性がインスタンスオブジェクトの__dict__に存在いているか調べる
3.最後に、インスタンスに設定されているクラスオブジェクトにおいて、この属性が非データディスクリプタであるか確認
'''

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