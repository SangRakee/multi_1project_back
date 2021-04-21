from rest_framework import serializers
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['memoId', 'memoTitle', 'memoContent', 'memoDate', 'memoImg', 'userId', 'article_id', 'book_id']


