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