from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    biography = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Books(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='authors_books', default=None)
    # author related with Authors model with Foreign Key
    # With on_delete= models.CASCADE model, when you delete an author, their books are also deleted
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    stock = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    publish_date = models.DateField(blank=True)

    def __str__(self):
        return self.title
