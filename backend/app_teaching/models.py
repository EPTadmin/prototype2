from django.db import models
from django.conf import settings

from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.



role_choices = (
    ('P1','P1'),
    ('F1','F1'),
    ('UL','UL'),
    ('P2','P2'),
    ('F2','F2'),
    ('L','L'),
    ('Ext','Ext')
)

groupe_choices = (
    ('s','s'),
    ('p','p'),
    ('t','t'),
    ('i','i'),
    ('Ext','Ext'),
)

course_group_choices = (
    ('s','s'),
    ('p','p'),
    ('t','t'),
    ('i','i'),
)

course_type_choices = (
    ('O1','O1'),
    ('O2','O2'),
    ('FE','FE'),
    ('FP','FP'),
    ('MS','MS'),
    ('PH','PH'),
    ('-','-'),
)

semester_type_choices = (
    ('V','V'),
    ('H','H'),
)

studiepoeng_choices = (
    ('3,75','3,75'),
    ('7,5','7,5'),
    ('10,0','10'),
    ('15,0','15'),
    ('20,0','20'),
    ('30,0','30'),
)

roletype_choices = (
    ('Instituttleder','Instituttleder'),
    ('Nestleder forskning','Nestleder forskning'),
    ('Nestleder utdanning','Nestleder utdanning'),
    ('Faggruppeleder','Faggruppeleder'),
    ('Studieprogramleder','Studieprogramleder'),
    ('Leder - forskningsprosjekt','Leder - forskningsprosjekt'),
    ('WP leder - Forskningsprosjekt','WP leder - Forskningsprosjekt'),
    ('Leder - EU prosjekt','Leder - EU prosjekt'),
    ('WP leder - EU prosjekt','WP leder - EU prosjekt'),
    ('Antall PhD studenter','Antall PhD studenter'),
)

emne_choices = (
    ('L','L'),
    ('P','P'),

    
)
antall_time_choices = (
    ('50','50'),
    ('70','70'),
    ('100','100'),

)
arsverk_choices= (
    ('20','20'),
    ('80','80'),

)
class Course(models.Model):

    course_id = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )


    name= models.CharField(
        null=False,
        blank=False,
        max_length=200
    )



    type = models.CharField(choices = course_type_choices,
                            max_length=3,
                            default='-')
    group = models.CharField(choices = course_group_choices,
                            max_length=3,
                            default='-')
    semester = models.CharField(choices = semester_type_choices,
                            max_length=2,
                            default='-')
    studiepoeng = models.CharField(choices = studiepoeng_choices,
                            max_length=4,default='-'
                            )
    
    nb_student = models.IntegerField(
        null = True,
    )

    nb_vit= models.IntegerField(
        null = True,
    )
    nb_stud_ass= models.IntegerField(
        null = True,
    )
    


    def __str__(self):
        return self.course_id + ' ' + self.name
    
class Position_Activity(models.Model):
    type = models.CharField(choices = roletype_choices,
                            max_length=40,
                            default='-')
    emne = models.CharField(choices = emne_choices,
                            max_length=2,
                            default='-')
    antall_time = models.CharField(choices = antall_time_choices,blank=True,null=True,max_length=3
                            )
    arsverk = models.CharField(choices = arsverk_choices,blank=True,null=True,max_length=3
                            )
    
    def __str__(self):
        return self.type

class Person(models.Model):

    first_name = models.CharField(
        unique=False,
        null=False,
        blank=False,
        max_length=50
    )

    middle_name = models.CharField(
        unique=False,
        null=True,
        blank=True,
        max_length=50
    )

    last_name = models.CharField(
        unique=False,
        null=False,
        blank=False,
        max_length=50
    )

    position = models.CharField (null = False,blank=False,choices = role_choices,
                            max_length=3,default='-')
    groupe = models.CharField (null = False,blank=False,choices = groupe_choices,
                            max_length=3,default='-')  
     
    courses = models.ManyToManyField(
        Course,
        null = True,
        related_name='courses'
    )

    activities = models.ManyToManyField(
        Position_Activity,
        related_name='activities'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


class PersonCourse(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE) 
    course = models.ForeignKey(Course,on_delete=models.CASCADE) 

    amount = models.IntegerField()

    def __int__(self):
        return self.amount
    



class PersonActivity(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE) 
    activity = models.ForeignKey(Position_Activity,on_delete=models.CASCADE) 
    amount = models.FloatField()

    def __int__(self):
        return self.amount
    
