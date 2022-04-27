from fastapi import FastAPI


api = FastAPI(title="Mon API pour la formation intra")


@api.get("/")
def get_index():
    return {
        "hello": "world"
    }


@api.post("/mon_post")
def post_mon_post():
    return {
        "ceci est": "un post"
    }


@api.get("/mon_get")
def get_mon_get():
    return {
        "status": 1
    }


@api.get("/items")
def get_items():
    return {
        "items": []
    }


@api.get("/health")
def get_health():
    return {
        "health": "ok"
    }


@api.get("/user")
def get_user():
    return {
        "name": "paul"
    }
