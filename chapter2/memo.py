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


