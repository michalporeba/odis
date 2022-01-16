import json
import re


def escape(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        v = func(*args, **kwargs)
        if v is None:
            return None
        return str(v).replace("\\", r"\\").replace("'", r"\'")

    return wrapper


@escape
def get_value(obj: any, key: str) -> str:
    if dict == type(obj):
        if not key in obj.keys():
            return None
        elif str == type(obj[key]):
            return obj[key]
        else:
            return get_value(obj[key], "@value")
    if list == type(obj) and len(obj) > 0:
        return get_value(obj[0], key)
    return None


with open("schema.org.json") as json_file:
    data = json.load(json_file)

data = data["@graph"]
rex = r"(?<!^)(?=[A-Z])"

f = open("../alps/schemaorg.py", "w")

f.write(
    """from .descriptors import Semantic

class SchemaOrg:
"""
)
for d in data:
    name = re.sub(rex, "_", get_value(d, "rdfs:label")).upper()
    if name[0].isdigit():
        name = "A_" + name
    f.write(
        f"""
    {name} = Semantic(
        id = '{get_value(d, 'rdfs:label')}',
        ref = '{get_value(d, '@id')}',
        text = '''{get_value(d, 'rdfs:comment')}'''
    )
    """
    )
f.close()
