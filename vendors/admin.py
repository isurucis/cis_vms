from django.contrib import admin
from .models import (
    Country, Vendor, Address, Category, VendorCategory,
    ContactPerson, Agent,
    ActivationProcess, Task, Note
)

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

class ContactPersonInline(admin.TabularInline):
    model = ContactPerson
    extra = 1

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

class VendorCategoryInline(admin.TabularInline):
    model = VendorCategory
    extra = 1

    def has_view_or_change_permission(self, request, obj=None):
        # Return True or implement custom logic to determine view/change permission
        return True
        
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'website', 'country', 'status')
    list_filter = ('status', 'country')
    search_fields = ('name', 'code')
                     
    inlines = [VendorCategoryInline, ContactPersonInline, AddressInline, NoteInline, TaskInline]  


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'address_line', 'city', 'state', 'postal_code')
    list_filter = ('city', 'state')
    search_fields = ('address_line', 'city', 'state', 'postal_code')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(VendorCategory)
class VendorCategoryAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'category')

@admin.register(ContactPerson)
class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'name')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ActivationProcess)
class ActivationProcessAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'agent', 'status')
    list_filter = ('status',)
    search_fields = ('vendor__name', 'agent__name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'description', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('description', 'vendor__name')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'vendor__name')
    readonly_fields = ('created_at',)
