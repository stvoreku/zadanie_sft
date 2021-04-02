from django.views import View
from django.http import JsonResponse
import json
from hashlib import sha256

class PersonView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            data_list = data['data_list']
            for d in data_list:
                d['hash'] = sha256(d['first_name'].encode('utf-8') + d['second_name'].encode('utf-8') + d['birth_date'].encode('utf-8')).hexdigest()
            result = sorted(data_list, key=lambda k: k['second_name'] + k['first_name'])
        except KeyError:
            return JsonResponse({'error':'bad form'}, status=400)
        return JsonResponse({'result':result}, status=200)



# Create your views here.
