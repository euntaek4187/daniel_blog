import os
import django
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

# Django 설정 초기화
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daniel_blog.settings")  # 프로젝트 이름에 맞게 변경
django.setup()

# 환경 변수에서 값 가져오기
client_id = os.getenv("SOCIALAPP_CLIENT_ID")
secret = os.getenv("SOCIALAPP_SECRET")

# Site 설정
site = Site.objects.get_or_create(domain="127.0.0.1:8000", name="Localhost")[0]

# SocialApp 설정
social_app = SocialApp.objects.create(
    provider="google",
    name="Google OAuth",
    client_id = 144736340574-a4fukokks5u4jt82v4gnifkka03t0542.apps.googleusercontent.com,
    secret = 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
)
social_app.sites.add(site)

print("SocialApp created successfully!")
