from rest_framework import serializers
from .models import Contact, Sponsorship


class ContactSerializer(serializers.ModelSerializer):
     class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class SponsorshipSerializer(serializers.ModelSerializer):
     class Meta:
        model = Sponsorship
        fields = ['email', 'company_name', 'contact_person', 'designation', 'proposal']