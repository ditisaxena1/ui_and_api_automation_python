import requests
from behave import step
import json


@step("Send the get request")
def step_impl(context):
    context.response = requests.get(context.api_url)


@step("Verify that status code is {status_code}")
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)


@step("Verify that the response contains {no_of_bpi} BPIs: USD, GBP, EUR")
def step_impl(context, no_of_bpi):
    data = json.loads(context.response.text)
    bpi = data.get("bpi", {})

    if len(bpi) == int(no_of_bpi) and all(currency in bpi for currency in ["USD", "GBP", "EUR"]):
        assert True
    else:
        assert False


@step("Verify that the GBP description' is '{text}'")
def step_impl(context, text):
    data = json.loads(context.response.text)
    bpi = data.get("bpi", {})
    actual_text = bpi["GBP"]["description"]

    assert actual_text == text




