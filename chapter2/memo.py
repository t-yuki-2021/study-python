#バイトリテラル
t = type(b"some bytes")
print(t)

'''
文字列オブジェクトをバイトシーケンスにエンコードする方法は2つ
'''
str.encode(encoding, errors)
bytes(source, encoding, errors)


'''
文字列の連結
pythonの文字列がimmutable(不変)であることは、複数の文字列インスタンスを1つにする時に問題となる
immutableなシーケンを連結するたびに新しいシーケンスオブジェクトが作られる
最終結果の文字列の長さの二乗の実行コストがかる→非常に効率が悪い
'''
s = ''
for substring in substrings:
    s += substring

'''
str.join()メソッドが使える
文字列を格納した配列かタプルを引数に取り、結合した文字列を返す
メソッドなのでメソッドを提供するインスタンスとして空の文字列リテラルを使用
高速に処理される
'''

s = ''.join(substrings)


'''
pythonのコレクション
リスト、タプル、辞書、セット
リストは動的なのでサイズ変更できる
タプルはimmutableなので作成後の変更はできない
タプルはhashable(ハッシュ可能)
'''

events = []
for i in range(10):
    if i % 2 == 0:
        events.append(i)
print(events)

'''
この書き方はC言語は良いがpythonでは以下の理由で遅くなる
リストを操作するコードをループごとにインタプリタ上で処理する必要がある
カウンタの操作もインタプリタ上で処理する必要がある
append()はリストメソッドであるため、イタレーションごとに関数ルックアップの追加コストが必要になる
このパターンのコードを書く場合には、リスト内包表記を使用するべき
処理の一部がインタープリタ内部で実行されるようになるので処理が早くなる
'''

[i for i in range(10) if i % 2 == 0]


'''
辞書の作成に多くのif分が必要で複雑になる場合は単純なfor文を使用した方が良い
'''

'''
イテレーター:単にイテレータープロトコルを実装したコンテナオブジェクト
イテレータープロトコルとは
・コンテナなの次の要素を返す
・イテレーター自身を返す
>>> i = iter('abc')
>>> print(next(i))
a
>>> print(next(i))
b
>>> print(next(i))
c
>>> print(next(i))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
forはStopIterationの例外を捕まえるとループを終了するようになっている。
'''

'''
カスタムイテレーター
クラス内に__next__()メソッド
イテレーターのインスタンスを返す特殊メソッド__iter__()を提供
'''

'''
ジェネレーターはyield文を使って関数を一時的に停止させ途中経過の結果を返す
一時停止中も実行コンテキストが保存されているため必要であれば止まった場所から再実行できる
ループ処理やシーケンスを返す処理を実行する時はジェネレーターの利用を検討すべき
'''

'''
send()はyieldの返り値として送った値が返ってくる
外部のクライアントコードからジェネレーター内にデータを送ることができる
'''

'''
デコレーターは関数やメソッドのラッピング(受け取った関数を拡張して返す)処理の見た目を分かりやすくするために導入された
デコレーターを使用できるのは一般的に1つの引数(デコレーション対象)を受け取れる、名前付きcallable(呼び出し可能)オブジェクト
名前がつかないlambda構文は使用できない
'''

'''
デコレーター関数の中で元の関数を呼び出すサブ関数を定義し、それを返す方法がシンプル
'''
def mydecorator(function):
    def wrapped(*args, **kwargs):
        #実際の関数を呼び出す前に行う処理
        result = function(*args, **kwargs)
        #呼び出し後に行う処理
        return result
    #ラッパーをデコレーター済関数として返す
    return wrapped


'''
デコレーターが複雑なパラメーターを使う必要があったり、
状態に依存した動作をさせたい場合はクラスの方が適切
クラスを使ったパラメーターを使わないデコレーター
'''
class DecoratorAsClass:
    def __init__(self, function):
        self.function = function
    def __call__(self, *args, **kwargs):
        #実際の関数を呼び出す前に行う処理
        result = self.function(*args, **kwargs)
        #呼び出し後に処理を行い返り値を返す
        return result

'''
実際にデコレーターを作成すると、パラメーターを渡したいことがよくある
この関数がデコレーターとして使用されると2回ラップが行われる
'''
def repeat(number=3):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


'''
デコレーターはミドルウェアのように使用されて、
処理の流れを理解したりデバックするのが難しくなる
汎用的なラッパーに制限されるべき
デコレーターの一般的な使用方法のパターン
・引数チェック
・キャッシュ
・プロキシ
・コンテキストプロバイダ
'''