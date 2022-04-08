#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR: Electric Sheep
VERSION: v2022.04.08
"""
import re, sys, getopt

def phin2ipa_A(s):
    "將拼音轉換爲IPA，省志音系"
    s = s.lower()
    # 轉換聲調
    tone = ["13", "33", "55", "24", "324"]
    for j in range(5):
        s = re.sub(r"(?<=[a-z])"+str(j+1)+r"\b", tone[j], s)
    # 轉換聲母
    s = re.sub(r"\b([ptck]|ts)h", r"\1ʰ", s)
    s = re.sub(r"\bc", r"tɕ", s)
    s = re.sub(r"\bsh", r"ɕ", s)
    s = re.sub(r"\bzh", r"ʑ", s)
    s = re.sub(r"\bng", r"ŋ", s)
    s = re.sub(r"\bgh", r"ɣ", s)
    s = re.sub(r"\bh", r"x", s)
    s = re.sub(r"\byi|\by(?=a|e|o)", r"i", s)
    s = re.sub(r"\bwu|\bw(?=a|e|o)", r"u", s)
    s = re.sub(r"\byu", r"y", s)
    # 轉換韻母
    s = re.sub(r"(s|z|sʰ)i", r"\1ɿ", s)
    s = re.sub(r"nyu", r"ny", s)
    s = re.sub(r"(ɕʰ?|ʑ)u", r"\1y", s)
    s = re.sub(r"ao", r"au", s)
    s = re.sub(r"ou", r"əu", s)
    s = re.sub(r"u(i|n)", r"ue\1", s)
    s = re.sub(r"yi", r"yei", s)
    s = re.sub(r"iu", r"iəu", s)
    s = re.sub(r"ou", r"əu", s)
    s = re.sub(r"ang", r"ã", s)
    s = re.sub(r"an", r"ẽ", s)
    s = re.sub(r"m(\d|\b)", r"m̩\1", s)
    s = re.sub(r"ng(\d|\b)", r"ŋ\1", s)
    s = re.sub(r"\bŋ(\d|\b)", r"ŋ̍\1", s)
    # 聲調上標
    s = re.sub(r"1", r"¹", s)
    s = re.sub(r"2", r"²", s)
    s = re.sub(r"3", r"³", s)
    s = re.sub(r"4", r"⁴", s)
    s = re.sub(r"5", r"⁵", s)
    return s

opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:")
for opt, arg in opts:
    if opt == "-i":
        input_file = arg
    elif opt == "-o":
        output_file = arg
    elif opt == "-f":
        function = arg
    elif opt == "-h":
        print(
"""
Usage:
  ./yunciu.py -i <file> -o <file> -f <option>

Options:
  -i <file>            input file
  -o <file>            output file
  -f <option>          fuction dealing with the file
  -h                   Display this information

These fuctions are avalible:
  phin2ipa_A             將拼音轉換爲IPA，省志音系
"""
)
        sys.exit()

with open(input_file, "r", encoding="utf-8") as f_input:
    s = f_input.readlines()
f_input.closed

s = [eval(function)(i) for i in s]

with open(output_file, "w", encoding="utf-8") as f_output:
    [f_output.write(i) for i in s]
f_output.closed
