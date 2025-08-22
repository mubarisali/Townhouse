from django.db import models

class Villa(models.Model):
    VILLA_TYPES = (
        ('townhouse', 'Townhouse'),
        ('villa', 'Villa'),
    )
    name = models.CharField(max_length=100)
    villa_type = models.CharField(max_length=20, choices=VILLA_TYPES)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area_sqft = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='villas/')
    floor_plan = models.FileField(upload_to='floorplans/', blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    name = models.CharField(max_length=200, blank=True)  # Only one name field
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)

    # For second form fields
    property_type = models.CharField(max_length=50, blank=True)
    bedroom_type = models.CharField(max_length=50, blank=True)
    requirements = models.TextField(blank=True)

    # Optional meta info
    page_url = models.URLField(blank=True)
    referrer = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Enquiry #{self.pk}"

