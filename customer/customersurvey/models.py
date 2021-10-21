from django.db import models
from django.contrib.auth.models import User



class tbl_questions(models.Model):
    question        = models.TextField()
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    # survey_id       = models.CharField(max_length=255)
    date_created    = models.DateTimeField(auto_now_add=True)

class Survey(models.Model):
    survey_id       = models.CharField(max_length=255)
    question        = models.ForeignKey(tbl_questions, on_delete=models.CASCADE)
    user_answer     = models.CharField(max_length=255, null=True, blank=True)
    date_created    = models.DateTimeField(auto_created=True)
    user            = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.question.question