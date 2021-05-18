from django.contrib import admin
from .models import Testimonial, Website, Form, Post, Comment
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass