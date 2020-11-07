import base64

s = base64.b64decode("eWJyYm5mMTEyMzIz".encode("UTF-8")).decode("UTF-8")

print(s)