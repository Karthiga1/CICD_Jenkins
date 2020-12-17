import os
import zipfile

input1 = os.getenv("STAGE_NAME")
print("Running stage", input1)


if not os.path.exists(input1):
        os.makedirs(input1)

fh = open('builds.zip', 'rb')        
z = zipfile.ZipFile(fh)

z.extract(input1,input1)

print("Files copied in this stage:", input1)

fh.close()
z.close()