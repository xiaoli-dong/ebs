from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    summary = models.TextField(max_length=5000, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="date created")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    
def pre_save_project_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.owner.username + "-" + instance.title)

pre_save.connect(pre_save_project_receiver, sender=Project)


class Sample(models.Model):
    title = models.CharField(max_length=100)
    organism = models.CharField(max_length=100)
    project = models.ForeignKey(
        Project, related_name = 'samples', on_delete=models.CASCADE)
    
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="date created")

    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")
    
    def __str__(self):
        return self.title

class Seq(models.Model):

    strategies = (
        ('WGA', 'WGA'),
        ('WGS', 'WGS'),
    )
    sources = (
        ('genomics', 'genomics'),
        ('metagenomics', 'metagenomics')
    )
    platforms = (
        ('Illumina HiSeq','Illumina HiSeq'),
        ('NextSeq 500', 'NextSeq 500'),
        ('Illumina MiSeq', 'Illumina MiSeq'),
        ('GridION', 'GridION'),
        ('MinION', 'MinION'),

    )
    title = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100, choices=platforms) #illumina MiSeq
    strategy = models.CharField(max_length=100, choices=strategies) # WGS
    source = models.CharField(max_length=100, choices=sources) # metagenomics
    layout = models.CharField(max_length=100) # paired
    created = models.DateTimeField(auto_now_add=True)
    seqfile = models.FileField(upload_to='seqs/', null=True, blank=True)

    #projects = models.ManyToManyField('Project', related_name='seqs', blank=True)
    sample = models.ForeignKey(Sample, related_name='seqs', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title