from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from guardian.admin import GuardedModelAdmin
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .models import User, Student, Teacher, Admin as AdminProfile
from .resources import UserResource

admin.site.unregister(Group)

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin, ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_classes = [UserResource]
    import_form_class = ImportForm
    export_form_class = ExportForm
    actions = ["make_active", "make_inactive"]

    @admin.action(description="Mark selected users as active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Mark selected users as inactive")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("email", "full_name", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name", "avatar")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("email", "full_name")
    ordering = ("email",)

@admin.register(Student)
class StudentAdmin(ModelAdmin, GuardedModelAdmin):
    list_display = ("user", "level", "created_at")
    search_fields = ("user__email", "user__full_name")

@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__email", "user__full_name")

@admin.register(AdminProfile)
class AdminProfileAdmin(ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user__email", "user__full_name")
