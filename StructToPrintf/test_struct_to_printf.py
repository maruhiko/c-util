from tkinter import W
import unittest
import parseStruct
import print_format

class TestStructToPrintf(unittest.TestCase):
  def test_parse_struct(self):
    fileName = './test_sample_header.h'
    dic = parseStruct.parseStruct(fileName)
    expect = {'HOGE2': {'a': 'long', 'b': 'HOGE', 'c': 'float'},'HOGE': {'a': 'int', 'b': 'char*'}} 
    self.assertDictEqual(dic, expect)

  def test_print_format(self):
    fileName = './test_sample_header.h'
    dic = parseStruct.parseStruct(fileName)
    ret = print_format.createPrintFormat(dic)
    expect = ['printf("%s a:%d b:%s", "HOGE", info.a, info.b);', 'printf("%s a:%ld b:%s c:%f", "HOGE2", info.a, info.b, info.c);']
    self.assertEqual(ret, expect)


if __name__ == '__main__':
  unittest.main()