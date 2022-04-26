from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
    pdf = models.FileField(upload_to='reports/pdfs/')
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='reports/covers/', null=True, blank=True)
    isUpdated = models.BooleanField(default=False,)
    isViewed = models.BooleanField(default=False,)
    viewers = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)