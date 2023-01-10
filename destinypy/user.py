from destinypy.requester import GET, POST

# Everything to do with bungie.net users

APIKEY = None

class UserMembership():

    def __init__(self,
        membershipType: int, 
        membershipId: int, 
        displayName: str, 
        bungieGlobalDisplayName: str, 
        bungieGlobalDisplayNameCode: int | None
    ):
        self.membershipType = membershipType
        self.membershipId = membershipId
        self.displayName = displayName
        self.bungieGlobalDisplayName = bungieGlobalDisplayName
        self.bungieGlobalDisplayNameCode = bungieGlobalDisplayNameCode

class CrossSaveUserMembership(UserMembership):

    def __init__(self,
        crossSaveOverride: int,
        applicableMembershipTypes: list[int],
        isPublic: bool,
        membershipType: int, 
        membershipId: int, 
        displayName: str, 
        bungieGlobalDisplayName: str, 
        bungieGlobalDisplayNameCode: int | None
    ):
        super().__init__(self, membershipType, membershipId, displayName, bungieGlobalDisplayName, bungieGlobalDisplayNameCode)
        self.crossSaveOverride = crossSaveOverride
        self.applicableMembershipTypes = applicableMembershipTypes
        self.isPublic = isPublic

class UserInfoCard(CrossSaveUserMembership):

    def __init__(self,
        supplementalDisplayName: str,
        iconPath: str,
        crossSaveOverride: int,
        applicableMembershipTypes: list[int],
        isPublic: bool,
        membershipType: int,
        membershipId: int,
        displayName: str,
        bungieGlobalDisplayName: str,
        bungieGlobalDisplayNameCode: int | None
    ):
        super().__init__(self, crossSaveOverride, applicableMembershipTypes, isPublic, membershipType, membershipId, displayName, bungieGlobalDisplayName, bungieGlobalDisplayNameCode)
        self.supplementalDisplayName = supplementalDisplayName
        self.iconPath = iconPath

class UserToUserContext():

    def __init__(self,
        isFollowing: bool,
        ignoreStatus, #TODO
        globalIgnoreEndDate: int | None
    ):
        self.isFollowing = isFollowing
        self.ignoreStatus = ignoreStatus
        self.globalIgnoreEndDate = globalIgnoreEndDate

class GeneralUser():
    @staticmethod
    def createFromJson(generalUserJson: dict):
        parameters = [
            "membershipId",
            "uniqueName",
            "normalizedName",
            "displayName",
            "profilePicture",
            "profileTheme",
            "userTitle",
            "successMessageFlags",
            "isDeleted",
            "about",
            "firstAccess",
            "lastUpdate",
            "legacyPortalUID",
            "context",
            "psnDisplayName",
            "xboxDisplayName",
            "fbDisplayName",
            "showActivity",
            "locale",
            "localeInheritDefault",
            "lastBanReportId",
            "showGroupMessaging",
            "profilePicturePath",
            "profilePictureWidePath",
            "profileThemeName",
            "userTitleDisplay",
            "statusText",
            "statusDate",
            "profileBanExpire",
            "blizzardDisplayName",
            "steamDisplayName",
            "stadiaDisplayName",
            "twitchDisplayName",
            "cachedBungieGlobalDisplayName",
            "cachedBungieGlobalDisplayNameCode",
            "egsDisplayName"]
        for i in parameters:
            if i not in generalUserJson:
                generalUserJson[i] = None
        return GeneralUser(*[generalUserJson[i] for i in parameters])

    def __init__(self,
        membershipId: int,
        uniqueName: str,
        normalizedName: str,
        displayName: str,
        profilePicture: int,
        profileTheme: int,
        userTitle: int,
        successMessageFlags: int,
        isDeleted: bool,
        about: str,
        firstAccess: str | None,
        lastUpdate: str | None,
        legacyPortalUID: int | None,
        context: UserToUserContext,
        psnDisplayName: str,
        xboxDisplayName: str,
        fbDisplayName: str,
        showActivity: bool | None,
        locale: str,
        localeInheritDefault: bool,
        lastBanReportId: int | None,
        showGroupMessaging: bool,
        profilePicturePath: str,
        profilePictureWidePath: str,
        profileThemeName: str,
        userTitleDisplay: str,
        statusText: str,
        statusDate: str,
        profileBanExpire: str | None,
        blizzardDisplayName: str,
        steamDisplayName: str,
        stadiaDisplayName: str,
        twitchDisplayName: str,
        cachedBungieGlobalDisplayName: str,
        cachedBungieGlobalDisplayNameCode: str | None,
        egsDisplayName: str
    ):
        self.membershipId = membershipId
        self.uniqueName = uniqueName
        self.normalizedName = normalizedName
        self.displayName = displayName
        self.profilePicture = profilePicture
        self.profileTheme = profileTheme
        self.userTitle = userTitle
        self.successMessageFlags = successMessageFlags
        self.isDeleted = isDeleted
        self.about = about
        self.firstAccess = firstAccess
        self.lastUpdate = lastUpdate
        self.legacyPortalUID = legacyPortalUID
        self.context = context
        self.psnDisplayName = psnDisplayName
        self.xboxDisplayName = xboxDisplayName
        self.fbDisplayName = fbDisplayName
        self.showActivity = showActivity
        self.locale = locale
        self.localeInheritDefault = localeInheritDefault
        self.lastBanReportID = lastBanReportId
        self.showGroupMessaging = showGroupMessaging
        self.profilePicturePath = profilePicturePath
        self.profilePictureWidePath = profilePictureWidePath
        self.profileThemeName = profileThemeName
        self.userTitleDisplay = userTitleDisplay
        self.statusText = statusText
        self.statusDate = statusDate
        self.profileBanExpire = profileBanExpire
        self.blizzardDisplayName = blizzardDisplayName
        self.steamDisplayName = steamDisplayName
        self.stadiaDisplayName = stadiaDisplayName
        self.twitchDisplayName = twitchDisplayName
        self.cachedBungieGlobalDisplayName = cachedBungieGlobalDisplayName
        self.cachedBungieGlobalDisplayNameCode = cachedBungieGlobalDisplayNameCode
        self.egsDisplayName = egsDisplayName

