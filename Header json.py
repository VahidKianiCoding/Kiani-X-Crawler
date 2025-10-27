import json

headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.5',
  'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
  'content-type': 'application/json',
  'priority': 'u=1, i',
  'referer': 'https://x.com/search?q=(from%3ALauraLoomer)%20until%3A2025-10-27%20since%3A2025-10-01&src=typed_query',
  'sec-ch-ua': '"Brave";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
  'x-client-transaction-id': 'EWmRJoQVC0y0b++T51vM3fqod8CpjGRvGB2oDmBaWxTuDJ++PH6Q0OoV+Sg2a1H6nZv9vhVm1SJ/nxOLOXYfzu2O3vm6Eg',
  'x-csrf-token': '5ffb38d9dd21ede5c28332ed8c4f2d7e5e9458c20870815daebd2e04ee8f2475d083e8ab0bf7efaf286a6d626222e7d74120ad57329d95449874042b4ad72e909287fc863763a98dd1fed826b1775a9f',
  'x-twitter-active-user': 'yes',
  'x-twitter-auth-type': 'OAuth2Session',
  'x-twitter-client-language': 'en',
  'x-xp-forwarded-for': 'c04e170eb98f573f8cb06ec78978476c8001d75089dd6ed18d918812fef185b2a7d27f63a6cb1107f94573fc55ae2024da30adbbc5454a33d1c10996ec12a5c9b68115413483d238d42db5db7ae1036280276222f2ba6e4c25c5ec1871d23bbe1e00b1d1e2b59b776c276354cf9d75e16bb43274cec91d375a8fe84543100fc9dfda1bdff1d0f073b483cec328a7299b3604b03a34a841460be31622829bc2639e178ed675586949b2e9e69ce0143a725a96c6f19e44ddf48a0a0270382a34e66e17d28792504ce9d85af6424833f638b797525602721b8534869dd47a2667fa69a2ee5ddc08c15ebc35021ade4ccb3c24e56f6ded7f01c55c6e',
  'Cookie': 'd_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; __cuid=f4a31d4f32114b23bf07b8d76d88012a; kdt=q934k6Jv4o3OyKUpkUst5puuYNLmPxdnrvKRvD94; g_state={"i_l":0,"i_ll":1761552074589,"i_b":"IG0dpgXbZphDSwZ+7iOPnEBcYVqeWVv8dcdvTTjWgfM"}; dnt=1; auth_multi="814875951498665984:a2022f3a4471541402c729722079b9551af3b586"; auth_token=2646e14ee38bac62ed87f669a761f55a400660da; guest_id=v1%3A176155210269506988; twid=u%3D1591785998702333958; ct0=5ffb38d9dd21ede5c28332ed8c4f2d7e5e9458c20870815daebd2e04ee8f2475d083e8ab0bf7efaf286a6d626222e7d74120ad57329d95449874042b4ad72e909287fc863763a98dd1fed826b1775a9f; lang=en; __cf_bm=YJdxfcp9MZ.TFie1S548UrNmkbwK9iiW_rj1UA9r5x0-1761562617.5261493-1.0.1.1-wv6JcmY8lqBDFJyT5gzXGgR5HOVG0L3dq9D4oSd28xkxObyDnbwzH9R60EJijRSHyrrBbK0wH13cTGf_rbVr.ToijYXps8sBUn9t7RcQ2GWhlGBI1jtPo2szqiind20V; __cf_bm=cmLwNXIMQdcDHdOT5hl5hRaAm7_1m56BFU.1RSrm2wo-1761562673.624953-1.0.1.1-RyfCXFLGZKy25iVMIGSNxpl8Q8caitzFjlNl_0EAC1p5BemopPOKk7J45ir_afOFfKqzz5A2.S9qOHflGJBtk3AIKlH1EP06URri30FQTl3XByuvKDLW84NEdcKE4zYo'
}

header_json = json.dumps(headers)

print(header_json)

with open("header.json", "w") as headersJSON:
  json.dump(header_json, headersJSON)
