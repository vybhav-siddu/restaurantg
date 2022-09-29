from django.contrib import admin
from .models import Customer
from .models import Dish
from .models import Drink
from .models import Order
from .models import Worker

admin.site.register(Customer)
admin.site.register(Dish)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(Worker)
