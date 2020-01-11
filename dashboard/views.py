from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

import json
from .tasks import data_forms_load, score_load, dropdown_metabase_load
import jwt
import time


@login_required
def dashboard_frame(request, dashname=None):

    METABASE_SITE_URL = "https://femama-dash.herokuapp.com"
    METABASE_SECRET_KEY = "bd2bbe68ba300861be298086ca2b200686cc5f4c73fc078befa9c7f8c9dd660b"
    payload = {"resource": {"dashboard": 4}, "params": {}, "exp": round(time.time()) + (60 * 10)}

    if dashname:
        if dashname == 'comunicação':
            payload["resource"] = {"dashboard": 4}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        if dashname == 'pacientes_atendidos':
            payload["resource"] = {"dashboard": 3}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        if dashname == 'radar':
            payload["resource"] = {"dashboard": 5}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        if dashname == 'radar_cidades':
            payload["resource"] = {"dashboard": 7}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        if dashname == 'encontre_no_censo':
            payload["resource"] = {"dashboard": 6}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        if dashname == 'perfil_das_ongs':
            payload["resource"] = {"dashboard": 9}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

        else:
            payload["resource"] = {"dashboard": 4}
            token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
            iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
            return render(request, 'index.html', {'iframeUrl': iframeUrl})

    else:
        payload["resource"] = {"dashboard": 4}
        token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
        iframeUrl = METABASE_SITE_URL + "/public/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
        return render(request, 'index.html', {'iframeUrl': iframeUrl})


@csrf_exempt
def mapa_br(request):
    with open('dashboard/static/json/uf.json', encoding='latin-1') as json_file:
        json_data = json.load(json_file)

    return JsonResponse(json_data, safe=False)


@csrf_exempt
def update_dados_form(request):

    status = data_forms_load.delay()

    return HttpResponse(status)


@csrf_exempt
def update_dados_score(request):

    score_load.delay()

    return JsonResponse({'status': 'ok'}, safe=False)


@csrf_exempt
def update_dropdown_metabase(request):

    status = dropdown_metabase_load.delay()

    return HttpResponse(status)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect('/info/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('url_dashboard:accounts')

    else:
        logout(request)
        return redirect('url_dashboard:accounts')
