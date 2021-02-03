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


'''
プロパティは属性とそれを処理するメソッドをリンクさせる組み込みディスクリプタ型を提供する
プロパティはfget引数と3つのオプション(fset, fdel, doc)引数をとる
メンテナンス性の面で、プロパティを作成する最良の構文はpropateyデコレーターを使用すること
'''

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    def _width_get(self):
        return self.x2 - self.x1
    def _width_set(self, value):
        self.x2 = self.x1 + value
    def _height_get(self):
        return self.y2 - self.y1
    def _height_set(self, value):
        self.y2 = self.y1 + value
    
    width = property(
        _width_get, _width_set,
        doc = "左辺から測定した矩形の幅"
    )
    height = property(
        _height_get, _height_set,
        doc = "上辺から測定した矩形の高さ"
    )
    def __repr__(self):
        return "{}({}, {}, {}, {})".format(self.__class__.__name__, self.x1, self.y1, self.x2, self.y2)


rectangle = Rectangle(10, 10, 25, 34)
print(rectangle.width, rectangle.height)
rectangle.width = 100
print(rectangle)
rectangle.height = 100
print(rectangle)
print(help(Rectangle))

'''
プロパティの動作の一部だけをオーバーライドすることは推奨されない
プロパティの動作を変更する必要があるときは親クラスの実装を借りずに
プロパティ用の全てのメソッドを派生クラスで書き換えることをオススメする
'''

'''
クラスに対して__slots__という名前で属性名のリストをセットすることで
クラスをインスタンス化した時に__dict__が作成されなくなる
この機能は属性が少ないクラスにおいて、全てのインスタンスで__dict__を作らないことで
メモリ消費を節約することを目的とする
'''

'''
メタクラスは他の型(クラス)を定義する型(クラス)
オブジェクトのインスタンスを定義するクラスもオブジェクト
基本的なクラス定義で使われるのは組み込みのtypeクラス
pythonではクラスオブジェクトのメタクラスを独自の型に置き換えられる
通常新しいメタクラスはtypeクラスのサブクラスを利用する
'''

'''
PEP8にある命名規則の例
名前付のベストプラクティス
スタイルガイドに準拠しているか確認するツール
'''

'''
・変数
・関数とメソッド
・プロパティ
・クラス
・モジュール
・パッケージ
'''


'''
変数
・定数
・バブリックもしくはプライベート変数
'''

定数：UPPER_CASE_WITH_UNDERSCORES

'''
Djangoではsettings.pyという名前のモジュールに内に初期値に関する全ての定数を集約
'''

パブリックで変更可能なグローバル変数：lower_case_with_underscores


'''
ブール値の名前の前にhasかisをつける
'''