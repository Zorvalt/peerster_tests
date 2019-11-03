import time

from behave import *


@given('wait for {n} seconds')
def step_impl(context, n):
    time.sleep(float(n))


@when('wait for {n} seconds')
def step_impl(context, n):
    time.sleep(float(n))

