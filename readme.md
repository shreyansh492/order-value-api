GET-ORDER-VALUE

DESCRIPTION-
 This api let you calculate the order price when it is in the given format below:
      {
      "order_items": [
      {
      "name": "bread",
      "quantity": 2,
      "price": 2200
      },
      {
      "name": "butter",
      "quantity": 1,
      "price": 5900
      }
      ],
      "distance": 1200,
      "offer": {
      "offer_type": "FLAT",
      "offer_val": 1000
      }
      }

Constraints-
# quantity for any item should be less than 100
# Distance should be given in meters and should be less than 300000 m.
# Offer type can only take two values- ("FLAT", "DELIVERY") and is optional.
# Length of the name of an Item should be maximum 250 characters

Testing URL-
# http://localhost:8000/api/get-price/
