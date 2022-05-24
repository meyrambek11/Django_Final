from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Book, Journal
from api.serializers import BookSerializer, BookCreateSerializer, BookUpdateSerializer, \
    JournalSerializer, JournalCreateSerializer, JournalUpdateSerializer
from autho.permissions import IsAdminMember


class BookBaseViewSet(viewsets.GenericViewSet):

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'get_books':
            return BookSerializer
        elif self.action == 'update_book':
            return BookUpdateSerializer
        elif self.action == 'create_book':
            return BookCreateSerializer
        return

    def get_permissions(self):
        if self.action in ('update_book', 'create_book'):
            self.permission_classes = (IsAuthenticated, IsAdminMember)
        return super().get_permissions()

    def get_books(self, request, *args, **kwargs):
        result = self.get_serializer(self.get_queryset(), many=True)
        return Response(result.data)

    def update_book(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

    def create_book(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class JournalBaseViewSet(viewsets.GenericViewSet):

    def get_queryset(self):
        return Journal.objects.all()

    def get_serializer_class(self):
        if self.action == 'get_journals':
            return JournalSerializer
        elif self.action == 'update_journal':
            return JournalUpdateSerializer
        elif self.action == 'create_journal':
            return JournalCreateSerializer
        return

    def get_permissions(self):
        if self.action in ('update_journal', 'create_journal'):
            self.permission_classes = (IsAuthenticated, IsAdminMember)
        return super().get_permissions()

    def get_journals(self, request, *args, **kwargs):
        result = self.get_serializer(self.get_queryset(), many=True)
        return Response(result.data)

    def update_journal(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)

    def create_journal(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()
