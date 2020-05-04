import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):

    class Meta:

        CHOICES = (
            
            ('ascending', 'Ascending'),
            ('descending', 'descending')


        )

        model = Game
        fields = {

     'title': ['icontains'],

         'tags' : ['icontains'] , 
         'genres' :['icontains'],
         'developers' : ['icontains'], 
         'platforms' : ['icontains'],
         



        }

    def filter_by_order(self,queryset, name, value):
        expression = 'title' if value == 'ascending' else '-title'
        return queryset.order_by(expression)

    
         # {{filter.form|bootstrap}}
