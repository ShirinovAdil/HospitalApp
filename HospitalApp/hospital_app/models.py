from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re
# Create your models here.


def number_validate(number):
    pattern = re.compile("^[+]{1}[0-9]+$")
    if not pattern.match(number):
        raise ValidationError(
            '%(number)s is not a phone number format',
            params={'number': number},
        )


HOSPITAL_CHOICES = [
    (1, "22ci əsr stomatoloji klinika(Sumqayıt şəhəri)"),
    (2, "32 Gözəl stomatoloji klinika"),
    (3, "AYAN - N"),
    (4, "Atlas Medical Center Assmed(Lökbatan qəsəbəsi)"),
    (5, "Astoriya Tibb Mərkəzi"),
    (6, "Avrasiya Hospital"),
    (7, "Azərbaycan Tibb Universitetinin Tədris Terapevtik Klinikas"),
    (8, "Azərbaycan Tibb Universitetinin Tədris Cərrahiyyə Klinikası"),
    (9, "Azərbaycan Respublikası Dövlət Təhlükəsizliyi XidmətininHərbi - Tibbİdarəsi"),
    (10, "Bioloji Təbabət MMC(Göyçay şəhəri)"),
    (11, "Caspian İnternational Hospital"),
    (12, "Celamig City hospital"),
    (13, "Blossomvale Medical Center"),
    (14, "West Valley Hospital"),
    (15, "Progress General Hospital"),
    (16, "White Blossom Medical Clinic"),
    (17, "Ruby Valley Community Hospital"),
    (18, "Lakewood Hospital"),
    (19, "Heartland General Hospital"),
    (20, "Heartstone General Hospital")
]


class Hospital(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=150, blank=False)
    contact = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    text = models.TextField(blank=True)
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.hospital.name


class Speciality(models.Model):
    name = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=150, blank=False)
    surname = models.CharField(max_length=150, blank=False)
    birthdate = models.DateTimeField(blank=False)
    phone = models.CharField(
        max_length=13,
        blank=False,
        validators=[MinLengthValidator(13), number_validate],
        help_text="Number in +994 format"
    )
    email = models.EmailField(blank=False)
    registration_date = models.DateTimeField(
        verbose_name="Registration date to the doctor",
        blank=False,
        help_text="You will be contacted for the exact time"
    )
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(to=Speciality, on_delete=models.CASCADE)
    complaint = models.TextField(verbose_name="Complaint/Comment", blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} -> {self.hospital}"


class Contact(models.Model):
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=350)

    def __str__(self):
        return f"{self.email} ->> {self.subject}"
