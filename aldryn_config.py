# -*- coding: utf-8 -*-

from aldryn_client import forms


class Form(forms.BaseForm):
    pagination = forms.NumberField('Work pagination', initial='5')
  
    def to_settings(self, data, settings):
        settings["INSTALLED_APPS"].extend(["djangocms_portfolio"])
        settings["WORK_PAGINATION"] = data['pagination']
        return settings
