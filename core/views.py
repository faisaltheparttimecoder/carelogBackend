import requests, json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User


@csrf_exempt
def Login(request):
    """
    User Login method
    """
    body = request.body.decode('utf-8')
    body_data = json.loads(body)
    data = {
        'code': body_data['code'],
        'client_id': os.environ['GOOGLE_CLIENT_ID'],
        'redirect_uri': body_data['redirectUri'],
        'client_secret': os.environ['GOOGLE_CLIENT_SECRET'],
        'grant_type': 'authorization_code',
        'scope': [
            'profile'
        ]
    }
    response = requests.post('https://accounts.google.com/o/oauth2/token',
                  data=data, headers={
            'content-type': 'application/x-www-form-urlencoded'
        })
    return JsonResponse(response.json())
