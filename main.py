import json
import time
import urllib.parse
import requests
from typing import Dict, Any, List, Optional

fingerprint_data = {
    "log2": "gl,tzp",
    "r3n": 33,
    "glvd": "Google Inc. (NVIDIA)",
    "glrd": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4050 Laptop GPU (0x000028E1) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    "nddc": 1,
    "exp8": 0,
    "dp0": False,
    "ucdv": False,
    "wdifrm": False,
    "npmtm": False,
    "wdif": False,
    "wdifpnh": "2935780137",
    "lg": "en-US",
    "isb": False,
    "idp": True,
    "crt": 0,
    "vnd": "Google Inc.",
    "bid": "NA",
    "med": "defined",
    "pltod": False,
    "csssp": "",
    "awe": False,
    "phe": False,
    "dat": False,
    "nm": False,
    "geb": False,
    "sqt": False,
    "pf": "Win32",
    "hc": 20,
    "br_oh": 912,
    "br_ow": 1536,
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "wbd": False,
    "ts_mtp": 0,
    "mob": False,
    "lgs": "[\"en-US\",\"en\",\"vi\"]",
    "dvm": 8,
    "hcovdr": False,
    "plovdr": False,
    "ftsovdr": False,
    "orf": "",
    "trrd": 0.90974067612581,
    "br_w": 414,
    "br_h": 834,
    "br_iw": 414,
    "br_ih": 834,
    "ars_w": 1536,
    "ars_h": 912,
    "rs_w": 1536,
    "rs_h": 960,
    "rs_cd": 24,
    "pr": 1.25,
    "so": "landscape-primary",
    "vco": "",
    "vcots": False,
    "vch": "probably",
    "vchts": True,
    "vcw": "probably",
    "vcwts": True,
    "vc3": "maybe",
    "vc3ts": False,
    "vcmp": "",
    "vcmpts": False,
    "vcq": "",
    "vcqts": False,
    "vc1": "probably",
    "vc1ts": True,
    "cssS": "11.98,11.10,8.38,3.47,5.46,5.52,12.81,14.75,3.69",
    "css0": "31, 23, 55",
    "css1": "3.40436, 0.448448, -0.50016, 0.0390445, -0.633075, -1.16183, -5.35075, 0.417701, -0.85683, 5.28962, -1.08932, 0.0850367, -10.976, 67.7601, -13.9542, 2.08932",
    "cssH": "0px",
    "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
    "plgod": False,
    "plg": 5,
    "plgne": True,
    "plgre": True,
    "plgof": False,
    "plggt": False,
    "mmt": "application/pdf,text/pdf",
    "bchk": "3223aeb6721e0d0917e7928181193ac88dcd62fad5cadfbe7a2b2b473ecf58ee70f018dbdb1a1832e8dc6528387b0745971dbcd82384261e9a4e3f",
    "nt_tcp": 76.3000000002794,
    "nt_dns": 23.100000000093132,
    "nt_rd": 0,
    "nt_irt": -101.20000000018626,
    "nt_rt": 35.1999999997206,
    "nt_tls": 40.40000000037253,
    "nt_ttf": 135.79999999981374,
    "nt_swt": 1.1000000000931323,
    "nt_csd": 507,
    "nt_nhp": "http/1.1",
    "nt_rdc": 0,
    "nt_it": "navigation",
    "nt_prs": 0,
    "nt_esc": 35.89999999990687,
    "nt_ttrd": -0.11138613862436056,
    "nt_le": 0,
    "nt_dcle": 0,
    "nt_di": 34484.299999999814,
    "nt_dc": 0,
    "ccsT": "Error\nat S (https://dd.garena.com/tags.js:2:25622)\nat Un.C (https://dd.garena.com/tags.js:2:61131)\nat https://dd.garena.com/tags.js:2:24018\nat https:/",
    "ccsB": "com/tags.js:2:25622)\nat Un.C (https://dd.garena.com/tags.js:2:61131)\nat https://dd.garena.com/tags.js:2:24018\nat https://dd.garena.com/tags.js:2:72042",
    "ccsH": 1404483668,
    "muev": False,
    "pro_t": True,
    "wglo": True,
    "prso": True,
    "wbst": True,
    "psn": True,
    "edp": True,
    "addt": True,
    "wsdc": True,
    "ccsr": True,
    "nuad": True,
    "bcda": False,
    "idn": True,
    "capi": False,
    "svde": False,
    "vpbq": True,
    "m_fmi": False,
    "mq": "aptr:fine, ahvr:hover",
    "aco": "probably",
    "acots": False,
    "acmp": "probably",
    "acmpts": True,
    "acw": "probably",
    "acwts": False,
    "acma": "maybe",
    "acmats": False,
    "acaa": "probably",
    "acaats": True,
    "ac3": "maybe",
    "ac3ts": False,
    "acf": "probably",
    "acfts": False,
    "acmp4": "maybe",
    "acmp4ts": False,
    "acmp3": "probably",
    "acmp3ts": False,
    "acwm": "maybe",
    "acwmts": False,
    "ocpt": False,
    "ckwa": True,
    "spwn": False,
    "emt": False,
    "bfr": False,
    "tz": 420,
    "hdn": False,
    "xt1": True,
    "cdhf": True,
    "eva": 40,
    "cokys": ",loadTimes,csi,app",
    "ecpc": False,
    "nhi": "x86,64,false,,Windows,15.0.0,138.0.3351.121,false",
    "k_lyts": 48,
    "k_lytk": "kg20va`l\\'w8mh.71pdfoqcn[zy365x/\\,-4bt9siu=j;r]e",
    "wwl": False,
    "tzp": "America/Los_Angeles",
    "es_sigmdn": None,
    "es_mumdn": None,
    "es_distmdn": None,
    "es_angsmdn": None,
    "es_angemdn": None,
    "k_hA": None,
    "k_hSD": None,
    "k_pA": None,
    "k_pSD": None,
    "k_rA": None,
    "k_rSD": None,
    "k_ikA": None,
    "k_ikSD": None,
    "k_kdc": 0,
    "k_kuc": 0,
    "m_s_c": 0,
    "m_m_c": 1,
    "m_c_c": 0,
    "m_cm_r": 0,
    "m_ms_r": -1,
    "uish": "3391171800",
    "jset": 1754238299,
    "bpc": 2,
    "isf": False,
    "isf2": False,
    "dt": True,
    "fph": 470008069,
    "dcok": ".garena.com",
    "emd": "k:ai,vi,ao",
    "bci": False,
    "bcl": 0.31,
    "bct": None,
    "bdt": 3044
}

