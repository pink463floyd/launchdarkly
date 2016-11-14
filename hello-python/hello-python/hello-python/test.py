import ldclient

if __name__ == "__main__":
  #ldclient.sdk_key = "sdk-b88a713c-f133-44a1-8128-2f6bcafa8b5b"
  ldclient.sdk_key = "sdk-b88a713c-f133-44a1-8128-2f6bcafa8b5b"


user = {
  "key": "bob@example.com",
  "firstName": "Bob",
  "lastName": "Loblaw",
  "custom": {
    "groups": "beta_testers"
  }
}

show_feature = ldclient.get().variation("foobar", user, False)

if show_feature:
  print "Showing your feature"
else:
  print "Not showing your feature"

ldclient.get().flush()
