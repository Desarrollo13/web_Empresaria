from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "author", "published", "post_categories")
    ordering = ("author", "published")
    # filtra por autor y categorias que son compuestas
    search_fields = ("title", "content", "author__username", "categories__name")
    # filtro por fechas
    date_hierarchy = "published"
    # filtra con una relacion comupesta autor
    list_filter = ("author__username", "categories__name")

    # para poder mostrar una fila caterias ya que es una relacion muchos a muchos
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
