Running command line `func pack --python --build-native-deps` will build out the packages locally
- Docker should be running locally for this command to work mimicing the same environment in Azure (Python runs only on Linux Function Apps on Azure PaaS)

![image](https://github.com/macavall/PythonFunctionV2Import/assets/43223084/afb78e14-b446-40f1-bd49-47a4a7822c83)

- Running the command `func pack --python --build-native-deps`

![image](https://github.com/macavall/PythonFunctionV2Import/assets/43223084/88d4be0f-50ce-4db8-9e1e-3a29dfd9a620)


- Running the command `func pack --python`

![image](https://github.com/macavall/PythonFunctionV2Import/assets/43223084/c7539084-d40f-4084-98f0-e586172ee8e7)

This creates a **Zip File** in the Python Function App Root Directory

![image](https://github.com/macavall/PythonFunctionV2Import/assets/43223084/c33f2283-ed69-4e42-94e7-766998735d78)

We can then upload this Zip File to the Function App in Azure

``` Python
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
```


