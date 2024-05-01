select pulseprofile.PulseProfileID ,pulseprofile.profileName, address.AddressID, AddressLine1,
state.StateName, pulseprofile.IsClaimedByID, businessModelType.PulseBusinessModelTypeID, businessModelType.BusinessModelDescription,
userLogin.UserLoginID, addressXref.IsDeleted, businessModelXref.IsDeleted
from
PPD_PulseProfile pulseprofile
LEFT JOIN PPD_PulseProfileAddressXref addressXref on pulseprofile.PulseProfileId = addressXref.PulseProfileId
LEFT JOIN PPD_Address address on address.AddressID =addressXref.AddressID
LEFT JOIN Ref_State state on address.stateId = state.stateId
LEFT JOIN Ref_PulseProfileType profileType on pulseprofile.PulseProfileTypeID = profileType.PulseProfileTypeID
LEFT JOIN PPD_PulseProfileBusinessModelTypeXref businessModelXref on businessModelXref.pulseprofileId = pulseprofile.pulseprofileId
LEFT JOIN Ref_PulseBusinessModelType businessModelType on businessModelType.PulseBusinessModelTypeID = businessModelXref.PulseBusinessModelTypeID
 /*one to many business models will be there */
LEFT JOIN PPD_UserLogin userLogin on userLogin.UserLoginID = pulseprofile.IsClaimedByID
/*UserRoleType roleType */
where
/*pulseprofile.PulseProfileID in (1,2,3,4,5,6,7,8,9,10)
AND*/ userLogin.UserLoginID =2
AND pulseprofile.PulseProfileTypeID is null
AND (businessModelXref.IsDeleted is null  or businessModelXref.IsDeleted =0)
AND (addressXref.IsDeleted is null or addressXref.IsDeleted = 0)
