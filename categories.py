import os
import requests
import json


headers = {
    'authority': 'www.woolworths.com.au',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': f"ai_user=4CWNSN5eAtn2w3sBgspu94|2022-09-28T03:30:53.789Z; aam_uuid=89214788305736996913647638823987700738; mdLogger=false; kampyle_userid=cd08-4172-1acb-96b1-7cbb-3279-b326-78ae; _gcl_au=1.1.1976667653.1664335860; _fbp=fb.2.1664335859787.664084428; __gads=ID=912ed570ef14967f:T=1664335863:S=ALNI_MbgsTpdGfX5rHgnZJYn1g7YgOAgpg; DECLINED_DATE=1664338403978; BVBRANDID=9c0c274e-fbcb-4408-b1e2-e63833b5de94; rr_rcs=eF4FwbENgDAMBMAmFbu85A8vx96ANSKSSBR0wPzclfKeR08Fhwl-qkF9LbQaE0q3WSOTqe3-nmsYdxroLjWjh2dFBMAfhiARHQ; bm_sz=02E29559FC75563A60E0F9E96F81F2FF~YAAQROUcuDCcA1iDAQAAlsUDnhGYOI15a/AAuEeTiLD5S1+bjVVqeXeX28vMjzIVvHU0+CcQ8AK0scP7PfizcipR+VhrwBEiSQFiE5jaxJUfZY8qiGyWDg617Ka42aTHt/gL7hB76hPP0Yv2xx3Hu1xpGHpqopQohBHrx++bJv3NYIMEDl1Jt11IzPBk1Bv/6Flago5R28XINXsdj6L6be4CVNYx+rE6uuQLB4owJMPNS7IFWo+2jjbDeBls752epw+U/BI7UyDo4/dp2ctSBZfcJ2/5c6SB9P2prqiEoiiHoLqM6izBjpds~3555636~3223861; akaalb_woolworths.com.au=~op=www_woolworths_com_au_BFF_MEL:WOW-BFF-MEL|www_woolworths_com_au_ZoneB:PROD-ZoneB|www_woolworths_com_au_BFF_MEL_Launch:WOW-BFF-MEL|~rv=20~m=PROD-ZoneB:0|WOW-BFF-MEL:0|~os=43eb3391333cc20efbd7f812851447e6~id=a1e1f208b4b235108eb0c693aee97536; at_check=true; INGRESSCOOKIE=1664803394.02.45.103965|5eeab2ea8cdefed6dbef0b52cd0ff0b3; ak_bmsc=CBFC464D86FE6F8021C0240B92DB5E76~000000000000000000000000000000~YAAQROUcuEycA1iDAQAASNADnhGgnpNbCAIM6Qkwqh0c4RTKd+znmYZNVWCweH+NkZ1+kUGnKnQk59Gcwoz1m/t1UaWag/0MwvaQrqtQWn+o8l16K/fQOzQpqKIaAfpGTrzzj/zcT3hF1d3wI0SZHinFxCL40SbovWhRTMNKGXNnpQZf2GQCJMbUIOdV5tR1vsGv6UwelwCnLO0XmrKqTjnhAW+WLB96WG0Fne0pXoa3dw9BM2s6ZUtZKLPQzWA7+QWH16fXzGC3gLTxpWCgSrPzA8g7No+tN9XVveSnI/8Bya+74q2gGxWA5YQOFvCk/nUL3KHoJPweosO/fbnSqzdEHc9G6Wz/wcf//aFKXcm7Ek1GwuAByMO39kS3YsKl6LCAR7M416oNQ6WZRfV13IBhPSpPzEoeRqe3iwVrZjraFm4bMbRn7lgg5RTS9sB4LAlPVFlQs5rHYmprvClgJdhkvnEAJyskv4unGrCljIfMBQ4s2NMG5NBE8czuaiqqbS/CrQ==; adobe_grs=other; AMCVS_4353388057AC8D357F000101%40AdobeOrg=1; AMCV_4353388057AC8D357F000101%40AdobeOrg=870038026%7CMCIDTS%7C19268%7CMCMID%7C88923653315150755113618772811742629342%7CMCAAMLH-1665408197%7C3%7CMCAAMB-1665408197%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1664810597s%7CNONE%7CvVersion%7C5.0.0; s_cc=true; _gid=GA1.3.1573501743.1664803398; IR_gbd=woolworths.com.au; __gpi=UID=000009e994511cd1:T=1664335863:RT=1664803402:S=ALNI_MZMoLAkI8-7DM7sV-YFTPEkODUWPQ; kampylePageLoadedTimestamp=1664805732451; _uetsid=8ac295b0431e11edac54d7bf7ba0696f; _uetvid=f834ba303edd11ed9fd5358ebe118add; IR_7464=1664806416251%7C0%7C1664806416251%7C%7C; kampyleUserSession=1664806416331; kampyleUserSessionsCount=33; kampyleUserPercentile=81.16424189543716; _ga=GA1.1.100643268.1664335860; kampyleSessionPageCounter=5; utag_main=v_id:01838225bc140055c43645e4f8c005075005206d0093c{_sn:17$_se:307$_ss:0$_st:1664808603044$vapi_domain:woolworths.com.au$dc_visit:17$ses_id:1664803396826%3Bexp-session$_pn:5%3Bexp-session$dc_event:174%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session;} mbox=PC#42c8ae0d155b4080b0be0613691e5a05.37_0#1728051604|session#d6405d5d75144fd1be80e5b78631fec3#1664808667; w-rctx=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjQ4MDgyMTUsImV4cCI6MTY2NDgxMTgxNSwiaWF0IjoxNjY0ODA4MjE1LCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6ImMzNWM4ZGQxLTQ5ZTAtNGJjZi05NjFjLTgzOTllNmI2OWQ2MyIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.U_MnlF0zeY2oKUpwjAPu1ciqGIunadHfeZj7i0zKOADMQ1xsbmqQeJ9wzPnugOBFldwgt1t3cXegP9_ZuQlWOt76obrc_LG7rgbEferDWDg-HEkLkPU_kZsquUSrBDsKl_V6gUDOok1Xq0Z6hNTqdWuYhfRrCaJ27hQCW8d3C4Mhis-6TwX14obQSl1gaQCUiZi_aaZZXrTczfx_G2O-mkHXU00aOC1ao2ErsQHfkrMQhE3jmKeJKxzikSumvSyHv6ZC-LpDCgz8rCOduWHn0q7xb9d_KeWTunGCS66GvOpNju1SaJkPG5nIm02uBXNmVX5ANJhKk4Bfi1XkQskgMg; wow-auth-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjQ4MDgyMTUsImV4cCI6MTY2NDgxMTgxNSwiaWF0IjoxNjY0ODA4MjE1LCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6ImMzNWM4ZGQxLTQ5ZTAtNGJjZi05NjFjLTgzOTllNmI2OWQ2MyIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.U_MnlF0zeY2oKUpwjAPu1ciqGIunadHfeZj7i0zKOADMQ1xsbmqQeJ9wzPnugOBFldwgt1t3cXegP9_ZuQlWOt76obrc_LG7rgbEferDWDg-HEkLkPU_kZsquUSrBDsKl_V6gUDOok1Xq0Z6hNTqdWuYhfRrCaJ27hQCW8d3C4Mhis-6TwX14obQSl1gaQCUiZi_aaZZXrTczfx_G2O-mkHXU00aOC1ao2ErsQHfkrMQhE3jmKeJKxzikSumvSyHv6ZC-LpDCgz8rCOduWHn0q7xb9d_KeWTunGCS66GvOpNju1SaJkPG5nIm02uBXNmVX5ANJhKk4Bfi1XkQskgMg; prodwow-auth-token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2NjQ4MDgyMTUsImV4cCI6MTY2NDgxMTgxNSwiaWF0IjoxNjY0ODA4MjE1LCJpc3MiOiJXb29sd29ydGhzIiwiYXVkIjoid3d3Lndvb2x3b3J0aHMuY29tLmF1Iiwic2lkIjoiMCIsInVpZCI6ImMzNWM4ZGQxLTQ5ZTAtNGJjZi05NjFjLTgzOTllNmI2OWQ2MyIsIm1haWQiOiIwIiwiYXV0IjoiU2hvcHBlciIsImF1YiI6IjAiLCJhdWJhIjoiMCIsIm1mYSI6IjEifQ.U_MnlF0zeY2oKUpwjAPu1ciqGIunadHfeZj7i0zKOADMQ1xsbmqQeJ9wzPnugOBFldwgt1t3cXegP9_ZuQlWOt76obrc_LG7rgbEferDWDg-HEkLkPU_kZsquUSrBDsKl_V6gUDOok1Xq0Z6hNTqdWuYhfRrCaJ27hQCW8d3C4Mhis-6TwX14obQSl1gaQCUiZi_aaZZXrTczfx_G2O-mkHXU00aOC1ao2ErsQHfkrMQhE3jmKeJKxzikSumvSyHv6ZC-LpDCgz8rCOduWHn0q7xb9d_KeWTunGCS66GvOpNju1SaJkPG5nIm02uBXNmVX5ANJhKk4Bfi1XkQskgMg; ai_session=E+0reIUvwJmIWD5+zBnkoI|1664803393297|1664808415642; _abck=9DE5490F973C8E42EA7B340D2663B297~0~YAAQHabWfdYH6p2DAQAApf5QngjI+8/E0zD8h8Cq90aX+JULowXEAjmIHaxbluirJmmrl9lPxubXhx3S1gAQYz8dYrE37N8RcRn+6msqY5WajImD00/EJr67euGO/5EoKoihYzaI8cI3V9Nyeztg0DoE4GOFpvpVHEgx+iuaY6gqWIzF/gTe1kaPIubhMbb7AKQWebj7t43gJPQgv+jfoUCnrDn8A86556ELfsucP494Cccyk2978R7HmuRYqMg0KVS9rEkU2XsOkd7tLTjIV19AGLx5PoHfIot2NseAo4CwkDD5C3nZz+FlEeW0ecU3RyNp+g67vqy2DLtrdkFyB4b8eqVZ09+3z5N6SbYf92gS1L8jgCX400F293Tt6yLvO4yTxf+jV2aHNYsSmd7wC4saCGKxFlCuZ9jtZQ==~-1~||-1||~-1; AKA_A2=A; bm_sv=9F0F08391B4150A78DA0854409A8FEF7~YAAQHabWfZ4I6p2DAQAAyTlRnhEzQsQ8VgqueuzFj/vLt9ive5rax42THQ4uMqYY9pt4yWKQi6SXFAeaOAoy6FVQhfaVq4YLT4si/AVlAnA0pkJMdXTHwnE6FywiNH35T8OnzgPp3+QyPs7GiQfneKgZugvmwK3UIi14E8aWDO1znGCmbDvXnduoW9b+0+0ajSQK6Xa3UK7NPG4Kh67P0ahicXPBlYwPdvzbyGcxLw6HGTtvgJ7YzETCRPZAKeZuphOsS9Vmw5Cf~1; RT=\"z=1&dm=www.woolworths.com.au&si=fd5642a8-9190-4d0a-ba9a-186653210693&ss=l8sur4ye&sl=0&tt=0&rl=1&ul=1805j&hd=181fl\"; _ga_YBVRJYN9JL=GS1.1.1664803399.19.1.1664808466.60.0.0",
    'referer': 'https://www.woolworths.com.au/shop/browse/pet',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

response = requests.get('https://www.woolworths.com.au/apis/ui/PiesCategoriesWithSpecials',headers=headers)

with open('categories.txt', "w") as file:
    file.write(response.text)
    


        
        