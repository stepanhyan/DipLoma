from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField('Username', max_length=28, default='')

    def __str__(self):
        return f"User {self.user}"


class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Composition name', max_length=50)
    image = ProcessedImageField(upload_to='images/', default='',
                                blank=True,
                                processors=[ResizeToFill(320, 320)],
                                format='JPEG',
                                options={'quality': 100})
    audio = models.FileField(upload_to='audio/', default='')
    likes_users = models.ManyToManyField(UserProfile, related_name='liked_songs', default=0)
    # comments_users = models.ManyToManyField(UserProfile, related_name='commented_songs', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.song.title}"


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user} on {self.song.title}"
