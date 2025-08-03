const { URLSearchParams } = require('url');

const fingerprint_data = {
    "log2": "gl,tzp",
    "r3n": 33,
    "glvd": "Google Inc. (NVIDIA)",
    "glrd": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4050 Laptop GPU (0x000028E1) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    "nddc": 1,
    "exp8": 0,
    "dp0": false,
    "ucdv": false,
    "wdifrm": false,
    "npmtm": false,
    "wdif": false,
    "wdifpnh": "2935780137",
    "lg": "en-US",
    "isb": false,
    "idp": true,
    "crt": 0,
    "vnd": "Google Inc.",
    "bid": "NA",
    "med": "defined",
    "pltod": false,
    "csssp": "",
    "awe": false,
    "phe": false,
    "dat": false,
    "nm": false,
    "geb": false,
    "sqt": false,
    "pf": "Win32",
    "hc": 20,
    "br_oh": 912,
    "br_ow": 1536,
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "wbd": false,
    "ts_mtp": 0,
    "mob": false,
    "lgs": "[\"en-US\",\"en\",\"vi\"]",
    "dvm": 8,
    "hcovdr": false,
    "plovdr": false,
    "ftsovdr": false,
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
    "vcots": false,
    "vch": "probably",
    "vchts": true,
    "vcw": "probably",
    "vcwts": true,
    "vc3": "maybe",
    "vc3ts": false,
    "vcmp": "",
    "vcmpts": false,
    "vcq": "",
    "vcqts": false,
    "vc1": "probably",
    "vc1ts": true,
    "cssS": "11.98,11.10,8.38,3.47,5.46,5.52,12.81,14.75,3.69",
    "css0": "31, 23, 55",
    "css1": "3.40436, 0.448448, -0.50016, 0.0390445, -0.633075, -1.16183, -5.35075, 0.417701, -0.85683, 5.28962, -1.08932, 0.0850367, -10.976, 67.7601, -13.9542, 2.08932",
    "cssH": "0px",
    "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
    "plgod": false,
    "plg": 5,
    "plgne": true,
    "plgre": true,
    "plgof": false,
    "plggt": false,
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
    "muev": false,
    "pro_t": true,
    "wglo": true,
    "prso": true,
    "wbst": true,
    "psn": true,
    "edp": true,
    "addt": true,
    "wsdc": true,
    "ccsr": true,
    "nuad": true,
    "bcda": false,
    "idn": true,
    "capi": false,
    "svde": false,
    "vpbq": true,
    "m_fmi": false,
    "mq": "aptr:fine, ahvr:hover",
    "aco": "probably",
    "acots": false,
    "acmp": "probably",
    "acmpts": true,
    "acw": "probably",
    "acwts": false,
    "acma": "maybe",
    "acmats": false,
    "acaa": "probably",
    "acaats": true,
    "ac3": "maybe",
    "ac3ts": false,
    "acf": "probably",
    "acfts": false,
    "acmp4": "maybe",
    "acmp4ts": false,
    "acmp3": "probably",
    "acmp3ts": false,
    "acwm": "maybe",
    "acwmts": false,
    "ocpt": false,
    "ckwa": true,
    "spwn": false,
    "emt": false,
    "bfr": false,
    "tz": 420,
    "hdn": false,
    "xt1": true,
    "cdhf": true,
    "eva": 40,
    "cokys": ",loadTimes,csi,app",
    "ecpc": false,
    "nhi": "x86,64,false,,Windows,15.0.0,138.0.3351.121,false",
    "k_lyts": 48,
    "k_lytk": "kg20va`l\\'w8mh.71pdfoqcn[zy365x/\\,-4bt9siu=j;r]e",
    "wwl": false,
    "tzp": "America/Los_Angeles",
    "es_sigmdn": null,
    "es_mumdn": null,
    "es_distmdn": null,
    "es_angsmdn": null,
    "es_angemdn": null,
    "k_hA": null,
    "k_hSD": null,
    "k_pA": null,
    "k_pSD": null,
    "k_rA": null,
    "k_rSD": null,
    "k_ikA": null,
    "k_ikSD": null,
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
    "isf": false,
    "isf2": false,
    "dt": true,
    "fph": 470008069,
    "dcok": ".garena.com",
    "emd": "k:ai,vi,ao",
    "bci": false,
    "bcl": 0.31,
    "bct": null,
    "bdt": 3044
};

const ddjskey = "AE3F04AD3F0D3A462481A337485081";
const datadome_cookie_for_payload = ".keep"; 
const jsType = "ch";
const eventCounters = [];
const refererUrl = "https://account.garena.com/";
const requestPath = "/";
const responsePage = "origin";
const dd_version = "5.1.5";
const dd_timestamp = Date.now();

class DataDomeGenerator {
    constructor(key, cookie) {
        this.key = key;
        this.cookie = cookie;
        this.t = 9959949970;
        this.n = 1789537805;
    }

