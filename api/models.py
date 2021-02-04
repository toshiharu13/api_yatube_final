from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)

class Follow(models.Model):
    # ссылка на объект пользователя, который подписывается
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    # ссылка на объект пользователя, на которого подписываются
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following', 'user'], name='uni_foll')
        ]

class Group(models.Model):
    title = models.CharField(
        max_length=200, help_text='Дайте короткое название группе',
        verbose_name="группа/сообщество"
    )
    #slug = models.SlugField(unique=True, max_length=20)
    #description = models.TextField()

    def __str__(self):
        return self.title