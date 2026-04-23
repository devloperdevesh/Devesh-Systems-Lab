from app.core.token_bucket import TokenBucket

class RateLimiter:
    def __init__(self):
        self.users = {}

    def allow_request(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = TokenBucket()

        return self.users[user_id].allow_request()