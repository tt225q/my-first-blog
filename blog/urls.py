#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 23:38:11 2023

@author: wangchungpin
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
]