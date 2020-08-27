# 转换json
import json

data = {
    'name':'python',
    'shares':100
}
res = json.dumps(data)
print(res)

# 字典写入json文件
with open('dict_to_json.json','w') as f:
   json.dump(data,f)

# 加载json
json_data = json.loads(res)
print(json_data)

# json读取json文件
with open('dict_to_json.json','r') as f:
    data = json.load(f)
    print(data)
