from django.contrib import admin
from .models import  *

#Zero modele
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','nom')
#Premier modele
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'desc','num','date_creation','date_mis_Ajour','image','category')

#Deuxieme modele
class CommentAdmin(admin.ModelAdmin):
    list_display = ('contenu','nom','email','corps','date_creation','date_mis_Ajour')
    
       
admin.site.register(Category,  CategoryAdmin)
admin.site.register(Article, BlogAdmin)
admin.site.register(Commentaire, CommentAdmin)
