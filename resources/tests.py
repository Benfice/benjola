from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Resource, Comment


class ResourceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="commentuser",
            email="commentuser@email.com",
            password="compass123",
        )

        cls.special_permission = Permission.objects.get(
            codename="special_status"
        )

        cls.resource = Resource.objects.create(
            title="Assimil - Apprendre le serbe",
            description="Méthode pour apprendre le serbe.",
            url="https://www.assimil.com/fr/9791-apprendre-le-serbe",
            language="FR",
        )

        cls.comment = Comment.objects.create(
            resource=cls.resource,
            author=cls.user,
            comment="A great resource to learn Serbian!",
        )

    def test_resource_listing(self):
        self.assertEqual(f"{self.resource.title}", "Assimil - Apprendre le serbe")
        self.assertEqual(f"{self.resource.description}", "Méthode pour apprendre le serbe.")
        self.assertEqual(f"{self.resource.url}", "https://www.assimil.com/fr/9791-apprendre-le-serbe")
        self.assertEqual(f"{self.resource.language}", "FR")
    
    def test_resource_list_view_for_logged_in_user(self):
        self.client.login(email="commentuser@email.com", password="compass123")
        response = self.client.get(reverse("resource_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Assimil - Apprendre le serbe")
        self.assertTemplateUsed(response, "resources/resource_list.html")

    def test_resource_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("resource_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/resources/" % (reverse("account_login")))
        response = self.client.get(
            "%s?next=/resources/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_resource_detail_view_with_permission(self):
        self.client.login(email="commentuser@email.com", password="compass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.resource.get_absolute_url())
        no_response = self.client.get("/resources/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Méthode pour apprendre le serbe.")
        self.assertContains(response, "A great resource to learn Serbian!")
        self.assertTemplateUsed(response, "resources/resource_detail.html")