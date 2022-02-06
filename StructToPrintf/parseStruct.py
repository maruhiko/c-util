import re

def parseStruct(fileName):
    file = open(fileName, 'r')
    fileContent = file.read()
    file.close()

    struct = re.findall('[typedef +]?struct.*?{.*?}.*?;', fileContent, re.S)
    
    dict = {}
    for content in struct:
      element = re.split('[\{\}]', content)
      body = element[1].split(';')
      name = element[2].strip(';').strip()
      field_to_type = {}
      for field in body:
        if field.strip() != '':
          field = field.split()
          field_to_type[field[1].strip()] = field[0].strip()
      dict[name] = field_to_type
    
    # print(dict)
    return dict
