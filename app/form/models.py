from django.db import models


# Create your models here.

class Faculty(models.Model):
    faculty = models.CharField(max_length=200, null=False, blank=False, unique=True)

    def __str__(self):
        return self.faculty


class University(models.Model):
    university = models.CharField(max_length=200, null=False, blank=False, unique=True
                                  )
    faculties = models.ManyToManyField('Faculty')

    def __str__(self):
        return self.university


class TimeSlot(models.Model):
    time = models.TimeField()
    date = models.DateField()
    capacity = models.IntegerField(default=20)

    def __str__(self):
        return '{}|{}'.format(self.time, self.date)


class FormApplierModel(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    mobile_number = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    university_other = models.CharField(max_length=100, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    faculty_other = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=50, null=True)
    department_other = models.CharField(max_length=100, null=True)
    academic_year = models.CharField(max_length=50)
    first_preference = models.CharField(max_length=50)
    second_preference = models.CharField(max_length=50)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    is_interviewed = models.BooleanField(default=0)
    data_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
