from import_export import resources
from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'full_name', 'role', 'is_active', 'is_staff')
        export_order = ('user_id', 'email', 'full_name', 'role', 'is_active', 'is_staff')
