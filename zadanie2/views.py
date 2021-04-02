from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
import json
import requests
from hashlib import sha256

class BitcoinView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            buy = float(data['buy'])
        except KeyError:
            return JsonResponse({'error':'bad form'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'float required'}, status=400)
        data = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')
        price_list = json.loads(data.text)['bids']
        price_list = sorted(price_list, key=lambda d: d[0])
        price = 0
        bought = 0
        for p in price_list:
            if p[1] >= buy-bought:
                price += p[0]*(buy - bought)
                bought += (buy - bought)

            else:
                price += p[0]*p[1]
                bought += p[1]
            if bought == buy:
                break

        return JsonResponse({'price':price}, status=200)



# Create your views here.
