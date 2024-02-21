import azure.functions as func
import datetime
import json
import logging

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

app = func.FunctionApp()

@app.route(route="http1", auth_level=func.AuthLevel.ANONYMOUS)
def http1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            
            
    try:
        # Call some method from your class
        # obj1.some_method()
            # You can use the Google Analytics related imports here
            # For example, you can use BetaAnalyticsDataClient to interact with Google Analytics data
        client = BetaAnalyticsDataClient()
    except Exception as e:
        logging.info("ERROR!!!:")

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )