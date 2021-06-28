class OfferTypeException(Exception):
    message = "Offer type can be FLAT or DELIVERY"
    error_code = "InvalidOfferType"

class OfferValException(Exception):
    message = "Offer value should be provided with FLAT type"
    error_code = "InvalidOfferVal"

class DistanceValException(Exception):
    message = "Distance should not exceed 300 KM"
    error_code = "InvalidDistanceVal"
