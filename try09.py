import random


def typoglycemia(target):
    result = ''
    # 前処理：','と'.'の前にスぺース追加
    target = target.translate(target.maketrans({'.': ' .', ',': ' ,'}))
    for word in target.split(' '):
        if len(word) > 4:
            # たぶんリストやないとシャッフルできない
            # [1:-1]2番目から最後ｰ1番目まで
            letter_list = list(word[1:-1])
            random.shuffle(letter_list)
            # 最初の文字にシャッフルした文字配列と最後の文字を足し合わせる
            result += word[0] + ''.join(letter_list) + word[-1] + ' '
        else:
            result += word + ' '
    return result[:-1]


sentence = input('なんか入力(英語)->')
print(typoglycemia(sentence))

# タイポグリセミア
# さしいょ と さいご が あるっていと なぜか よめゃちう
# ふぎしな げしんょう のこと。にげんん の にきのんちう
# は　すいごね。
