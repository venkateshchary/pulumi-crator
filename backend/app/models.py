from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='genres')

"""
# Assume authors/publishers already exist
dune = Book.objects.create(title="Dune", author=herbert, publisher=ace_books)
neuromancer = Book.objects.create(title="Neuromancer", author=gibson, publisher=ace_books)
hobbit = Book.objects.create(title="The Hobbit", author=tolkien, publisher=allen_unwin)
foundation = Book.objects.create(title="Foundation", author=asimov, publisher=gnome_press)

sci_fi = Genre.objects.create(name="Sci-Fi")
adventure = Genre.objects.create(name="Adventure")
fantasy = Genre.objects.create(name="Fantasy")
cyberpunk = Genre.objects.create(name="Cyberpunk")

# M2M links are set via .add(), .set(), or on either side — doesn't matter which
dune.genres.set([sci_fi, adventure])
neuromancer.genres.set([sci_fi, cyberpunk])
hobbit.genres.set([fantasy, adventure])
foundation.genres.set([sci_fi])

"""