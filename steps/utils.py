from time import sleep

from behave import *


@then('wait for {n} seconds')
def step_impl(context, n):
    sleep(int(n))
