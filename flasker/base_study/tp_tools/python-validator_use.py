#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : python-validator_use.py
# @Author: QUANLI
# @Date  : 2018/8/2 10:30
# @Desc  : python-validator 使用测试
import os, django

from validator import Validator, StringField, EnumField

class UserInfoValidator(Validator):
    user_name = StringField(min_length=5, max_length=18, required=True)
    pass_word = StringField(min_length=5, max_length=18, required=True, validators='[0-9A-Za-z]')
    gender = EnumField(choices=['Male', 'Female'], default='Male')


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flasker.settings')
    django.setup()
    print("====================== Validator start ======================")
    is_valid = False
    while not is_valid:
        register_name = input(" Please enter you name: ")
        register_pass = input(" Please enter you password: ")
        register_gender = input(" Please enter you gender: ")

        user_data = {
            'user_name': register_name,
            'pass_word': register_pass,
            'gender': register_gender
        }

        validator_result = UserInfoValidator(user_data)
        print(validator_result)
    print("====================== Validator end ======================")