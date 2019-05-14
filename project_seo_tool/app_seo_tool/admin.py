
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from app_seo_tool import models as app_seo_models


# Register your models here.
admin.site.register(app_seo_models.Engine)

admin.site.register(app_seo_models.Result)

admin.site.register(app_seo_models.Search)
