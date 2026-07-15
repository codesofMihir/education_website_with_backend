from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Courses(models.Model):
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    description=models.TextField(null=True)
    qty=models.IntegerField(default=1)
    product_image=models.ImageField(upload_to='product_images/',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product_name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

class CourseContent(models.Model):
    CONTENT_NOTE = 'note'
    CONTENT_VIDEO = 'video'
    CONTENT_QUIZ = 'quiz'

    CONTENT_TYPE_CHOICES = [
        (CONTENT_NOTE, 'Note'),
        (CONTENT_VIDEO, 'Video'),
        (CONTENT_QUIZ, 'Quiz'),
    ]

    course = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=250)

    # Notes / Video uploads
    note_file = models.FileField(upload_to='course_notes/', blank=True, null=True)
    video_file = models.FileField(upload_to='course_videos/', blank=True, null=True)

    # Quiz fields (simple single-question quiz)
    quiz_question = models.CharField(max_length=500, blank=True, null=True)
    quiz_answer = models.CharField(max_length=500, blank=True, null=True)

    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_id} - {self.title} ({self.content_type})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.submitted_at.strftime('%Y-%m-%d')}"

