from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _

# Create your models here.

STATES_CHOICES = [
    ('IN-AP' , 'Andhra Pradesh'),
    ('IN-AR' , 'Arunachal Pradesh'),
    ('IN-AS' , 'Assam'),
    ('IN-BR' , 'Bihar'),
    ('IN-CT' , 'Chhattisgarh'),
    ('IN-GA' , 'Goa'),
    ('IN-GJ' , 'Gujarat'),
    ('IN-HR' , 'Haryana'),
    ('IN-HP' , 'Himachal Pradesh'),
    ('IN-JK' , 'Jammu and Kashmir'),
    ('IN-JH' , 'Jharkhand'),
    ('IN-KA' , 'Karnataka'),
    ('IN-KL' , 'Kerala'),
    ('IN-MP' , 'Madhya Pradesh'),
    ('IN-MH' , 'Maharashtra'),
    ('IN-MN' , 'Manipur'),
    ('IN-ML' , 'Meghalaya'),
    ('IN-MZ' , 'Mizoram'),
    ('IN-NL' , 'Nagaland'),
    ('IN-OR' , 'Odisha'),
    ('IN-PB' , 'Punjab'),
    ('IN-RJ' , 'Rajasthan'),
    ('IN-SK' , 'Sikkim'),
    ('IN-TN' , 'Tamil Nadu'),
    ('IN-TG' , 'Telangana'),
    ('IN-TR' , 'Tripura'),
    ('IN-UT' , 'Uttarakhand'),
    ('IN-UP' , 'Uttar Pradesh'),
    ('IN-WB' , 'West Bengal'),
    ('IN-AN' , 'Andaman and Nicobar Islands'),
    ('IN-CH' , 'Chandigarh'),
    ('IN-DN' , 'Dadra and Nagar Haveli'),
    ('IN-DD' , 'Daman and Diu'),
    ('IN-DL' , 'Delhi'),
    ('IN-LD' , 'Lakshadweep'),
    ('IN-PY' , 'Puducherry'),
]

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, blank= False)
    lastName = models.CharField(max_length=50, blank=False)
    mobileNo = models.DecimalField(
        max_digits=13,
        decimal_places=0,
        blank=False)
    emailID= models.EmailField(blank=False)
    college = models.CharField(max_length=100, blank=False)
    street = models.CharField(max_length=100, blank=False)
    locality = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(
        max_length=5,
        choices= STATES_CHOICES, 
        blank=False)
    pin = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        blank=False)

    def __unicode__(self):
        return 'Participant ' + str(id)

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields= '__all__'
        labels = {
            'firstName': _('First name'),
            'lastName': _('Last name'),
            'mobileNo': _('Mobile Number'),
            'emailID': _('EMail ID'),
            'college': _('College'),
            'street': _('Street'),
            'locality': _('Locality'),
            'city': _('City'),
        }
        widgets = {
            'firstName': TextInput(attrs={'required':'True'}),
            'lastName': TextInput(attrs={'required':'True'}),
            'mobileNo': TextInput(attrs={'required':'True'}),
            'college': TextInput(attrs={'required':'True'}),
            'street': TextInput(attrs={'required':'True'}),
            'locality': TextInput(attrs={'required':'True'}),
            'city': TextInput(attrs={'required':'True'}),
        }