import requests
from lxml import html 
from rich import print

cookies = {
    'visid_incap_2800108': 'UWkm19AHQEyn8FkI0L2WkVayJ2oAAAAAQUIPAAAAAACSkDccbYfAUv1XJh7GXsNQ',
    'incap_ses_797_2800108': '0/ZVPGGqRUSsiHW4S4MPC1ayJ2oAAAAAjgf7RmiA45ctg1Aaf9bKdA==',
    'incap_ses_988_2800108': 'Vw2CQaEbJD+24U4RAxW2DViyJ2oAAAAAt9xhFBFHZB36bvtk3V3lxQ==',
    's_rnd': '99',
    'ld_user': 'ed910297-d5a9-4e7f-a3af-c5d93eafc686',
    'sessionId': '5f330d96-9710-4377-8a15-0cad19ceef84',
    'visitorId': 'febd39cc-2540-42b1-82ad-579e0af8e2c0',
    'AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg': '1',
    'nlbi_2800108_3037207': '6sDdenhWRWPMbJc9QME8pAAAAABTOKpg+MPtj4i0h9QWZWnW',
    'analyticsIsLoggedIn': 'false',
    'ldUserType': 'anonymous',
    'at_check': 'true',
    'ApplicationGatewayAffinityCORS': 'bfe5a4a2131860a0c8623216b3d7f486',
    'ApplicationGatewayAffinity': 'bfe5a4a2131860a0c8623216b3d7f486',
    'nlbi_2800108': 'pNk5FoXQSEqRgL/XQME8pAAAAABppyL+czwfKo8tgbPEhEYN',
    's_ecid': 'MCMID|55475477978608863228892936985040748335',
    'nlbi_2800108_2670698': 'ye1RNSGSkUvNVrfUQME8pAAAAABu6l3hdZvfhuMqiHqRLUV4',
    'OptanonAlertBoxClosed': '2026-06-09T07:02:46.619Z',
    'reese84': '3:gcbFZCSQOmDIwiGD8P9oaA==:NnKTpqjRlbwEXsewAEyWprxJRivrCsRJQ62atpI0H3YwsL927XzV5/c6tql/14TUE1X/QAR3u+4B++JVlJWf6zpCL4PqbWuD//llSafE1PRbsYVj0eK88q3yIIaEmlyNXZ13beDqp2vv5yhGwWF31Q==:mRhoJfUceB8KSew/Sj2QSGJk3wZHN8/i7RefOkDC2Ag=:XDr4Lsd21Z7IbTUSfPgrWa+q78mRQviTP5C7lp1GlQhA/7Jkck7tIOn+8rR8Ik+jjv4Gki1WSQCZDdhGTGGobD2LQ2VdXa3dAJQnzwytbhX9Kk3sqcXk1tGeITE9hW9eK8Oe6ZX9lvGTXEVnk2QbiAiyMX0Vy88JCgSW14sSX/HaM3/5HQcMaa7vRgmwAhtR5jap3R4xE94ohXdrko3ugYSptD4JRziWE2sBX/WOcesb5lPRVoAwM0c/iUjg1JLjp6FFUL8eqv/zQ69adtxXTigIrexJ00SdBacVu1vsHcFMWiuWYu65exSkldOJCvoAAhY9Kcooib9vkZGlAzf6Poln5ufC92IS/eMdVsR9qQ==:',
    'AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg': '179643557%7CMCIDTS%7C20614%7CMCMID%7C55475477978608863228892936985040748335%7CMCAID%7CNONE%7CMCOPTOUT-1780995779s%7CNONE%7CvVersion%7C5.5.0',
    'nlbi_2800108_2147483392': 'X/Inb96CkAw8Ny+gQME8pAAAAACPyGpre/FLeX6Bn0GOOEUY',
    'mbox': 'PC#dbcde2d089e7450a89efda99dfb600ab.41_0#1844233381|session#cc017e529cdf410482e1a3c985b13a34#1780990441',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Jun+09+2026+12%3A33%3A00+GMT%2B0530+(India+Standard+Time)&version=202603.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8ccb7b56-ab1a-4cc5-a441-f85faf10526c&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=BG4%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1&crTime=1780986794085&AwaitingReconsent=false&geolocation=IN%3BGJ',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'cookie': 'visid_incap_2800108=UWkm19AHQEyn8FkI0L2WkVayJ2oAAAAAQUIPAAAAAACSkDccbYfAUv1XJh7GXsNQ; incap_ses_797_2800108=0/ZVPGGqRUSsiHW4S4MPC1ayJ2oAAAAAjgf7RmiA45ctg1Aaf9bKdA==; incap_ses_988_2800108=Vw2CQaEbJD+24U4RAxW2DViyJ2oAAAAAt9xhFBFHZB36bvtk3V3lxQ==; s_rnd=99; ld_user=ed910297-d5a9-4e7f-a3af-c5d93eafc686; sessionId=5f330d96-9710-4377-8a15-0cad19ceef84; visitorId=febd39cc-2540-42b1-82ad-579e0af8e2c0; AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg=1; nlbi_2800108_3037207=6sDdenhWRWPMbJc9QME8pAAAAABTOKpg+MPtj4i0h9QWZWnW; analyticsIsLoggedIn=false; ldUserType=anonymous; at_check=true; ApplicationGatewayAffinityCORS=bfe5a4a2131860a0c8623216b3d7f486; ApplicationGatewayAffinity=bfe5a4a2131860a0c8623216b3d7f486; nlbi_2800108=pNk5FoXQSEqRgL/XQME8pAAAAABppyL+czwfKo8tgbPEhEYN; s_ecid=MCMID|55475477978608863228892936985040748335; nlbi_2800108_2670698=ye1RNSGSkUvNVrfUQME8pAAAAABu6l3hdZvfhuMqiHqRLUV4; OptanonAlertBoxClosed=2026-06-09T07:02:46.619Z; reese84=3:gcbFZCSQOmDIwiGD8P9oaA==:NnKTpqjRlbwEXsewAEyWprxJRivrCsRJQ62atpI0H3YwsL927XzV5/c6tql/14TUE1X/QAR3u+4B++JVlJWf6zpCL4PqbWuD//llSafE1PRbsYVj0eK88q3yIIaEmlyNXZ13beDqp2vv5yhGwWF31Q==:mRhoJfUceB8KSew/Sj2QSGJk3wZHN8/i7RefOkDC2Ag=:XDr4Lsd21Z7IbTUSfPgrWa+q78mRQviTP5C7lp1GlQhA/7Jkck7tIOn+8rR8Ik+jjv4Gki1WSQCZDdhGTGGobD2LQ2VdXa3dAJQnzwytbhX9Kk3sqcXk1tGeITE9hW9eK8Oe6ZX9lvGTXEVnk2QbiAiyMX0Vy88JCgSW14sSX/HaM3/5HQcMaa7vRgmwAhtR5jap3R4xE94ohXdrko3ugYSptD4JRziWE2sBX/WOcesb5lPRVoAwM0c/iUjg1JLjp6FFUL8eqv/zQ69adtxXTigIrexJ00SdBacVu1vsHcFMWiuWYu65exSkldOJCvoAAhY9Kcooib9vkZGlAzf6Poln5ufC92IS/eMdVsR9qQ==:; AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg=179643557%7CMCIDTS%7C20614%7CMCMID%7C55475477978608863228892936985040748335%7CMCAID%7CNONE%7CMCOPTOUT-1780995779s%7CNONE%7CvVersion%7C5.5.0; nlbi_2800108_2147483392=X/Inb96CkAw8Ny+gQME8pAAAAACPyGpre/FLeX6Bn0GOOEUY; mbox=PC#dbcde2d089e7450a89efda99dfb600ab.41_0#1844233381|session#cc017e529cdf410482e1a3c985b13a34#1780990441; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jun+09+2026+12%3A33%3A00+GMT%2B0530+(India+Standard+Time)&version=202603.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8ccb7b56-ab1a-4cc5-a441-f85faf10526c&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=BG4%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0001%3A1&crTime=1780986794085&AwaitingReconsent=false&geolocation=IN%3BGJ',
}

response = requests.get('https://www.coles.com.au/cusp-sitemap.xml', cookies=cookies, headers=headers)
html_content=html.fromstring(response.content)
urls=html_content.xpath("//*[local-name()='loc']/text()")
print((urls))











