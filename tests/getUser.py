from destinypy import user

APIKEY = ""

me = user.GetBungieNetUserById(23895923, APIKEY)

print(me.displayName)