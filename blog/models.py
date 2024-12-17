from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    # auto_now_add=True 를 해줘야 추후에 글 생성시, 시간 등을 선택하지 않고 자동반영 될 수 있음
    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 포스트의 pk 값 , 포스트의 title 값
        return f"[{self.pk}] {self.title}"