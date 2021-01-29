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
