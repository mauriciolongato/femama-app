from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

import json
from .tasks import data_forms_load, score_load, dropdown_metabase_load
from .models import jobs


@csrf_exempt
def dashboard_frame(requests):
    # METABASE_SITE_URL = "http://134.209.10.236:3000"
    # METABASE_SECRET_KEY = "7331ac790842a4e87e3dbd7dac5ee69da446597ad105519ae78fa739567276ad"
    #
    # payload = {"resource": {"dashboard": 1}, "params": {}, "exp": round(time.time()) + (60 * 10)}
    # token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    #
    # iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=false&titled=true"

    question_html = '''<iframe src="https://femama-app.herokuapp.com/public/question/0ca1110c-cf90-4d79-b8b5-3a43d903bd13" frameborder="0"
                            width="800" height="600" allowtransparency ></iframe>'''
    return render(requests, 'index.html', {'iframeUrl': question_html})


@csrf_exempt
def mapa_br(requests):
    with open('dashboard/static/json/uf.json', encoding='latin-1') as json_file:
        json_data = json.load(json_file)

    return JsonResponse(json_data, safe=False)


@csrf_exempt
def update_dados_form(requests):

    status = data_forms_load.delay()

    return HttpResponse(status)


@csrf_exempt
def update_dados_score(requests):

    score_load.delay()

    return JsonResponse({'status': 'ok'}, safe=False)


@csrf_exempt
def update_dropdown_metabase(requests):

    status = dropdown_metabase_load.delay()

    return HttpResponse(status)