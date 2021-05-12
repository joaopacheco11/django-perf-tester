from django.db import models
from gettext import gettext as _
import string
import random

size_multiplier = 2048


# Create your models here.

class TestModel1(models.Model):
    ifield1 = models.IntegerField(_('Integer field 1'))
    ifield2 = models.IntegerField(_('Integer field 2'), db_index=True)
    ifield3 = models.IntegerField(_('Integer field 3'), blank = True, null = True)
    bfield4 = models.BooleanField(_('Boolean field 4'))
    bfield5 = models.BooleanField(_('Boolean field 5'), blank = True, null = True)
    tfield6 = models.TextField(_('Text field 6'))
    tfield7 = models.TextField(_('Text field 7'), blank = True, null = True)
    index_field = models.IntegerField(_("Index Field"), default = 0)

def create_random_testmodels(amount=10):
    for i in range(0, amount):
        test_model = TestModel1(
            ifield1 = random.randint(-999999, 99999999),
            ifield2 = random.randint(-999999, 99999999),
            ifield3 = random.randint(-999999, 99999999),
            bfield4 = bool(random.getrandbits(1)),
            bfield5 = bool(random.getrandbits(1)),
            tfield6 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 3*size_multiplier)),
            tfield7 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 4*size_multiplier)),
            index_field = random.randint(0,4)
        )
        test_model.save()