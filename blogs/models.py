from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    topic = models.CharField('Тема поста',max_length=256)
    text = models.TextField('Текст поста')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField('Изображение', upload_to='image/%Y',blank=True,null=True, default=None)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.topic}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.topic}'