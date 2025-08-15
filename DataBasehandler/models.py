from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PythonQues(models.Model):
    question=models.CharField()
    option_a=models.CharField()
    option_b=models.CharField()
    option_c=models.CharField()
    option_d=models.CharField()
    correct_answer=models.CharField()


class DjangoQues(models.Model):
    question=models.CharField()
    option_a=models.CharField()
    option_b=models.CharField()
    option_c=models.CharField()
    option_d=models.CharField()
    correct_answer=models.CharField()


class JavaQues(models.Model):
    question=models.CharField()
    option_a=models.CharField()
    option_b=models.CharField()
    option_c=models.CharField()
    option_d=models.CharField()
    correct_answer=models.CharField()


class CppQues(models.Model):
    question=models.CharField()
    option_a=models.CharField()
    option_b=models.CharField()
    option_c=models.CharField()
    option_d=models.CharField()
    correct_answer=models.CharField()



