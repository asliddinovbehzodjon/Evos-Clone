from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Category,Product
class ProductInline(admin.TabularInline):
    model =  Product
    fields = ['name','image','about','price','discount']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        def render_change_form(self, request, context, *args, **kwargs):
            context['adminform'].form.fields['category'].queryset = Category.objects.filter(user=request.user)
            return super(ProductAdmin, self).render_change_form(request, context, *args, **kwargs)
        def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            else:
                return qs.filter(category__in=Category.objects.filter(user=request.user))
        list_display = ['Product_Image','name','category','price','Last_Updated','user']
        list_filter = ['category__name','discount']
        list_per_page = 10
        list_max_show_all = 15
        search_fields = ['name','category__name','price','discount']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_Image','name','user','Products_Count','Last_Updated']
    list_filter = ['updated']
    list_per_page = 10
    list_max_show_all = 15
    search_fields = ['name']
    list_display_links = ['Category_Image']
    inlines = [ProductInline]
    def render_change_form(self, request, context, *args, **kwargs):
            
            if request.user.is_superuser:
                context['adminform'].form.fields['user'].queryset = User.objects.all()
                return super(CategoryAdmin, self).render_change_form(request, context, *args, **kwargs)
            else:
                context['adminform'].form.fields['user'].queryset = User.objects.filter(username=request.user)
                return super(CategoryAdmin, self).render_change_form(request, context, *args, **kwargs)
    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            else:
                return qs.filter(user=request.user)
    
    