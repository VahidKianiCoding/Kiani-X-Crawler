import json

headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.5',
  'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
  'content-type': 'application/json',
  'priority': 'u=1, i',
  'referer': 'https://x.com/search?q=(%22Palestine%22)%20(from%3ALauraLoomer)%20until%3A2025-10-27%20since%3A2025-10-10&src=typed_query',
  'sec-ch-ua': '"Brave";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
  'x-client-transaction-id': 'yLBI/13M0pVttjZKPoIVBCNxrhlwVb22wcRx17mDgs031UZn5adJCTPMIPHvsogjRNQRZ8wPGsHmoLSFhHinnwv+p3Dbyw',
  'x-csrf-token': '5ffb38d9dd21ede5c28332ed8c4f2d7e5e9458c20870815daebd2e04ee8f2475d083e8ab0bf7efaf286a6d626222e7d74120ad57329d95449874042b4ad72e909287fc863763a98dd1fed826b1775a9f',
  'x-twitter-active-user': 'yes',
  'x-twitter-auth-type': 'OAuth2Session',
  'x-twitter-client-language': 'en',
  'x-xp-forwarded-for': '867313f1de232f109745a9bfe48a82921a83ee14cd21585b7f4832fab77978ff691800287186236629e30a9932bcb19c3a5458ae4f6204232e69a1c7ada868721a5f716bb18ced5aed8aecbb86db4333d56eb49b72f419cbf5d2244882a82c841b282a21f5dd0993c456e0511cb3bd4cb0f46850d31ecda3f964d10dcced1760463f4c419e509f67a40f6f9af7268472469352d75e41ed551bb5c4047d30802cf5410f11c090694fa66f72763d2205ee67d8b3fdb96d9ccccaecddf02cfa8225915e738b95328e1763f7ef4b280a0f72b5506d5470bb21a0da2b596e70ce4100eba6e2f356dc4f59f8495598fe90a0e6508307cfb0ad1a32b5071a',
  'Cookie': 'd_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; __cuid=f4a31d4f32114b23bf07b8d76d88012a; kdt=q934k6Jv4o3OyKUpkUst5puuYNLmPxdnrvKRvD94; g_state={"i_l":0,"i_ll":1761552074589,"i_b":"IG0dpgXbZphDSwZ+7iOPnEBcYVqeWVv8dcdvTTjWgfM"}; dnt=1; auth_multi="814875951498665984:a2022f3a4471541402c729722079b9551af3b586"; auth_token=2646e14ee38bac62ed87f669a761f55a400660da; guest_id=v1%3A176155210269506988; twid=u%3D1591785998702333958; ct0=5ffb38d9dd21ede5c28332ed8c4f2d7e5e9458c20870815daebd2e04ee8f2475d083e8ab0bf7efaf286a6d626222e7d74120ad57329d95449874042b4ad72e909287fc863763a98dd1fed826b1775a9f; lang=en; __cf_bm=zzFn3jFr9ZoDg_u_mKTsdHyO9z.k2twxCTM98lBMLeU-1761557642.5801322-1.0.1.1-I3G72UgXvjfgXuOFmSspkBwtYYW.y0BUSLPQUzh1l8DZtgg3GEbINWdFyjvk79Wr44PA2ZE_t6q4z4oKcWQGG82xcUOC2j7M1NjNWHY8N9Voq5U86ex5FzPlLKIQRzkX'
}

headers_json = json.dumps(headers)

print(headers_json)

with open("headers.json", "w") as heardersJSON:
  json.dump(headers_json, heardersJSON)
