import parseStruct

def convert_type_to_format(type):
  if type == 'char':
    return 's'
  elif type == 'int':
    return 'd'
  elif type == 'float':
    return 'f'
  elif type == 'double':
    return 'f'
  elif type == 'long':
    return 'ld'
  elif type == 'long long':
    return 'lld'
  elif type == 'short':
    return 'hd'
  elif type == 'unsigned char':
    return 's'
  elif type == 'unsigned int':
    return 'u'
  elif type == 'unsigned long':
    return 'lu'
  elif type == 'unsigned long long':
    return 'llu'
  elif type == 'unsigned short':
    return 'hu'
  elif type == 'void':
    return 's'
  else:
    return 's'

def createPrintFormat(dict):
  list = []
  for key, val in dict.items():
    head = 'printf(\"'
    text_format = '%s'
    params = f'\", \"{key}\"' 
    tail = ");"
    for name, type in val.items():
      text_format += f' {name}:%{convert_type_to_format(type)}'
      params += f', info.{name}'
    ret = head + text_format + params + tail
    print(ret)
    list.append(ret)
  return list


# if __name__ == '__main__':
#   createPrintFormat(parseStruct.parseStruct('test_sample_header.h'))


