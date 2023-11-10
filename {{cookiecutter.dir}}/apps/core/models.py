from django.db import models


class BvgelsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tagging(BvgelsModel):
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)


class Comment(BvgelsModel):
    user = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    comment = models.TextField()

    class Meta:
        abstract = True
