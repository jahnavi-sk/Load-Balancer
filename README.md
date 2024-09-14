# Load-Balancer
Mapper Reducer codes to validate the dataset with the information regarding all the requests made by clients during the day.

### Story
A Company's team was assigned to predict the status codes that clients would receieve while hitting the company's endpoints, while taking into consideration the traffic received on a certain endpoint at a given time, as well as the reliability of the servers handling the requests. You are given a dataset with the information regarding all the requests made by clients during the day. The predicted status codes by the team are also provided. You are to validate the dataset given and evaluate each client's success metric.

### Objective

Direct each incoming request to an available server assigned to the respective endpoint, given that each endpoint has 3 servers which may or may not be down at different timestamps. The goal is to determine the number of successfully predicted requests by the team for each client and calculate each client's total_price, based on the fixed price associated with each endpoint.

#### Points to be considered :

- The requests in the same timestamp must be processed in the lexicographical order.
- A Single client is only allowed to hit one endpoint at a given timestamp. Other requests are not processed and are not taken into consideration for evaluation.
- The time taken to handle a client request by any server is 1 second.

### Metadata for the Dataset:

###### Request ID (rX):

- A unique identifier for each request. This is used to differentiate between different requests in the dataset.

###### Client ID (cX):

- Identifies the client making the request. Each client is associated with a unique ID, which can be used to track the activity or behavior of individual clients.

###### Endpoint (endpoint):

- Represents the specific service or function the request is accessing.

    ```
    user/profile: Access or update user profile information.
    user/settings: Modify user settings, such as privacy or notification preferences.
    order/history: Retrieve the history of past orders.
    order/checkout: Complete the checkout process for an order.
    product/details: View detailed information about a specific product.
    product/search: Search for products based on certain criteria.
    cart/add: Add an item to the shopping cart.
    cart/remove: Remove an item from the shopping cart.
    payment/submit: Submit payment information to complete a purchase.
    support/ticket: Create or view support tickets for customer service.
    ``` 

- Each endpoint is associated with a price, which is used to calculate the total_price for each client. The price for all the endpoints is given below.

        'user/profile': 100
        'user/settings': 200
        'order/history': 300
        'order/checkout': 400
        'product/details': 500
        'product/search': 600
        'cart/add': 700
        'cart/remove': 800
        'payment/submit': 900
        'support/ticket': 1000
###### Timestamp (HH:MM:SS):

- Indicates the time at which the request was made in hours, minutes, and seconds. This can be used for analyzing patterns in request timing or for sequencing events.

###### Downtime (No.of servers):

- Reflects the no.of servers down. A value of 0.0 indicates no servers are down at that second.

###### Predicted Status Code:

- Represents the status codes predicted by the Company's team for each client request. These predictions may or may not be correct.

- 500 - Internal Server Error
- 200 - Successful Request
