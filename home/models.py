from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
MALE = "MALE"
FEMALE = "FEMALE"

GENDER = (
    (MALE, MALE),
    (FEMALE, FEMALE)
)

class User(AbstractUser):
    is_voter = models.BooleanField(default=True)
    is_candidate = models.BooleanField(default=False)
    gender = models.CharField(max_length=10,choices=GENDER, blank=False, null=False)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username

class PollEvent(models.Model):
    poll_name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.poll_name
    
class Position(models.Model):
    event = models.ForeignKey(PollEvent, on_delete=models.CASCADE, related_name="poll_positions")
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    num_candidate = models.IntegerField(default=1) # Number of candidates to be selected
    candidates = models.ManyToManyField(User, through="Candidate")

    def __str__(self):
        return self.title
    
class Candidate(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="candidacy")
    photo = models.ImageField(upload_to='candidates',blank=True,null=True)
    votes = models.ManyToManyField(User, through="Tally")

    def __str__(self):
        return "{}".format(self.candidate)

    def getNumVotes(self):
        return self.votes.count()
    
class Tally(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_votes")
    date_vote = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.candidate)