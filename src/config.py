import json

configFile = open('conf/setting.json', 'r')
content = configFile.read()
dictConfig = json.loads(content)
print(type(dictConfig))
print(dictConfig)
configFile.close()
