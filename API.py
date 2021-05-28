def get_data():
    "Gets api data"
    ship_api_url = "http:"
    request_data = requests.get(ship_api_url)
    return request_data.json()

def convertDataToFood(data):
    "Converts to food through AI prediction"

def format_data(data):
    "Formats the data"
    formatted = """
    """.format(convertDataToFood(data[0],data[1],data[2]))
    return formatted

def put(self,name):
    parser = reqparse.RequestParser()
    parser.add_argument("food")
    parser.add_argument("necessities")
    args = parser.parse_args()

    for user in Users:
        if(name==user["name"]):
            user["food"] = args["food"]
            user["necessities"] = args["necessities"]
            return user

    user = {
        "name": name,
        "food": args["food"],
        "necessities": args["necessities"]
    }
    Users.append(user)
    return user