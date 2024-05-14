# # logs/models.py
# from django.db import models

# class Log(models.Model):
#     LEVEL_CHOICES = [
#         ('info', 'Info'),
#         ('error', 'Error'),
#         ('success', 'Success')
#     ]
    
#     level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
#     log_string = models.TextField()
#     timestamp = models.DateTimeField()
#     source = models.CharField(max_length=100)

#     def __str__(self):
#         return f'{self.timestamp} - {self.level} - {self.source}'



# logs/models.py

from django.db import models

class Log(models.Model):
    LEVEL_CHOICES = [
        ('info', 'Info'),
        ('error', 'Error'),
        ('success', 'Success'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    log_string = models.TextField()
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.level} - {self.source}"
