import hashlib, json
from myapp.models import Tender


#this function is use for hash data of the user
def hashturnover():
    # For convenience, this is a helper function that wraps our hashing algorithm
    gmodel=Model(Tender)
    turnover1=gmodel.turnover
    msg= turnover1
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!

    return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    print unicode

def hashExperience():
    gmodel = Model(Tender)
    exp = gmodel.experience
    msg = exp
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!

    return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    print unicode