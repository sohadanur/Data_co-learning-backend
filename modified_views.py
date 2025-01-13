import json
from django.http import JsonResponse
from data.models import Country, State, City  # Import your models
#from django.db import transaction 

import json
from django.http import JsonResponse
from data.models import Country, State, City

def show_country(request, country_name):
    if request.method == "GET":
        try:
            # Retrieve the country by name
            country = Country.objects.get(name=country_name)
            
            # Return the country's details
            return JsonResponse({
                "id": country.id,
                "name": country.name,
                "sortname": country.sortname,
                "phonecode": country.phonecode,
            })
        except Country.DoesNotExist:
            return JsonResponse({"error": f"Country '{country_name}' does not exist"}, status=404)
        
def show_city(request, country_name):
    if request.method == "GET":
        try:
            # Find the country by name
            country = Country.objects.get(name=country_name)

            # Retrieve all states for the country
            states = State.objects.filter(country=country)

            # Retrieve all cities in the states of this country
            cities = City.objects.filter(state__in=states).values("id", "name", "state_id")
            city_list = list(cities)  # Convert QuerySet to a list of dictionaries

            return JsonResponse({"cities": city_list}, safe=False)

        except Country.DoesNotExist:
            return JsonResponse({"error": f"Country '{country_name}' does not exist"}, status=404)
        
def show_state(request, country_name):
    if request.method == "GET":
        try:
            # Find the country by name
            country = Country.objects.get(name=country_name)

            # Retrieve all states for the country
            states = State.objects.filter(country=country).values("id", "name", "country_id")
            state_list = list(states)  # Convert QuerySet to a list of dictionaries

            return JsonResponse({"states": state_list}, safe=False)

        except Country.DoesNotExist:
            return JsonResponse({"error": f"Country '{country_name}' does not exist"}, status=404)
        
        
#Shows list of all countries 
# def show_country(request):
#     if request.method == "GET":
#         # Retrieve all countries
#         countries = Country.objects.values("name")
#         country_list = [country["name"] for country in countries]
#         return JsonResponse({"countries": country_list}, safe=False)

# #To show the NAMES of the states only
# def show_state(request, country_name):
#     if request.method == "GET":
#         try:
#             # Find the country by name
#             country = Country.objects.get(name=country_name)

#             # Retrieve all states for the country
#             states = State.objects.filter(country=country).values("name")
#             state_list = [state["name"] for state in states]
#             return JsonResponse({"states": state_list}, safe=False)

#         except Country.DoesNotExist:
#             return JsonResponse({"error": f"Country '{country_name}' does not exist"}, status=404)
        
# #To see the list of the names of the cities only
# def show_city(request, country_name):
#     if request.method == "GET":
#         try:
#             # Find the country by name
#             country = Country.objects.get(name=country_name)

#             # Retrieve all states for the country
#             states = State.objects.filter(country=country)

#             # Retrieve all cities in the states of this country
#             cities = City.objects.filter(state__in=states).values("name")
#             city_list = [city["name"] for city in cities]

#             return JsonResponse({"cities": city_list}, safe=False)

#         except Country.DoesNotExist:
#             return JsonResponse({"error": f"Country '{country_name}' does not exist"}, status=404)

# def show_city(request, state_name):
#     if request.method == "GET":
#         try:
#             # Find the state by name
#             state = State.objects.get(name=state_name)

#             # Retrieve all cities for the state
#             cities = City.objects.filter(state=state).values("name")
#             city_list = [city["name"] for city in cities]
#             return JsonResponse({"cities": city_list}, safe=False)

#         except State.DoesNotExist:
#             return JsonResponse({"error": f"State '{state_name}' does not exist"}, status=404)


###To just get the countries in json body

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
