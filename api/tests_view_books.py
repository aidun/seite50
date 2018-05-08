from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models_book import Book

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_api_can_create_a_book(self):
        self.book_data = {'bookid': "1234",
                          'title': "TestBuch",
                          'description': "Ein Buch über das Testen",
                          'published_date': "2018-05-07",
                          'seite50_sentence': "Uch wie ist das schön",
                          }

        self.response = self.client.post(
            reverse('create'),
            self.book_data,
            format="json"
        )

        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)

    def test_api_can_get_a_book(self):
        book = Book.objects.get()
        response = self.client.get(
            reverse('details',kwargs={'pk': book.id}),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response,book)

    def test_api_can_update_book(self):
        book = Book.objects.get()#

        change_book = {'title': "new"}
        res = self.client.put(
           reverse('details', kwargs={'pk': book.id}),
           change_book, format='json'
        )

       self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_book(self):
        book = Book.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk':book.id}),
            format='json', follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)