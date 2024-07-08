from django.db import models


class Tasks(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=255
    )
    done = models.BooleanField(
        verbose_name="Done",
        null=True,
        blank=True,
        default=False
    )

    def __str__(self) -> str:
        return self.name
