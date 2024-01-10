from django.db import models



class Mcq(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, blank=False)
    a = models.CharField(max_length=255, blank=False)
    b = models.CharField(max_length=255, blank=False)
    c = models.CharField(max_length=255, blank=False)
    d = models.CharField(max_length=255, blank=False)
    correct = models.CharField(max_length=1, blank=False)
    positive_marks = models.IntegerField(default=4)
    negative_marks = models.IntegerField(default=-2)

class Custom_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    score = models.IntegerField(default=0)
    current_question = models.ForeignKey(Mcq,default=1, on_delete=models.CASCADE, blank=False, null=True)


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Custom_user, on_delete=models.CASCADE, blank=False)
    question_id = models.ForeignKey(Mcq, on_delete=models.CASCADE, blank=False)
    selected_option = models.CharField(max_length=1, blank=False)
    status = models.CharField(max_length=255, blank=False)

