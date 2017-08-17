# -*- coding: utf-8 -*-

from aldryn_client import forms


class Form(forms.BaseForm):
    pagination = forms.NumberField('Work pagination', initial='5')
    work_list_truncwords = forms.NumberField('Work List Truncwords', initial='50')

    def to_settings(self, data, settings):
        settings["INSTALLED_APPS"].extend(["djangocms_portfolio"])
        settings["INSTALLED_APPS"].extend(["taggit"])
        settings["WORK_PAGINATION"] = data['pagination']
        settings["WORK_LIST_TRUNCWORDS_COUNT"] = data['work_list_truncwords']
        return settings
