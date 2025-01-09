import json
from django.http import JsonResponse
from data.models import Country, State, City  # Import your models
#from django.db import transaction

def add_country(request):#Only shows in postman not used in database
    if request.method == "GET":
        try:
            # Parse the JSON data from the request body
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            
            # Ensure the payload is a list
            if not isinstance(body_data, list):
                return JsonResponse({"error": "Payload must be a list of JSON objects"}, status=400)
            # Return the same JSON payload back
            return JsonResponse(body_data, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)  

def add_state(request):#Only shows in postman not used in database
    if request.method == "GET":
        try:
            # Parse the JSON data from the request body
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            
            # Ensure the payload is a list
            if not isinstance(body_data, list):
                return JsonResponse({"error": "Payload must be a list of JSON objects"}, status=400)
            # Return the same JSON payload back
            return JsonResponse(body_data, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)        

def add_city(request):#Only shows in postman not used in database
    if request.method == "GET":
        try:
            # Parse the JSON data from the request body
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            
            # Ensure the payload is a list
            if not isinstance(body_data, list):
                return JsonResponse({"error": "Payload must be a list of JSON objects"}, status=400)
            
            # Return the same JSON payload back
            return JsonResponse(body_data, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        
####################################################################     

# def add_country(request):
#     if request.method == "GET":
#         try:
#             # Parse the JSON data from the request body
#             body_unicode = request.body.decode('utf-8')
#             body_data = json.loads(body_unicode)
            
#             # Save to the database
#             country = Country.objects.create(
#                 id=body_data["id"],
#                 sortname=body_data["sortname"],
#                 name=body_data["name"],
#                 phonecode=body_data["phonecode"],
#             )
#             country.save()
            
#             # Return the same JSON payload back
#             return JsonResponse(body_data, safe=False)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)   
# def add_city(request): #For saving in the database
#     if request.method == "GET":
#         try:
#             # Parse the JSON data from the request body
#             body_unicode = request.body.decode('utf-8')
#             body_data = json.loads(body_unicode)
            
#             # Ensure the state_id exists in the database
#             state = State.objects.get(id=body_data["state_id"])
            
#             # Save to the database
#             city = City.objects.create(
#                 id=body_data['id'],
#                 name=body_data["name"],
#                 state_id=state.id,
#             )
#             city.save()
            
#             # Return the same JSON payload back
#             return JsonResponse(city, safe=False)
#         except State.DoesNotExist:
#             return JsonResponse({"error": f"State with id {body_data['state_id']} does not exist"}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON data"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
# def add_state(request):
#     if request.method == "GET":
#         try:
#             # Parse the JSON data from the request body
#             body_unicode = request.body.decode('utf-8')
#             body_data = json.loads(body_unicode)
            
#             # Ensure the country_id exists in the database
#             country = Country.objects.get(id=body_data["country_id"])
            
            # # Save to the database
            # state = State.objects.create(
            #     id=body_data["id"],
            #     name=body_data["name"],
            #     country=country,
            # )
            # state.save()
            
        #     # Return the same JSON payload back
        #     return JsonResponse(body_data, safe=False)
        # except Country.DoesNotExist:
        #     return JsonResponse({"error": f"Country with id {body_data['country_id']} does not exist"}, status=400)
        # except json.JSONDecodeError:
        #     return JsonResponse({"error": "Invalid JSON data"}, status=400)
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=400)
        
################################To save only in the get request