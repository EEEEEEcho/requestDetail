import requests
html = requests.options("https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&hd=0&latest=0&copyright=0&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn=30&rn=30&gsm=1e&1595690436389=")
# html.encoding="utf-8"
if html.status_code == 200:
    content = html.json()['data']
    for item in content:
        try:
            print(item['replaceUrl'][1]['ObjURL'])
        except:
            print("无原图")
# print(html.text)