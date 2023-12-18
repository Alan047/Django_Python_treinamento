from django.db import models



class Task(models.Model):

	Task = models.CharField(max_length=255)
	Descricao = models.TextField(max_length=255)
	crated_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	