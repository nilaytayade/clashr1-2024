from typing import Any
from django.db import models



class Mcq(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=255, blank=False)
    a = models.CharField(max_length=255, blank=False)
    b = models.CharField(max_length=255, blank=False)
    c = models.CharField(max_length=255, blank=False)
    d = models.CharField(max_length=255, blank=False)
    correct = models.CharField(max_length=1, blank=False)
    def __str__(self):
        return str(self.question_id)
    

class Custom_user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    score = models.IntegerField(default=0)
    current_question = models.ForeignKey(Mcq,default=1, on_delete=models.CASCADE, blank=False, null=True)
    previous_question = models.BooleanField(default=True,blank=False)
    def __str__(self):
        return str(self.user_id)+"👉"+str(self.current_question)+"🌟"+str(self.score)


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Custom_user, on_delete=models.CASCADE, blank=False)
    question_id = models.ForeignKey(Mcq, on_delete=models.CASCADE, blank=False)
    selected_option = models.CharField(max_length=1, blank=False)
    status = models.BooleanField(blank=False,default=False)

    def __str__(self):
        return str(self.user_id)+"👉"+str(self.question_id)+"👉"+str(self.selected_option)+"👉"+str(self.status)
