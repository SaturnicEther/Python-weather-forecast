import requests
url_template = 'https://wttr.in/{}?MnTm_qu&lang=ru'
article_ids = ['Лондон', 'Шереметьево', 'Череповец']
for article_id in article_ids:
    url = url_template.format(article_id)
    response=requests.get(url)
    print(response.text)