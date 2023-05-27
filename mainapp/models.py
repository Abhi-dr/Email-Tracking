from django.db import models

class Email(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    opened = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)
    tracking_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Email - Subject: {self.subject}, Recipient: {self.recipient}"
