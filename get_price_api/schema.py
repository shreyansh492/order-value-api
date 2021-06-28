import marshmallow
from marshmallow import validate
from marshmallow import pre_load

from get_price_api import exceptions

class _OrderItemsSchema(marshmallow.schema.Schema):
    name = marshmallow.fields.Str(validate = validate.Length(max = 250))
    quantity = marshmallow.fields.Int(validate = validate.Range(max =100))
    price = marshmallow.fields.Int(validate = validate.Range(max =30000))
class _OrderOfferSchema(marshmallow.schema.Schema):
    offer_type = marshmallow.fields.Str()
    offer_val = marshmallow.fields.Int(validate = validate.Range(max =30000), required = False)

class OrderSchema(marshmallow.schema.Schema):
    order_items = marshmallow.fields.List(marshmallow.fields.Nested(_OrderItemsSchema))
    distance = marshmallow.fields.Int()
    offer = marshmallow.fields.Nested(_OrderOfferSchema, required = False)

    @pre_load
    def _validate_offer(self,data,**kwargs):
        distance = data.get('distance')
        offer_data = data.get('offer',{})
        if not offer_data:
            return data
        if offer_data.get('offer_type').upper() not in ['FLAT', 'DELIVERY']:
            raise exceptions.OfferTypeException
        if offer_data.get('offer_type').upper() == "FLAT":
            if not offer_data.get('offer_val',None):
                raise exceptions.OfferValException
        if type(distance) == int and distance > 300000:
            print("distance is : ",distance)
            raise exceptions.DistanceValException
        return data
