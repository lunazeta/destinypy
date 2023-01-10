from destinypy import user
from destinypy import queries
# Clans, etc.

class ClanBanner():

    def __init__(self,
        decalId: int,
        decalColorId: int,
        decalBackgroundColorId: int,
        gonfalonId: int,
        gonfalonColorId: int,
        gonfalonDetailId: int,
        gonfalonDetailColorId: int
    ):
        self.decalId = decalId
        self.decalColorId = decalColorId
        self.decalBackgroundColorId = decalBackgroundColorId
        self.gonfalonId = gonfalonId
        self.gonfalonColorId = gonfalonColorId
        self.gonfalonDetailId = gonfalonDetailId
        self.gonfalonDetailColorId = gonfalonDetailColorId

class ClanInfo():
    
    def __init__(self,
        clanCallsign: str,
        clanBannerData: ClanBanner
    ):
        self.clanCallsign = clanCallsign
        self.clanBannerData = clanBannerData

class ClanInfoAndInvestment():

    def __init__(self,
        d2ClanProgressions, #TODO
        clanCallsign: str,
        clanBannerData: ClanBanner
    ):
        self.d2ClanProgressions = d2ClanProgressions
        self.clanCallsign = clanCallsign
        self.clanBannerData = clanBannerData



# https://bungie-net.github.io/multi/schema_GroupsV2-GroupFeatures.html#schema_GroupsV2-GroupFeatures
class GroupFeatures():

    def __init__(self,
        maximumMembers: int,
        maximumMembershipsOfGroupType: int,
        capabilities: int,
        membershipTypes: list[int],
        invitePermissionOverride: bool,
        updateCulturePermissionOverride: bool,
        hostGuidedGamePermissionOverride: int,
        updateBannerPermissionOverride: bool,
        joinLevel: int
    ):
        self.maximumMembers = maximumMembers
        self.maximumMembershipsOfGroupType = maximumMembershipsOfGroupType
        self.capabilities = capabilities
        self.membershipTypes = membershipTypes
        self.invitePermissionOverride = invitePermissionOverride
        self.updateCulturePermissionOverride = updateCulturePermissionOverride
        self.hostGuidedGamePermissionOverride = hostGuidedGamePermissionOverride
        self.updateBannerPermissionOverride = updateBannerPermissionOverride
        self.joinLevel = joinLevel

class GroupV2():

    def __init__(self,
        groupId: int,
        name: str,
        groupType: int,
        membershipIdCreated: int,
        creationDate: str,
        modificationDate: str,
        about: str,
        tags: list[str],
        memberCount: int,
        isPublic: bool,
        isPublicTopicAdminOnly: bool,
        motto: str,
        allowChat: bool,
        isDefaultPostPublic: bool,
        chatSecurity: int,
        locale: str,
        avatarImageIndex: int,
        homepage: int,
        membershipOption: int,
        defaultPublicity: int,
        theme: str,
        bannerPath: str,
        avatarPath: str,
        conversationId: int,
        enableInvitationMessagingForAdmins: bool,
        banExpireDate: str | None,
        features: GroupFeatures,
        clanInfo: ClanInfoAndInvestment
    ):
        self.groupId = groupId
        self.name = name
        self.groupType = groupType
        self.membershipIdCreated = membershipIdCreated
        self.creationDate = creationDate
        self.modificationDate = modificationDate
        self.about = about
        self.tags = tags
        self.memberCount = memberCount
        self.isPublic = isPublic
        self.isPublicTopicAdminOnly = isPublicTopicAdminOnly
        self.motto = motto
        self.allowChat = allowChat
        self.isDefaultPostPublic = isDefaultPostPublic
        self.chatSecurity = chatSecurity
        self.locale = locale
        self.avatarImageIndex = avatarImageIndex
        self.homepage = homepage
        self.membershipOption = membershipOption
        self.defaultPublicity = defaultPublicity
        self.theme = theme
        self.bannerPath = bannerPath
        self.avatarPath = avatarPath
        self.conversationId = conversationId
        self.enableInvitationMessagingForAdmins = enableInvitationMessagingForAdmins
        self.banExpireDate = banExpireDate
        self.features = features
        self.clanInfo = clanInfo

class GroupUserInfoCard():

    def __init__(self,
        LastSeenDisplayName: str,
        LastSeenDisplayNameType: int,
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
        self.LastSeenDisplayName = LastSeenDisplayName
        self.LastSeenDisplayNameType = LastSeenDisplayNameType
        self.supplementalDisplayName = supplementalDisplayName
        self.iconPath = iconPath
        self.crossSaveOverride = crossSaveOverride
        self.applicableMembershipTypes = applicableMembershipTypes
        self.isPublic = isPublic
        self.membershipType = membershipType
        self.membershipId = membershipId
        self.displayName= displayName
        self.bungieGlobalDisplayName = bungieGlobalDisplayName
        self.bungieGlobalDisplayNameCode = bungieGlobalDisplayNameCode

class GroupUserBase():

    def __init__(self,
        groupId: int,
        destinyUserInfo: GroupUserInfoCard,
        bungieNetUserInfo: user.UserInfoCard,
        joinDate: str
    ):
        self.groupId = groupId
        self.destinyUserInfo = destinyUserInfo
        self.bungieNetUserInfo = bungieNetUserInfo
        self.joinDate = joinDate

class GroupMember():

    def __init__(self,
        memberType: int,
        isOnline: bool,
        lastOnlineStatusChange: int,
        groupId: int,
        destinyUserInfo: GroupUserInfoCard,
        bungieNetUserInfo: user.UserInfoCard,
        joinDate: str
    ):
        self.memberType = memberType
        self.isOnline = isOnline
        self.lastOnlineStatusChange = lastOnlineStatusChange
        self.groupId = groupId
        self.destinyUserInfo = destinyUserInfo
        self.bungieNetUserInfo = bungieNetUserInfo
        self.joinDate = joinDate

class GroupPotentialMember():

    def __init__(self,
        potentialStatus: int,
        groupId: int,
        destinyUserInfo: GroupUserInfoCard,
        bungieNetUserInfo: user.UserInfoCard,
        joinDate: str
    ):
        self.potentialStatus = potentialStatus
        self.groupId = groupId
        self.destinyUserInfo = destinyUserInfo
        self.bungieNetUserInfo = bungieNetUserInfo
        self.joinDate = joinDate

class GroupV2Card():

    def __init__(self,
        groupId: int,
        name: str,
        groupType: int,
        creationDate: str,
        about: str,
        motto: str,
        memberCount: int,
        locale: str,
        membershipOption: int,
        capabilities: int,
        clanInfo: ClanInfo,
        avatarPath: str,
        theme: str
    ):
        self.groupId = groupId
        self.name = name
        self.groupType = groupType
        self.creationDate = creationDate
        self.about = about
        self.motto = motto
        self.memberCount = memberCount
        self.locale = locale
        self.membershipOption = membershipOption
        self.capabilities = capabilities
        self.clanInfo = clanInfo
        self.avatarPath = avatarPath
        self.theme = theme

# https://bungie-net.github.io/multi/schema_GroupsV2-GroupSearchResponse.html#schema_GroupsV2-GroupSearchResponse
class GroupSearchResponse():

    def __init__(self,
        results: list[GroupV2Card],
        totalResults: int,
        hasMore: bool,
        query: queries.PagedQuery,
        replacementContinuationToken: str,
        useTotalResults: bool # See bungie documentation
    ):
        self.results = results
        self.totalResults = totalResults
        self.hasMore = hasMore
        self.query = query
        self.replacementContinuationToken = replacementContinuationToken
        self.useTotalResults = useTotalResults