class GetCredentialTypesForAccountResponse():

    def __init__(self,
        credentialType: bytes,
        credentialDisplayName: str,
        isPublic: bool,
        credentialAsString: str
    ):
        self.credentialType = credentialType
        self.credentialDisplayName = credentialDisplayName
        self.isPublic = isPublic
        self.credentialAsString = credentialAsString

class UserMembershipData():

    @staticmethod
    def createFromJson(userMembershipJson: dict):
        if "primaryMembershipId" not in userMembershipJson:
            userMembershipJson["primaryMembershipId"] = None

        return UserMembershipData("TODO", userMembershipJson["primaryMembershipId"], GeneralUser.createFromJson(userMembershipJson["bungieNetUser"])) #TODO
        

    def __init__(self,
        destinyMemberships, #TODO
        primaryMembershipId: int | None,
        bungieNetUser: GeneralUser
    ):
        self.destinyMemberships = destinyMemberships
        self.primaryMembershipId = primaryMembershipId
        self.bungieNetUser = bungieNetUser

class HardLinkedUserMembership():
    
    @staticmethod
    def createFromJson(hluMembershipJson: dict):
        parameters = [
            "membershipType",
            "membershipId",
            "CrossSaveOverriddenType",
            "CrossSaveOverriddenMembershipId"
        ]
        for i in parameters:
            if i not in hluMembershipJson:
                hluMembershipJson[i] = None
        return HardLinkedUserMembership(*[hluMembershipJson[i] for i in parameters])

    def __init__(self,
        membershipType: int,
        membershipId: int,
        CrossSaveOverriddenType: int,
        CrossSaveOverriddenMembershipId: int | None
    ):
        self.membershipType = membershipType
        self.membershipId = membershipId
        self.CrossSaveOverriddenType = CrossSaveOverriddenType
        self.CrossSaveOverriddenMembershipId = CrossSaveOverriddenMembershipId

class UserSearchResponseDetail():

    def __init__(self,
        bungieGlobalDisplayName: str,
        bungieGlobalDisplayNameCode: int | None,
        bungieNetMembershipId: int | None,
        destinyMemberships: list[UserInfoCard]
    ):
        self.bungieGlobalDisplayName = bungieGlobalDisplayName
        self.bungieGlobalDisplayNameCode = bungieGlobalDisplayNameCode
        self.bungieNetMembershipId = bungieNetMembershipId
        self.destinyMemberships = destinyMemberships

class UserSearchResponse():

    @staticmethod
    def createFromJson(userSearchResponseJson: dict):
        parameters = [
            "searchResults",
            "page",
            "hasMore"
        ]
        for i in parameters:
            if i not in userSearchResponseJson:
                userSearchResponseJson[i] = None
        return UserSearchResponse(*[userSearchResponseJson[i] for i in parameters])

    def __init__(self,
        searchResults: list[UserSearchResponseDetail],
        page: int,
        hasMore: int
    ):
        self.searchResults = searchResults
        self.page = page
        self.hasMore = hasMore

class UserSearchPrefixRequest():

    def __init__(self,
        displayNamePrefix: str
    ):
        self.displayNamePrefix = displayNamePrefix

class EmailSettingSubscriptionLocalization():

    def __init__(self,
        unknownUserDescription: str,
        registeredUserDescription: str,
        unregisteredUserDescription: str,
        unknownUserActionText: str,
        knownUserActionText: str,
        title: str,
        description: str
    ):
        self.unknownUserDescription = unknownUserDescription
        self.registeredUserDescription = registeredUserDescription
        self.unregisteredUserDescription = unregisteredUserDescription
        self.unknownUserActionText = unknownUserActionText
        self.knownUserActionText = knownUserActionText
        self.title = title
        self.description = description

