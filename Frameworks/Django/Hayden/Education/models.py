from django.db import models
from django.urls import reverse

from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField


class Institution(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    next_year_full_tuition = models.DecimalField(max_digits=7, decimal_places=2)

    headmaster = models.CharField(max_length=250)
    address = AddressField(on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)

    admissions_director = models.CharField(
        max_length=250,
        blank=True,
    )

    website = models.URLField(blank=True)

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
    )

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

    def __str__(self):
        return self.name

    SIXTH_GRADE = '6th Grade'
    SEVENTH_GRADE = '7th Grade'
    EIGHTH_GRADE = '8th Grade'
    FRESHMAN = 'Freshman'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    GRADUATE = 'Graduate'

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
        max_length=9,
        choices=YEAR_IN_SCHOOL_CHOICES,
        blank=False,
    )

    def is_middleschool(self):
        return self.grade_level in {self.SIXTH_GRADE, self.SEVENTH_GRADE, self.EIGHTH_GRADE}

    def is_upperschool(self):
        return self.grade_level in {self.FRESHMAN, self.SOPHOMORE, self.JUNIOR, self.SENIOR}

    CAPSTONE = 'Capstone'
    FINE_ARTS = 'Fine Arts'
    LANGUAGE_ARTS = 'Language Arts'
    MATHEMATICS = 'Mathematics'
    OUTDOOR_EDUCATION = 'Outdoor Education'
    PHYSICAL_EDUCATION = 'Physical Education'
    SCIENCE = 'Science'
    SOCIAL_STUDIES = 'Social Studies'
    TECHNOLOGY = 'Technology'
    WORLD_LANGUAGES = 'World Languages'

    SUBJECT_CHOICES = [
        (CAPSTONE, 'Capstone'),
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
        max_length=18,
        choices=SUBJECT_CHOICES,
        blank=True,
    )

    AP = 'AP'
    CLEP = 'CLEP'

    EXAM_CHOICES = [
        (AP, 'Advanced Placement'),
        (CLEP, 'College Level Examination Program'),
    ]

    required_exam = models.CharField(
        max_length=4,
        choices=EXAM_CHOICES,
        blank=True,
    )

    registered = models.BooleanField(default=False)

    def is_registered(self):
        if self.registered:
            return self.registered

    def is_college_credit_eligible(self):
        return self.required_exam in {self.AP, self.CLEP}

    class Meta:
        ordering = ['school', 'grade_level', 'subject']
        verbose_name = "Graduation Credit"
        verbose_name_plural = "Graduation Credits"

    def get_absolute_url(self):
        return reverse('credit-detail', kwargs={'pk': self.pk})


class Instructor(models.Model):
    school = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Credit,
        on_delete=models.CASCADE,
        blank=True,
    )

    first_name = models.CharField(
        blank=True,
        max_length=125,
    )

    last_name = models.CharField(
        blank=True,
        max_length=125,
    )

    email_address_of_instructor = models.EmailField(blank=True)
    phone_number_of_instructor = PhoneNumberField(blank=True)

    class Meta:
        verbose_name = "Teaching Instructor"
        verbose_name_plural = "Teaching Instructors"
