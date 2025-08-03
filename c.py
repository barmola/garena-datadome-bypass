import requests

url = "https://sso.garena.com/api/prelogin"

params = {
  'app_id': "10100",
  'account': "a",
  'format': "json",
  'id': "1754242831148"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  'Accept': "application/json, text/plain, /",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua-platform': "\"Windows\"",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
  'sec-ch-ua-mobile': "?0",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://sso.garena.com/universal/login?app_id=10100&redirect_uri=https%3A%2F%2Faccount.garena.com%2F&locale=vi-VN",
  'Accept-Language': "vi",
  'Cookie': "_ga=GA1.1.147002254.1754242821; _ga_1M7M9L6VPX=GS2.1.s1754242820$o1$g0$t1754242820$j60$l0$h0; datadome=tVAFa3pNBIUEOeZ2MmT5Sn7iYe8z48BRQhBhwATu7Xdbyp677wpMoh5iuJHFhcJqDoYX0TzMdOlpUQwcTQZ1hY1dYsqeZ1JdkdjrpRkOVvNiSifJd11rHCLe_tS36qNB"
}

response = requests.get(url, params=params, headers=headers)

print(response.text)