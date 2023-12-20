from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
import json
from .models import About , Work , Education
from .serials import * 

class AboutView(ListCreateAPIView):

    def create(self, request, *args, **kwargs):
        # return super().create(request, *args, **kwargs)


        return Response({'data':'Data inserted successfully'})
    

    def response_format(self ):

        response_format ='''
        {
        "Name": "Rachit Saxena",
        "Desc": "",
        "email_id":"",
        "website":"",
        "linkedin_url":"",
        "phone":"",
        "Skills": ["python", "Django"],
        "Work Experience" : [
            {
                "Title":"SDE-II",
                "Company Name" : "UST Global",
                "Start Date" : "01/06/2023",
                "End Date" : null , 
                "Desc" : "",
                "Skills" : ["python" , "django" , "react"]
            },
            ],

        "Education":[
        
            {
             "School Name": "IEC",
             "start_date" "01/06/2018",
             "end_date": "31/05/2022",
             "Title": "B.Tech"   
            }
            ]
        }
        ''' 
        return response_format
    
    def list(self , request):
        try:
            #Must Refactor this code and convert this into serializer class to add validation 

            obj = About.objects.first()
            if not obj:
                raise Exception("No About Object Found")   
            
            response = {
                "name": obj.name,
                "desc": obj.desc,
                "skills": obj.skills.split(','),
                "email_id": obj.email_id,
                "website":obj.website,
                "linkedin_url":obj.linkedin_url,
                'phone':obj.phone,  
                "work_experience": self.fetch_work_experience(obj.work_experience),
                "education": self.fetch_education(obj.education)
            
            }
            return Response(response) 
        except Exception as E:
            return Response({'status':400 , "data": str(E)})

    def fetch_education(self , education):
        output = []

        for i in education.all():
            education_instance = {
                "school_name": i.school_name,
                "start_date" :str(i.start_date),
                "end_date": str(i.end_date),
                "title": str(i.title)
            }
            output.append(education_instance)
        return output

    def fetch_work_experience(self , work_experience):
        output = []
        for i in work_experience.all():
            work_instance = {
                "title": i.title,
                "company_name" : i.company_name,
                "start_date" : str(i.start_date),
                "end_date" : str(i.end_date) , 
                "desc" : i.desc if i.desc else "",
                "skills" : i.skills.split(',') if i.skills else ""
            }
            output.append(work_instance)

        return output

class ProjectView(ListCreateAPIView):
    pass 


class WorkView(ListCreateAPIView):

    def list(self ,request , *args , **kwargs):

        obj = Work.objects.all() 

        serial_obj = WorkSerializer(obj , many=True)
        return Response(serial_obj.data)
    


    def create(self ,request , *args , **kwargs):
        try:
            input_data = request.data

            serial = WorkSerializer(data=input_data)
            if serial.is_valid():
                # serial.save()
                pass 
            else:
                raise Exception('')
            
            return Response({'data':'worked'})
        except Exception as E:
            return Response({'error':str(E)})
    
