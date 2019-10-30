import time

from behave import *


@then('wait for {n} seconds')
def step_impl(context, n):
    time.sleep(float(n))
