# coding: utf-8

#Import Models

from djangocms_portfolio.models import Work, CategoryWork
from django import template

register = template.Library()


@register.inclusion_tag('djangocms_portfolio/tags/work_categories_filters.html')
def list_work_categories():
    categories = CategoryWork.objects.all().order_by('title')
    return {'categories': categories}

