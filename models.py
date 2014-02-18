from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

#
# To create a new resource, use these three super-classes. 
#

class NewGenericResource(Page, RichText):
	resource_content = models.FileField(
		upload_to='newgenericresource',
		help_text='this should be a NetCDF file',
	)
	resource_description = models.TextField(null=False, blank=True, default='',
		help_text='this should contain the data description of fields in the netCDF')
	resource_file_count = models.IntegerField(null=False, default=1, 
		help_text='this should contain the number of files in the NetCDF bag')

	class Meta:
		verbose_name = 'New Generic Resource'

