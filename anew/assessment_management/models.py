from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Year choice ranges from 2015 to 2099
YEAR = [(v, v) for k, v in enumerate([i for i in xrange(2015, 3000)])]

MONTH = [(v, (datetime.date(2015, v, 1).strftime('%B'))) for k, v in enumerate([i for i in xrange(1, 13)])]


class Student(models.Model):
    # Extending User Model
    user = models.OneToOneField(User, verbose_name="User")
    reg_no = models.CharField(
        verbose_name="Registration Number",
        max_length=40, blank=False,
        null=False, unique=True)
    college_name = models.CharField(
        verbose_name="College Name",
        max_length=40, blank=True,
        null=True
    )
    age = models.IntegerField(
        "Age",
        blank=True, null=True)
    phone_number = models.CharField(
        "Phone Number",
        max_length=15,
        blank=True, null=True)
    address = models.CharField(
        verbose_name="Address",
        max_length=100, blank=True,
        null=True
    )

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}: {1} {2}'.format(self.reg_no,
                                      self.user.first_name,
                                      self.user.last_name)


class Company(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=40, blank=False,
        null=False)
    location = models.CharField(
        verbose_name="Location",
        max_length=40, blank=True,
        null=True
    )

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        unique_together = ('name', 'location', )
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Timings(models.Model):
    start_time = models.TimeField(verbose_name='Start Time')
    end_time = models.TimeField(verbose_name='End Time')

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0} : {1}'.format(self.start_time, self.end_time)

    class Meta:
        verbose_name = 'Timing'
        verbose_name_plural = 'Timings'


class Batch(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=40, blank=False,
        null=False)
    tutor = models.ForeignKey(User)
    timing = models.ForeignKey(Timings)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'


class TutorBatch(models.Model):
    tutor = models.ForeignKey(User)
    batch = models.ForeignKey(Batch)

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}: {1} {2}'.format(self.batch.name, self.tutor.first_name, self.tutor.last_name)

    class Meta:
        verbose_name = 'Tutor Batch'
        verbose_name_plural = 'Tutor Batches'


class StudentBatch(models.Model):
    student = models.ForeignKey(Student)
    batch = models.ForeignKey(Batch)

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}: {1} {2}'.format(self.batch.name, self.student.user.first_name,
                                      self.student.user.last_name)

    class Meta:
        verbose_name = 'Student Batch'
        verbose_name_plural = 'Student Batches'


class Subject(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=40, blank=False,
        null=False)

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)


class Assessment(models.Model):
    student_batch = models.ForeignKey(StudentBatch)
    subject = models.ForeignKey(Subject)
    year = models.IntegerField(choices=YEAR, default=YEAR[0][0])
    month = models.CharField(choices=MONTH, default=MONTH[0][0],
                             max_length=20)
    theory_mark = models.DecimalField("Theory Mark", validators=[MaxValueValidator(0),
                                                                 MinValueValidator(100)],
                                      decimal_places=2, max_digits=12)
    practical_mark = models.DecimalField("Practical Mark", validators=[MaxValueValidator(0),
                                                                       MinValueValidator(100)],
                                         decimal_places=2, max_digits=12)
    presentation_skills = models.DecimalField("Presentaion Skills", validators=[MaxValueValidator(0),
                                                                                MinValueValidator(100)],
                                              decimal_places=2, max_digits=12)
    punctuality = models.DecimalField("Punctuality", validators=[MaxValueValidator(0),
                                                                 MinValueValidator(100)],
                                      decimal_places=2, max_digits=12)
    attitude = models.DecimalField("Attitude", validators=[MaxValueValidator(0),
                                                           MinValueValidator(100)],
                                   decimal_places=2, max_digits=12)
    class_participation = models.DecimalField("Class Participation", validators=[MaxValueValidator(0),
                                                                                MinValueValidator(100)],
                                              decimal_places=2, max_digits=12)
    commitment = models.DecimalField("Commitment", validators=[MaxValueValidator(0),
                                                               MinValueValidator(100)],
                                     decimal_places=2, max_digits=12)
    english_fluency = models.DecimalField("English Fluency", validators=[MaxValueValidator(0),
                                                                         MinValueValidator(100)],
                                          decimal_places=2, max_digits=12)
    remarks = models.CharField(
        verbose_name="Remarks",
        max_length=40, blank=False,
        null=False)

    # For logs
    createdon = models.DateTimeField(verbose_name="created Date",
                                     auto_now_add=True)
    updatedon = models.DateTimeField(verbose_name="Updated Date",
                                     auto_now=True)

    def __unicode__(self):
        return u'{0}'.format(self.student_batch)