    _hashStrToInt(s) {
        if (!s) {
            return this.n;
        }
        let o = 0;
        for (let i = 0; i < s.length; i++) {
            o = ((o << 5) - o + s.charCodeAt(i)) | 0;
        }
        return o;
    }

    _prngH(n) {
        n ^= n << 13;
        n ^= n >>> 17;
        n ^= n << 5;
        return n | 0;
    }

    _createKeystreamGenerator(seed1, seed2) {
        let e = seed1;
        let i = -1;
        let r = seed2;
        let a = true;
        let u = null;

        const generator = (get_val = false) => {
            if (u !== null) {
                const t = u;
                u = null;
                return t;
            }

            i++;
            if (i > 2) {
                e = this._prngH(e);
                i = 0;
            }

            let t = (e >> (16 - 8 * i)) & 0xFF;

            if (a) {
                r--;
                t ^= (r & 0xFF);
            }

            if (get_val) {
                u = t;
            }
            return t;
        };

        a = false;
        return generator;
    }

    _customB64EncodeChar(n) {
        if (37 < n) return 59 + n;
        if (11 < n) return 53 + n;
        if (1 < n) return 46 + n;
        return 50 * n + 45;
    }

    generatePayload(data) {
        const seed_from_cookie = this._hashStrToInt(this.cookie);
        const initial_seed = this.t ^ seed_from_cookie ^ this._hashStrToInt(this.key);
        const e = this._prngH(this._prngH(((dd_timestamp >> 3) ^ 11027890091) * this.t));
        const keystream_gen_a = this._createKeystreamGenerator(initial_seed, e);

        const payload_bytes = [];
        let is_first = true;

        const stringify = (val) => {
            return JSON.stringify(val);
        };

        const encrypt_str = (s) => {
            const buffer = Buffer.from(s, 'utf8');
            const encrypted = [];
            for (const byte of buffer) {
                encrypted.push(byte ^ keystream_gen_a());
            }
            return encrypted;
        };

        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                const value = data[key];

                if (!is_first) {
                    payload_bytes.push(keystream_gen_a() ^ 44);
                }

                const key_bytes = encrypt_str(stringify(key));
                const value_bytes = encrypt_str(stringify(value));

                payload_bytes.push(...key_bytes);
                payload_bytes.push(keystream_gen_a() ^ 58);
                payload_bytes.push(...value_bytes);

                is_first = false;
            }
        }

        const keystream_gen_b = this._createKeystreamGenerator(1809053797 ^ this._hashStrToInt(this.cookie), e);

        const final_bytes = payload_bytes.map(byte => byte ^ keystream_gen_b());

        final_bytes.push((keystream_gen_a(true) ^ 125) ^ keystream_gen_b());

        const result_chars = [];
        let w = 0;
        let b = e;

        while (w < final_bytes.length) {
            b = (b - 1) | 0;
            const byte1 = (b & 0xFF) ^ final_bytes[w];
            w++;

            b = (b - 1) | 0;
            const byte2 = w < final_bytes.length ? (b & 0xFF) ^ final_bytes[w] : 0;
            w++;

            b = (b - 1) | 0;
            const byte3 = w < final_bytes.length ? (b & 0xFF) ^ final_bytes[w] : 0;
            w++;
            
            const z = (byte1 << 16) | (byte2 << 8) | byte3;
            
            result_chars.push(String.fromCharCode(this._customB64EncodeChar((z >> 18) & 63)));
            result_chars.push(String.fromCharCode(this._customB64EncodeChar((z >> 12) & 63)));
            result_chars.push(String.fromCharCode(this._customB64EncodeChar((z >> 6) & 63)));
            result_chars.push(String.fromCharCode(this._customB64EncodeChar(z & 63)));
        }

        const padding = final_bytes.length % 3;
        if (padding > 0) {
            return result_chars.slice(0, -(3 - padding)).join('');
        }

        return result_chars.join('');
    }
}

async function main() {
    const generator = new DataDomeGenerator(ddjskey, datadome_cookie_for_payload);
    const jspl_payload = generator.generatePayload(fingerprint_data);

    const params = new URLSearchParams();
    params.append('jspl', jspl_payload);
    params.append('eventCounters', JSON.stringify(eventCounters));
    params.append('jsType', jsType);
    params.append('cid', datadome_cookie_for_payload);
    params.append('ddk', ddjskey);
    params.append('Referer', refererUrl);
    params.append('request', requestPath);
    params.append('responsePage', responsePage);
    params.append('ddv', dd_version);

    const body = params.toString();

    try {
        const response = await fetch("https://dd.garena.com/js/", {
            "headers": {
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
            },
            "body": body,
            "method": "POST"
        });

        const responseData = await response.json();

        if (responseData.cookie) {
            console.log("✅ Success:", responseData);
        } else {
            console.log("\n\n❌ THẤT BẠI! Không nhận được cookie. Hãy kiểm tra lại dữ liệu fingerprint hoặc payload.");
        }

    } catch (error) {
        console.error("\n\n❌ Đã xảy ra lỗi khi gửi yêu cầu:", error);
    }
}

main();