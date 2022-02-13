from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_img_src = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    answer_img_src = models.CharField(max_length=100)

    def __str__(self):
        return 'id:' + str(self.id) + ', ' + \
                '             '+ \
                'answer:'+self.answer

class VerticalKeyword(models.Model):
    quiz_id = models.IntegerField(default=-1)
    keyword = models.CharField(max_length=500)

    def __str__(self):
        return 'quiz_id:' + str(self.quiz_id) + ', ' + \
                '             '+ \
                '縦:'+self.keyword
    
class HorizonalKeyword(models.Model):
    quiz_id = models.IntegerField(default=-1)
    keyword = models.CharField(max_length=500)

    def __str__(self):
        return 'quiz_id:' + str(self.quiz_id) + ', ' + \
                '             '+ \
                '横:'+self.keyword