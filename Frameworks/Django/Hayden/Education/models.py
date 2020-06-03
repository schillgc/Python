from django.db import models
from django.urls import reverse

from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField


class Institution(models.Model):
    name = models.CharField(max_length=250)
    next_year_full_tuition = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return "$" + str(self.next_year_full_tuition)

    headmaster = models.CharField(max_length=250)
    address = AddressField(on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    # def __init__(self):
    #     PHONENUMBER_DB_FORMAT = 'RFC3966'

    fax_number = PhoneNumberField(blank=True)

    admissions_director = models.CharField(
        max_length=250,
        blank=True,
    )

    application_received = models.BooleanField(default=False)
    application_submitted = models.BooleanField(default=False)

    toured = models.BooleanField(default=False)

    teacher_recommendations_requested = models.BooleanField(default=False)
    teacher_recommendations_submitted = models.BooleanField(default=False)

    accepted = models.BooleanField(default=False)

    financial_aid_requested = models.BooleanField(default=False)
    financial_aid_awarded = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
    )

    def __str__(self):
        return "$" + str(self.financial_aid_awarded)

    description = models.TextField(
        max_length=10000,
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = "Educational Institution"
        verbose_name_plural = "Educational Institutions"

    def get_absolute_url(self):
        return reverse('institution-detail', kwargs={'pk': self.pk})


class Credit(models.Model):
    school = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        blank=True,
    )

    name = models.CharField(max_length=100)

    SIXTH_GRADE = '6G'
    SEVENTH_GRADE = '7G'
    EIGHTH_GRADE = '8G'
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'

    YEAR_IN_SCHOOL_CHOICES = [
        (SIXTH_GRADE, '6th Grade'),
        (SEVENTH_GRADE, '7th Grade'),
        (EIGHTH_GRADE, '8th Grade'),
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate School'),
    ]

    grade_level = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        blank=False,
    )

    def is_middleschool(self):
        return self.grade_level in {self.SIXTH_GRADE, self.SEVENTH_GRADE, self.EIGHTH_GRADE}

    def is_upperschool(self):
        return self.grade_level in {self.FRESHMAN, self.SOPHOMORE, self.JUNIOR, self.SENIOR}

    EXTRACURRICULAR = 'ECA.'
    FINE_ARTS = 'FART'
    LANGUAGE_ARTS = 'L.A.'
    MATHEMATICS = 'MATH'
    OUTDOOR_EDUCATION = 'O.E.'
    PHYSICAL_EDUCATION = 'P.E.'
    SCIENCE = 'SCI.'
    SOCIAL_STUDIES = 'S.S.'
    TECHNOLOGY = 'TECH'
    WORLD_LANGUAGES = 'W.L.'

    SUBJECT_CHOICES = [
        (EXTRACURRICULAR, 'Extracurricular Activity'),
        (FINE_ARTS, 'Fine Arts'),
        (LANGUAGE_ARTS, 'Language Arts'),
        (MATHEMATICS, 'Mathematics'),
        (OUTDOOR_EDUCATION, 'Outdoor Education'),
        (PHYSICAL_EDUCATION, 'Physical Education'),
        (SCIENCE, 'Science'),
        (SOCIAL_STUDIES, 'Social Studies'),
        (TECHNOLOGY, 'Technology'),
        (WORLD_LANGUAGES, 'World Languages'),
    ]

    subject = models.CharField(
        max_length=4,
        choices=SUBJECT_CHOICES,
        blank=True,
    )

    AP = 'AP'
    CLEP = 'CL'
    COLLEGE = 'CO'

    EXAM_CHOICES = [
        (AP, 'Advanced Placement'),
        (CLEP, 'College Level Examination Program'),
        (COLLEGE, 'Taken @ College')
    ]

    required_exam = models.CharField(
        max_length=2,
        choices=EXAM_CHOICES,
        blank=True,
    )

    def is_college_credit_eligible(self):
        return self.required_exam in {self.AP, self.CLEP, self.COLLEGE}

    class Meta:
        verbose_name = "Graduation Credit"
        verbose_name_plural = "Graduation Credits"

    def get_absolute_url(self):
        return reverse('credit-detail', kwargs={'pk': self.pk})
