from django.contrib import admin
from .models import Template, DataSource, RenderedFile


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'file')
    search_fields = ('name',)
    readonly_fields = ('uploaded_at',)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'file')
    search_fields = ('name',)
    readonly_fields = ('uploaded_at',)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


class RenderedFileAdmin(admin.ModelAdmin):
    list_display = ('get_template_name', 'get_datasource_name', 'uploaded_at', 'file')
    search_fields = ('template__name', 'datasource__name')
    readonly_fields = ('uploaded_at',)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    def get_template_name(self, obj):
        return obj.template.name if obj.template else 'No template'

    get_template_name.admin_order_field = 'template__name'
    get_template_name.short_description = 'Template Name'

    def get_datasource_name(self, obj):
        return obj.datasource.name if obj.datasource else 'No datasource'

    get_datasource_name.admin_order_field = 'datasource__name'
    get_datasource_name.short_description = 'Datasource Name'


admin.site.register(Template, TemplateAdmin)
admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(RenderedFile, RenderedFileAdmin)
