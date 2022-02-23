from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from .models import SupportedApp, SupportedAppParam, RiskRecomendation




@api_view(['POST'])
def getRiskList(request):
    response = {"message": "Something went wrong!"}
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        appName = pythonData.get('app')
        if appName:
            app = SupportedApp.objects.get(name=appName)
            
            if app:
                supportedParams = SupportedAppParam.objects.filter(app_id=app.id)
                params = pythonData.get("params")
                responseData = []
                for param in params:
                    paramData = {
                        "param_name": param,
                        "risk_recommendations": []
                    }
                    for supportedP in supportedParams:
                        if supportedP.param_id.name == param:
                            if supportedP.param_id.id:
                                risks = RiskRecomendation.objects.filter(param_id=supportedP.param_id.id)
                                returnNames = []
                                for risk in risks:
                                    returnNames.append(risk.name)
                                paramData['risk_recommendations'] = returnNames
                            

                    responseData.append(paramData)
                    finalResponse = {
                        "status":"Success",
                        "message": "Response successful.",
                        "data": {
                            "app": appName,
                            "param_data": responseData
                        }
                    }
                json_data = JSONRenderer().render(finalResponse)
                return HttpResponse(json_data, status=status.HTTP_200_OK, content_type="application/json")
            else:
                return HttpResponse({"message":"App not supported."}, status=status.HTTP_200_OK, content_type="application/json")
        
        return HttpResponse(response, status=status.HTTP_400_BAD_REQUEST,content_type="application/json")