from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        # суммарный рейтинг всех комментариев к статьям автора
        post_rating = self.post_set.all().aggregate(postRating=Sum('rating'))
        post_rat = 0
        post_rat += post_rating.get('postRating')

        # суммарный рейтинг всех комментариев автора
        com_rating = self.author_user.comment_set.all().aggregate(commentRating=Sum('rating_comment'))
        com_rat = 0
        com_rat += com_rating.get('commentRating')

        # суммарный рейтинг каждой статьи автора умножается на 3
        self.rating_author = post_rat * 3 + com_rat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NE'
    ARTICLE = 'AR'
    TYPES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )

    category_types = models.CharField(max_length=2, choices=TYPES, default=ARTICLE)
    date_create = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.author_user.username}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    post_models = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_models = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.comment_post.author.author_user.username}'

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
