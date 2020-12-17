import json
import os
import shutil
import zipfile

source = 'C:/Users/kg52/OneDrive - DXC Production/Documents/Model/person.txt'
destination = 'C:/Users/kg52/OneDrive - DXC Production/Documents/Model/builds'

try:
  with open('C:/Users/kg52/OneDrive - DXC Production/Documents/Model/Build.json') as f:
    y = json.dumps(f.read())
    data = json.loads(f.read())
    parseFiles = []

    for d in data:
      print(d)
      #name = d['name']
      #content = d['content']
      #print(d('Name'))
      #print(d['content'])

    #print(data['Stage1'])
    #data1 = data['Stage1']
    #print(data1['Name'])
    #data2 = data1['Name']

    #if not os.path.exists('builds'):
    #    os.makedirs('builds')

    #dest = shutil.move(source, destination)     
    #shutil.make_archive('builds', 'zip', root_dir='.')


    
    #with open('person.txt', 'w') as json_file:
    #        json.dump(data, json_file) 
finally:
    f.close()


