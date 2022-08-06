from dataclasses import dataclass
import json
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company

# Create your views here.
class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,  *args, **kwargs):
       return super().dispatch(request, *args, **kwargs)

#===================== GET ALL DATA FROM DB ======================  
    def get(self, request, id=0):
        if (id > 0):
            company = list(Company.objects.filter(id=id).values())
            if (len(company) > 0):
                return JsonResponse(company[0], safe=False)
            else:
                return JsonResponse({'message': 'Not found'})    

        else:  
            companys = list (Company.objects.values())
            if len(companys) > 0:
                data = { 'message': 'Success', 'companys': companys }
            else :
                data = { 'message': 'No data' }    
            return JsonResponse (data)
#===================== GET ALL DATA FROM DB ====================== 

        

#===================== POST DATA FROM DB =========================  
    def post(self, request):
        print(request.body)
        # convert json to dict
        jd= json.loads(request.body)
        Company.objects.create( name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        data = { 'message': 'Success' }
        return JsonResponse (data)
      
#===================== POST DATA FROM DB =========================          



#===================== PUT DATA FROM DB ===?======================
    def put(self, request, id=0):
        jd= json.loads(request.body)
        company = list(Company.objects.filter(id=id).values())
        if (len(company) > 0):
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            data = { 'message': 'Success' }
        else:
            data = { 'message': 'Not found' }
        
        return JsonResponse (data)
#===================== PUT DATA FROM DB ==========================



#===================== DELETE DATA FROM DB =======================
    def delete(self, request, id=0):
        company = list(Company.objects.filter(id=id).values())
        if (len(company) > 0):
            company = Company.objects.filter(id=id)
            company.delete()
            data = { 'message': 'Success' }
        else:
            data = { 'message': 'Not found' }  
        
        return JsonResponse (data)

#===================== DELETE DATA FROM DB =======================
    