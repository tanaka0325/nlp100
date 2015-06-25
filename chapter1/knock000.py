# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

s = "stressed"

def reverse(s: str) -> str:
    list = []

    for char in s:
        list.insert(0, char)

    return "".join(list)

print(reverse(s))
