from crud_rest_framework.serializers import ContactHyperlinkedSerializer
from rest_framework import viewsets, permissions, generics
from contacts.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactViewApi(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactCreateApi(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]
