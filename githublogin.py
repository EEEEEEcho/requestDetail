# coding=utf8
# 模拟登录github
import requests
import time

headers = {
    "Cookie": "_octo=GH1.1.1969675729.1595836364; logged_in=no; _ga=GA1.2.1973480592.1595899507; _gat=1; tz=Asia%2FShanghai; _device_id=19195ba71665b47fb4a8df28faeebc31; has_recent_activity=1; _gh_sess=6Id4%2FS4jMdSD8mUvoWgmZVUeGtGeia64EwvKQxf8PelO70BnvHIHjNrKcT47gcbGgRpf%2FmARNapWUC8ZN%2FMyHL658oRdb2SOhrmY5dvQcstfsnmFh2nSa5qvDyzMNPxgdpib3NxfoRgZAM848%2Boee%2FXFaEeop0iJjw3Zn%2Fa1b%2BX9QUkoWPJbAbtn0prcG7uGZonBa0zLjMOd%2BTV3L9xazjVfNXXE%2BlW2b%2FImF2nBy9W183IT5vVidmCIe4oRX8J1U9ch5FKQkSO2uvoQXiF5UY5tYyn91OULGAhe5vik0s%2BF35sstOlGI%2FxEtogn6GGrb3MZ4aBVIEdbHOGaY4YKLiQEovjrZs0eNM1mGjDAfM3JGQwheHYH6OEaFifAyMuPCDJzKDFeNLlD1flO0C93FB%2FkWpmP%2FQBNfECWjJITEqEffkqEl8EFjsjkhtPiFPbuhLsuRAf40nxGXUUAhFanynShlBaokETN8CV3tcQTQ3k1rbVzwvhsO1PFVEJr7A7yPGXmI0jAsy3MBfhhLXCvv4VYE6wGSngU1wRbiBqY61oY85KuZg4wlRXD%2Fny0F8SB4QnynxBqKo9D2Vt5uVFYXbBU6piSPNvZzL4E2mbkMlNRh75Lg4aUvn1A5I7Srp4MKV1I2DemZlPOqiZRhJTnKCLi0Xqw9bHXKyPzo5WO422Y%2FTXh1WmU%2Fk9PUdyJP%2FhtPJPX9r2pStSYWXPh8O1UvLYXcOFG31Bq9hihfA9BiEcbWXY2ppy0ZG6nJtuwm4YuWii8IyCZojqsX4AdyMSRjB%2BmyMkLqZZjFy3qdFesW4Q1KzOL6jq%2FNeKmE0IsoeWpBbm8Zko9rM%2Fi2f5bVbbuIcsDQHE%3D--kfZJFYqVK2FwSPGb--t8HL1zw6syAK38SrsSKd6Q%3D%3D",
    "Referer": "https://github.com/session",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


def post_github():
    url = "https://github.com/session"
    data = {
        "commit": "Sign in",
        "authenticity_token": "jUk6JmMTBBj6eaumJlDBPmACzQe / nNfq + 3pzv / xsgVdYmAh36NfQ5jtxZekt0p + 4Jd07Le0zu0YMcxng9zVdaA ==",

        "login": "814466057 @ qq.com",
        "password": "1224057950nb++",
        "webauthn - support": "supported",
        "webauthn - iuvpaa - support": "unsupported",
        "timestamp": '{}'.format(time.time()),
        "timestamp_secret": "ad688c7b7503281678a03a432d856b21ef58df76dd5585900a63cd677abbda31"
    }
    html = requests.post(url, headers=headers,data=data)
    if html.status_code == 200:
        print(html.text)
