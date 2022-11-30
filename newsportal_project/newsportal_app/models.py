from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    postRat = 0
    comRat = 0

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        postRatSum = 0
        postRatSum += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        commentRatSum = 0
        commentRatSum += commentRat.get('commentRating')

        self.ratingAuthor = postRatSum * 3 + commentRatSum
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # NEWS = 'NW'
    # ARTICLE = 'AR'
    # CATEGORY_CHOICES = (
    #     (NEWS, 'Новость'),
    #     (ARTICLE, 'Статья'),
    # )

    # categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    categoryType = models.CharField(max_length=2)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def preview(self):
        return self.text[0:123] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    # def __str__(self):
    #     return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()



