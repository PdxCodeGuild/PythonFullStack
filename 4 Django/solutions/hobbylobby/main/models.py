from django.db import models


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='cities')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.state.name + ' - ' + self.name


# null=True allows you to have null values in a column in your table
# blank=True allows you to enter in a blank value in the admin panel
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    # blank=True allows us to save a blank string for the middle name in the admin panel
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='customers')
    notes = models.TextField()
    send_newsletter = models.BooleanField()
    age = models.IntegerField(null=True, blank=True)
    customer_points = models.FloatField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + ' ' + ('' if len(self.middle_name) == 0 else self.middle_name[0] + '.') + ' ' + self.last_name

    def city_state(self):
        print(type(self.city))
        return self.city.name + ', ' + self.city.state.name
    
    def get_age_or_dash(self):
        if self.age is not None:
            return self.age
        else:
            return '-'