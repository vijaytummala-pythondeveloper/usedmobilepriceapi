from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import *

@api_view(['GET', 'POST', 'DELETE'])
def getPrice(request):
    mobile_data = request.data
    brand = give_mobileid("OPPO")
    model = give_modelid('A12')
    data_predict = [[brand,model,mobile_data['Memory'],mobile_data["Storage"],mobile_data['Rating']]]

    data = {
        'message': predict(data_predict),
    }
    return Response(data)