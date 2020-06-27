from django.db import models


class Career(models.Model):
    job_title = models.CharField(
        verbose_name="Job Title",
        max_length=250,
    )

    average_salary = models.DecimalField(max_digits=6, decimal_places=0)

    MINIMUM_AGE = "Minimum Age"
    HIGH_SCHOOL_DIPLOMA = "High School Diploma"
    ASSOCIATES = "Associate's Degree"
    BACHELORS = "Bachelor's Degree"
    MASTERS = "Master's Degree"
    PHD = "PhD"

    DEGREE_CHOICES = [
        (MINIMUM_AGE, "Minimum Age"),
        (HIGH_SCHOOL_DIPLOMA, "High School Diploma"),
        (ASSOCIATES, "Associate's Degree"),
        (BACHELORS, "Bachelor's Degree"),
        (MASTERS, "Master's Degree"),
        (PHD, "PhD"),
    ]

    required_education = models.CharField(
        verbose_name="Required Education",
        max_length=19,
        choices=DEGREE_CHOICES,
        blank=False,
    )
