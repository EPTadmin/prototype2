from rest_framework import serializers
from . models import *


    
    
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')

class PositionActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Position_Activity
        field = ['__all__']

class PersonSerializers(serializers.ModelSerializer):
#    courses = CourseSerializers(many = True,read_only=True)  
#    activities = PositionActivitySerializers(read_only=True,many=True)   
   class Meta:
        model = Person
        # fields = ('__all__')
        fields = ('id','first_name','last_name','courses','position','groupe','activities')




class PersonCourseSerializers(serializers.ModelSerializer):
    # person = serializers.CharField(source="person.first_name", read_only=True)    
    # course = serializers.CharField(source="course.course_id", read_only=True)    

    class Meta:
        model = PersonCourse
        fields = ['person','course', 'amount']


# class PersonActivitySerializers(serializers.ModelSerializer):
#     # person = serializers.CharField(source="person.first_name", read_only=True)    
#     # activity = serializers.CharField(source="course.course_id", read_only=True)    

#     class Meta:
#         model = PersonActivity
#         field = ['__all__']

    