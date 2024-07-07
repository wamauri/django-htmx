from django.db import models


class Tasks(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=255
    )

    def __str__(self) -> str:
        return self.name
