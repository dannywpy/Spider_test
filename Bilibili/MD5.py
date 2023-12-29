import hashlib
from datetime import time
from urllib.parse import quote
def hash(data, date):
    date = (time.time() * 1000)

    data = {
        'oid': '23836532',
        'type': '1',
        'mode': '2',
        'pagination_str': '{"offset":"{\\"type\\":3,\\"direction\\":1,\\"Data\\":{\\"cursor\\":%s}}"}' % data,
        'plat': '1',
        'web_location': '1315875',
        'w_rid': w_rid,
        'wts': date,
    }


    print(quote(data))
    # %7B%22offset%22:%22%7B%5C%22type%5C%22:3,%5C%22direction%5C%22:1,%5C%22Data%5C%22:%7B%5C%22cursor%5C%22:7024%7D%7D%22%7D
    # %7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A3%2C%5C%22direction%5C%22%3A1%2C%5C%22Data%5C%22%3A%7B%5C%22cursor%5C%22%3A7024%7D%7D%22%7D
    Zt = [
        "mode=2",
        "oid=23836532",
        f"pagination_str={quote(data)}",
        "plat=1",
        "type=1",
        "web_location=1315875",
        f"wts={date}"  # 时间戳
    ]
    ct = "ea1db124af3c7062474693fa704f4ff8"
    Ut = '&'.join(Zt)
    string = Ut + ct
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    w_rid = MD5.hexdigest()
    print(w_rid)
    return w_rid


hash()