from rest_framework import serializers
from .models import Customer
from .models import Dish
from .models import Drink
from .models import Order
from .models import Worker

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','contact_number','address']

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id','name','price','description']

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','price','description']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','table_number','items']

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id','name','department','contact_number']