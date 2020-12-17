import json
import os
import shutil
import zipfile


try:
    with open('Build.json') as f:
        data = json.loads(f.read())

        for x in data:
            StageName =  data[x]['Name']
            StageContent = data[x]['Content']

            if not os.path.exists('builds'):
                os.makedirs('builds')

            filepath = os.path.join("builds", StageName)   

            with open(filepath, 'w') as json_file:
                json.dump(StageContent, json_file)  

    shutil.make_archive('builds', 'zip', 'builds') 

finally:
    f.close()
    json_file.close()
