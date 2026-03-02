from django.contrib import admin
from django.utils.html import format_html
from .models import Categories, Product


# =====================================
# CATEGORY ADMIN
# =====================================
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = ("id", "category")
    search_fields = ("category",)
    ordering = ("id",)


# =====================================
# PRODUCT ADMIN
# =====================================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # columns shown in admin table
    list_display = (
        "id",
        "name",
        "price",
        "category",
        "image_preview",
    )

    # search bar
    search_fields = (
        "name",
        "description",
    )

    # right sidebar filters
    list_filter = (
        "category",
    )

    ordering = ("id",)

    # image preview inside edit page
    readonly_fields = ("image_preview",)

    # thumbnail preview
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" '
                'style="object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"