from django.contrib import admin
from .models import Student, Company, Timings, Batch, \
    TutorBatch, StudentBatch, Subject, Assessment
from import_export.admin import ImportExportMixin


class StudentAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Company)
admin.site.register(Timings)
admin.site.register(Batch)
admin.site.register(TutorBatch)
admin.site.register(StudentBatch)
admin.site.register(Subject)
admin.site.register(Assessment)
