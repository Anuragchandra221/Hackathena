from django.db import models

# Create your models here.
class Questions(models.Model):

    name = models.CharField(max_length=50)
    
    option_one = models.BooleanField()
    option_one_lower = models.IntegerField()
    option_one_upper = models.IntegerField()

    option_two = models.BooleanField()
    option_two_lower = models.IntegerField()
    option_two_upper = models.IntegerField()

    option_three = models.BooleanField()
    option_three_lower = models.IntegerField()
    option_three_upper = models.IntegerField()

    option_four = models.BooleanField()
    option_four_lower = models.IntegerField()
    option_four_upper = models.IntegerField()

    option_five = models.BooleanField()
    option_five_lower = models.IntegerField()
    option_five_upper = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