ddjskey = "AE3F04AD3F0D3A462481A337485081"
datadome_cookie_for_payload = "nNGehF9mPYh~olywk47_5K9lhBzZbDJS2S2rF~NdPhYMAGRFMHcb125vYsuTSkS2ViuIyxuJwMpV5iih6NSJEBs_Jb7ff5qZGzlYIJ0KRmsnsIuLWoFLixviuLFz~JKQ"
jsType = "ch"
eventCounters = []
refererUrl = "https://account.garena.com/"
requestPath = "/"
responsePage = "origin"
dd_version = "5.1.5"
dd_timestamp = int(time.time() * 1000)

class DataDomeGenerator:
    def __init__(self, key: str, cookie: str):
        self.key = key
        self.cookie = cookie
        self.t = 9959949970
        self.n = 1789537805

    def _hash_str_to_int(self, s: str) -> int:
        if not s:
            return self.n
        o = 0
        for char in s:
            o = ((o << 5) - o + ord(char)) & 0xFFFFFFFF
        return o

    def _prng_h(self, n: int) -> int:
        n ^= n << 13
        n ^= (n >> 17) & 0xFFFFFFFF
        n ^= n << 5
        return n & 0xFFFFFFFF

    def _create_keystream_generator(self, seed1: int, seed2: int):
        e = seed1
        i = -1
        r = seed2
        a = True
        u = None

        def generator(get_val: bool = False) -> int:
            nonlocal e, i, r, a, u
            if u is not None:
                t = u
                u = None
                return t
            i += 1
            if i > 2:
                e = self._prng_h(e)
                i = 0
            t = (e >> (16 - 8 * i)) & 0xFF
            if a:
                r -= 1
                t ^= (r & 0xFF)
            if get_val:
                u = t
            return t
        a = False
        return generator

    def _custom_b64_encode_char(self, n: int) -> int:
        if 37 < n:
            return 59 + n
        if 11 < n:
            return 53 + n
        if 1 < n:
            return 46 + n
        return 50 * n + 45

    def generate_payload(self, data: Dict[str, Any]) -> str:
        seed_from_cookie = self._hash_str_to_int(self.cookie)
        initial_seed = self.t ^ seed_from_cookie ^ self._hash_str_to_int(self.key)
        e = self._prng_h(self._prng_h(((dd_timestamp >> 3) ^ 11027890091) * self.t))
        keystream_gen_a = self._create_keystream_generator(initial_seed, e)
        payload_bytes = []
        is_first = True
        def stringify(val: Any) -> str:
            return json.dumps(val)
        def encrypt_str(s: str) -> List[int]:
            buffer = s.encode('utf-8')
            encrypted = []
            for byte in buffer:
                encrypted.append(byte ^ keystream_gen_a())
            return encrypted
        for key, value in data.items():
            if not is_first:
                payload_bytes.append(keystream_gen_a() ^ 44)
            key_bytes = encrypt_str(stringify(key))
            value_bytes = encrypt_str(stringify(value))
            payload_bytes.extend(key_bytes)
            payload_bytes.append(keystream_gen_a() ^ 58)
            payload_bytes.extend(value_bytes)
            is_first = False
        keystream_gen_b = self._create_keystream_generator(1809053797 ^ self._hash_str_to_int(self.cookie), e)
        final_bytes = [byte ^ keystream_gen_b() for byte in payload_bytes]
        final_bytes.append((keystream_gen_a(True) ^ 125) ^ keystream_gen_b())
        result_chars = []
        w = 0
        b = e
        while w < len(final_bytes):
            b = (b - 1) & 0xFFFFFFFF
            byte1 = (b & 0xFF) ^ final_bytes[w]
            w += 1
            b = (b - 1) & 0xFFFFFFFF
            byte2 = (b & 0xFF) ^ final_bytes[w] if w < len(final_bytes) else 0
            w += 1
            b = (b - 1) & 0xFFFFFFFF
            byte3 = (b & 0xFF) ^ final_bytes[w] if w < len(final_bytes) else 0
            w += 1
            z = (byte1 << 16) | (byte2 << 8) | byte3
            result_chars.append(chr(self._custom_b64_encode_char((z >> 18) & 63)))
            result_chars.append(chr(self._custom_b64_encode_char((z >> 12) & 63)))
            result_chars.append(chr(self._custom_b64_encode_char((z >> 6) & 63)))
            result_chars.append(chr(self._custom_b64_encode_char(z & 63)))
        padding = len(final_bytes) % 3
        if padding > 0:
            return ''.join(result_chars[:-(3 - padding)])
        return ''.join(result_chars)

async def main():
    generator = DataDomeGenerator(ddjskey, datadome_cookie_for_payload)
    jspl_payload = generator.generate_payload(fingerprint_data)
    params = {
        'jspl': jspl_payload,
        'eventCounters': json.dumps(eventCounters),
        'jsType': jsType,
        'cid': datadome_cookie_for_payload,
        'ddk': ddjskey,
        'Referer': refererUrl,
        'request': requestPath,
        'responsePage': responsePage,
        'ddv': dd_version
    }
    body = urllib.parse.urlencode(params)
    try:
        headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,vi;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": refererUrl,
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        response = requests.post(
            "https://dd.garena.com/js/",
            headers=headers,
            data=body
        )
        response_data = response.json()
        if 'cookie' in response_data:
            print("✅ Success:", response_data)
        else:
            print("Không nhận được cookie. Hãy kiểm tra lại dữ liệu fingerprint hoặc payload.")
    except Exception as error:
        print(f"Đã xảy ra lỗi khi gửi yêu cầu: {error}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 