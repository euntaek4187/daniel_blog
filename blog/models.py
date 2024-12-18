from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    # blank=True는 필수 입력값이 아니라는 뜻
    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d/", blank=True)

    # auto_now_add=True 를 해줘야 추후에 글 생성시, 시간 등을 선택하지 않고 자동반영 될 수 있음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # f-string 기법
    def __str__(self):
        # 포스트의 pk 값 , 포스트의 title 값
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'