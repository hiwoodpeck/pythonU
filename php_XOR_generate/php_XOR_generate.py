# coding:utf-8
import argparse


def chrXORCreat(ch=''):
    return f(bin(ord(ch))[2:], 0, "", "")


def f(ch, index, chr1, chr2):
    if len(ch) <= index:
        if int(chr1, 2) >= 32 and int(chr1, 2) >= 32:
            return chr(int(chr1, 2)), chr(int(chr2, 2))
        else:
            return ""
    else:
        if ch[index] == "1":
            result = f(ch, index + 1, chr1 + "0", chr2 + "1")
            if result == "":
                return f(ch, index + 1, chr1 + "1", chr2 + "0")
            else:
                return result
        else:
            return f(ch, index + 1, chr1 + "1", chr2 + "1")


parser = argparse.ArgumentParser(description='输入字符获取PHP异或运算的两个可行字符.')
parser.add_argument('-s', '--str', type=str, help='输入字符', required=False)
parser.add_argument('-c', '--constr', type=str, help='默认为PHP字符的连接符“.”', required=False)
args = parser.parse_args()

if args.str:
    s = args.str
else:
    s = input("请输入参数:")
if args.constr:
    constr = args.constr
else:
    constr = "."
for i in range(len(s)):
    if i + 1 == len(s):
        constr = ""
    item1, item2 = chrXORCreat(s[i])
    print(f"('{item1}' ^ '{item2}')", end=constr)
