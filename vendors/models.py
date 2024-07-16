from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    STATUS_CHOICES = [
        ('activated', 'Activated'),
        ('declined', 'Declined'),
        ('pending', 'Pending'),
    ]

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Address(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='addresses', on_delete=models.CASCADE)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class VendorCategory(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ContactPerson(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='contact_persons', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ContactNumber(models.Model):
    contact_person = models.ForeignKey(ContactPerson, related_name='contact_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

class Email(models.Model):
    contact_person = models.ForeignKey(ContactPerson, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField()

class Agent(models.Model):
    name = models.CharField(max_length=255)

class ActivationProcess(models.Model):
    STATUS_CHOICES = [
        ('email', 'Email'),
        ('identify_contact_person', 'Identify the contact person'),
        ('items_analysis', 'Items Analysis'),
        ('gain_stock_list', 'Gain Stock List'),
        ('activated', 'Activated'),
        ('lost', 'Lost'),
    ]

    vendor = models.OneToOneField(Vendor, related_name='activation_process', on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='email')
    notes = models.TextField(blank=True, null=True)

class Task(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class Note(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
