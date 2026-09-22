from locust import HttpUser, task, constant, between
import random
import logging

logger = logging.getLogger(__name__)

class HelloWorldUser(HttpUser):
    # wait_time = constant(2) # wait 2s for every request

    # @task
    # def hello_world(self):
    #     self.client.get("/api/v1/health")

    @task
    def order_items(self,):
        # random_number = random.randint(2, 10)
        user_id = 11
        payload = {
            "user_id": user_id,
            "products": [
                {
                    "product_id": 3,
                    "quantity": 1
                }
            ]
        }
        logger.info(f"payload: {payload}")
        self.client.post("/api/v1/order", json=payload)

