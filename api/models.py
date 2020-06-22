from django.db import models


class Student(models.Model):
    GENDERS=(
        ("f","female"),
        ("m","male"),
        ("u","undisclosed")
    )
    name = models.CharField(max_length = 100)
    roll_number = models.IntegerField(unique =  True)
    email = models.EmailField(max_length = 100)
    gender = models.CharField(max_length = 1 , choices = GENDERS)
    age = models.IntegerField()
    percentage = models.FloatField()

    institute = models.ForeignKey("Institute",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Institute(models.Model):
    TYPE=(
        ("c","college"),
        ("h","highschool")
    )
    name = models.CharField(max_length = 200)
    type_of_institute = models.CharField(max_length = 256 , choices = TYPE)

    def __str__(self):
        return self.name






