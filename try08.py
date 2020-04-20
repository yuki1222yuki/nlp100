def cipher(target, key):
    result = ''
    for letter in target:
        if letter.islower():
            #ord():アスキーコードを取得
            #chr():アスキーコード->文字
            result += chr(key - ord(letter))
        else:
            result += letter
    return result


target = input('なんか入れて=>')
key = int(input('暗号鍵的なやつ=>'))

# 暗号化
target_enc = cipher(target, key)
print("暗号化：" + target_enc)
print(ord(target_enc))
# 復号
target_dec = cipher(target_enc, key)
print("復号：" + target_enc)

# チェック
print(target == target_dec)

# めも(219から文字コードを引く理由)
# 次式で文字を暗号化
# key - 文字コード(A) = 文字コード(B)
# 移項してなんやかんや
# key - 文字コード(B) = 文字コード(A)
# ということで、関数を使いまわして復元はできる
# が、関数の特性上、入力が小文字でないと文字変換ができない
# a->97 z->122　から、変換する文字コードの範囲は[97,122]
# keyを97+122=219にするとa->z, b->y, c->xと逆順に変換可能になる

