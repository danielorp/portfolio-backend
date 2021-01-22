from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    home_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    short_description = models.TextField(null=True, blank=True)
    post_text = models.TextField(null=True, blank=True)
    use_in_home_screen = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Contact(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    contact_text = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.portfolio.name