class EmailSettingLocalization():
    
    def __init__(self,
        title: str,
        description: str
    ):
        self.title = title
        self.description = description

class EmailSubscriptionDefinition():

    def __init__(self,
        name: str,
        localization: dict[str, EmailSettingSubscriptionLocalization],
        value: int
    ):
        self.name = name
        self.localization = localization
        self.value = value

class EmailViewDefinitionSetting():

    def __init__(self,
        name: str,
        localization: dict[str, EmailSettingLocalization],
        setByDefault: bool,
        optionAggregateValue: int,
        subscriptions: list[EmailSubscriptionDefinition]
    ):
        self.name = name
        self.localization = localization
        self.setByDefault = setByDefault
        self.optionAggregateValue = optionAggregateValue
        self.subscriptions = subscriptions

class EmailViewDefinition():

    def __init__(self,
        name: str,
        viewSettings: list[EmailViewDefinitionSetting]
    ):
        self.name = name
        self.viewSettings = viewSettings

class EmailOptInDefinition():

    def __init__(self,
        name: str,
        value: int,
        setByDefault: bool,
        dependentSubscriptions: list[EmailSubscriptionDefinition]
    ):
        self.name = name
        self.value = value
        self.setByDefault = setByDefault
        self.dependentSubscriptions = dependentSubscriptions

class EmailSettings():

    def __init__(self,
        optInDefinitions: dict[str, EmailOptInDefinition],
        subscriptionDefinitions: dict[str, EmailSubscriptionDefinition],
        views: dict[str, EmailViewDefinition]
    ):
        self.optInDefinitions = optInDefinitions
        self.subscriptionDefinitions = subscriptionDefinitions
        self.views = views

class PlatformDisplayNames():

    @staticmethod
    def createFromJson(platformNamesJson: dict):
        parameters = [i for i in range(1,7)]
        for i in parameters:
            if i not in platformNamesJson:
                platformNamesJson[i] = None
        return PlatformDisplayNames(*[platformNamesJson[i] for i in range(1,7)])

    def __init__(self, 
        xboxName: str| None,
        psnName: str | None,
        steamName: str | None,
        blizzardName: str | None,
        stadiaName: str | None,
        egsName: str | None
    ):
        self.xboxName = xboxName
        self.psnName = psnName
        self.steamName = steamName
        self.blizzardName = blizzardName
        self.stadiaName = stadiaName
        self.egsName = egsName

def GetBungieNetUserById(membershipId: str, apiKey: str) -> GeneralUser:
    response = GET(f"https://www.bungie.net/Platform/User/GetBungieNetUserById/{membershipId}/", headers={"X-API-Key": apiKey})
    generalUserJson = response["Response"]
    return GeneralUser.createFromJson(generalUserJson)

def GetSanitizedPlatformDisplayNames(membershipId: str, apiKey: str) -> PlatformDisplayNames:
    response = GET(f"https://www.bungie.net/Platform/User/GetSanitizedPlatformDisplayNames/{membershipId}/", headers={"X-API-Key": apiKey})
    platformNamesJson = response["Response"]
    return PlatformDisplayNames.createFromJson(platformNamesJson)

# Identical to Bungie's GetCredentialTypesForTargetAccount
# Integers returned correspond to the membership type (see https://bungie-net.github.io/multi/schema_BungieCredentialType.html#schema_BungieCredentialType)
def GetMembershipTypes(membershipId: str, apiKey: str) -> list[int]:
    response = GET(f"https://www.bungie.net/Platform/User/GetCredentialTypesForTargetAccount/{membershipId}/", headers={"X-API-Key": apiKey})
    return [i["credentialType"] for i in response["Response"]]

def GetMembershipDataById(membershipId: str, membershipType: str, apiKey: str) -> UserMembershipData:
    response = GET(f"https://www.bungie.net/Platform/User/GetMembershipsById/{membershipId}/{membershipType}/", headers={"X-API-Key": apiKey})
    userMembershipJson = response["Response"]
    return UserMembershipData.createFromJson(userMembershipJson)

# This is OAuth TODO
def GetMembershipDataForCurrentUser():
    pass

# Bungie API only supports Steam ids for this
def GetUserFromSteamId(steamId: str, apiKey: str) -> HardLinkedUserMembership:
    response = GET(f"https://www.bungie.net/Platform/User/GetMembershipFromHardLinkedCredential/12/{steamId}/", headers={"X-API-Key": apiKey})
    hluMembershipJson = response["Response"]
    return HardLinkedUserMembership.createFromJson(hluMembershipJson)

def SearchByGlobalName(page: int | str, displayNamePrefix: str, apiKey: str):
    response = POST(f"https://www.bungie.net/Platform/User/Search/GlobalName/{page}/", data={"displayNamePrefix": displayNamePrefix}, headers={"X-API-Key": apiKey})
    userSearchResponseJson = response["Response"]
    return UserSearchResponse.createFromJson(userSearchResponseJson)