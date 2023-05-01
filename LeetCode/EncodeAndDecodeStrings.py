#https://www.lintcode.com/problem/659/

def encode(strs):
    """
    For every String we will count the length and delimit it with that length & with "#". Such that it can
    be used in decode
    :param strs: ["wow","such","string"]
    :return: "3#wow4#such6#string"
    """
    ans = ""
    for string in strs:
        ans += str(len(string)) + "#" + string
    return ans


def decode(string):
    ans, i = [], 0

    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1
            length = int(string[i:j])
            ans.append(string[j + 1: j + 1 + length])
            i = j + 1 + length
    return ans

def encode1(strs):
    """
    use join and "#" to create an encoded string
    :param strs:
    :return:
    """
    return "#".join(strs)

def decode1(str):
    """
        A much simplier solution, but doesn't take into consideration that string could contain "#" so
    encoded a word expected to be "wo#w" would be split into "wo", "w" instead of "wo#w"
    :param str:
    :return:
    """
    return str.split("#")

