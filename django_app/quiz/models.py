from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_img_src = models.CharField(max_length=100)
    vertical = models.CharField(max_length=500)
    horizontal = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)
    answer_img_src = models.CharField(max_length=100)

    def __str__(self):
        return 'id:' + str(self.id) + ', ' + \
                '             '+ \
                'answer:'+self.answer