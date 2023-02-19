from rest_framework import serializers

from contacts.models import Contact


class ContactHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
