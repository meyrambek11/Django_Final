from django.urls import path

from api.views import BookBaseViewSet, JournalBaseViewSet

urlpatterns = [
    path(
        'books',
        BookBaseViewSet.as_view({
            'get': 'get_books',
            'put': 'update_book',
            'post': 'create_book'
        }),
        name='books'
    ),
    path(
        'journals',
        JournalBaseViewSet.as_view({
            'get': 'get_journals',
            'put': 'update_journal',
            'post': 'create_journal'
        }),
        name='journals'
    ),
]
