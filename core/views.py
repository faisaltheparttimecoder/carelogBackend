import requests, json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


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
    return JsonResponse(generate_access_token(response.json()))


@csrf_exempt
def generate_access_token(responseJson):
    """
    Generate the token of the authorized user
    """
    access_token = responseJson['access_token']
    data = {
        'grant_type': 'convert_token',
        'client_id': os.environ['SOCIAL_AUTH_KEY'],
        'client_secret': os.environ['SOCIAL_AUTH_SECRET'],
        'backend': os.environ['SOCIAL_AUTH_BACKEND'],
        'token': access_token
    }
    response = requests.post(os.environ['BASE_URL'] + 'auth/convert-token', data=data)
    return response.json()


class loggedUser(APIView):
    """
    Get the logged in users full name
    """
    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        return Response(request.user.get_full_name())
