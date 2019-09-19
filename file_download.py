import requests
import urllib3

crops_directory = '/crops_directory/'
images_directory =  '/images_directory/'

for file in open('crops.txt'):

    file_name = file.split('/')[-1]
    http = urllib3.PoolManager()
    r = http.request('GET', file)
    print(r.data)
    break

    output = open(file_name, 'wb')
    output.write(resource.read())
    output.close()
