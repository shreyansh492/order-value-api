from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from get_price_api.serializers import OrderSerializer
from get_price_api import decorators
from get_price_api import schema

class GetPrice(APIView):

    # serializer_class= OrderSerializer
    @decorators.validate_post_data(schema.OrderSchema())
    def post(self,request,data):# use data instead of request.data

        def delivery_cost(distance):
            cost = 0
            if distance<=10000 :
                cost+= 5000
            elif distance<=20000:
                cost += 10000
            elif distance<= 50000:
                cost += 50000
            else:
                cost += 100000
            return cost

        total_cost = 0
        order_items = request.data['order_items']
        offer = request.data.get('offer',{})
        offer_type = request.data.get('offer',{}).get('offer_type')
        offer_val = request.data.get('offer',{}).get('offer_val')
        distance = request.data['distance']

        for i in order_items:
            total_cost += i['quantity']*i['price']

        if offer_type == "FLAT":
            total_cost += delivery_cost(distance)

            total_cost = max(total_cost - offer_val,0)
        elif offer_type == "DELIVERY":
            pass
        else:
            total_cost += delivery_cost(distance)

        return Response({'order_total':total_cost })
