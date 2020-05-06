import MeCab

tagger = MeCab.Tagger("-O wakati")
text = '東京都の桜'
print(tagger.parse(text))
