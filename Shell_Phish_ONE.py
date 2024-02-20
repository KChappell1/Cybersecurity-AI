url = input("Enter a url: ")
print (url)

NumDots = 0
for i in url: 
    if i == ".":
        NumDots += 1
print ( NumDots )



# SubdomainLevel 
# PathLevel



UrlLength = 0
for i in url: 
    UrlLength += 1
print ( UrlLength )

NumDash = 0
for i in url: 
    if i == "-":
        NumDash += 1
print ( NumDash )



# NumDashInHostname = 



AtSymbol = 0 
for i in url: 
    if i == "@":
        AtSymbol += 1
print ( AtSymbol )

TildeSymbol = 0
for i in url: 
    if i == "~":
        TildeSymbol += 1
print ( TildeSymbol )

NumUnderscore = 0
for i in url: 
    if i == "_":
        NumUnderscore +=1
print ( NumUnderscore )

NumPercent = 0 
for i in url: 
    if i == "%":
        NumPercent +=1
print ( NumPercent )

# NumQueryComponents

NumAmpersand = 0
for i in url: 
    if i == "&": 
        NumAmpersand +=1
print (NumAmpersand)

NumHash = 0 
for i in url: 
    if i == "#": 
        NumHash +=1
print ( NumHash )

NumNumericChars = 0 
for i in url: 
    if i in "1234567890": 
        NumNumericChars +=1
print ( NumNumericChars ) 

# NoHttps = 
# RandomString 
# IpAddress
# DomainInSubdomains
# DomainInPaths
# HttpsInHostname
# HostnameLength,
# PathLength
# QueryLength
# DoubleSlashInPath
# NumSensitiveWords
# EmbeddedBrandName
# PctExtHyperlinks
# PctExtResourceUrls
# ExtFavicon
# InsecureForms
# RelativeFormAction
# ExtFormAction
# AbnormalFormAction
# PctNullSelfRedirectHyperlinks
# FrequentDomainNameMismatch
# FakeLinkInStatusBar
# RightClickDisabled
# PopUpWindow
# SubmitInfoToEmail
# IframeOrFrame
# MissingTitle
# ImagesOnlyInForm
# SubdomainLevelRT
# UrlLengthRT
# PctExtResourceUrlsRT
# AbnormalExtFormActionR
# ExtMetaScriptLinkRT
# PctExtNullSelfRedirectHyperlinksRT

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler

# dataset = pd.read_csv('Phishing_Legitimate_full.csv')

# x = dataset.drop(columns=["id", "CLASS_LABEL", "SubdomainLevel", ]).values
# y = dataset["CLASS_LABEL"].values

# scaler = StandardScaler().fit(x)
# x = scaler.transform(x)

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# model = linear_model.LogisticRegression().fit(x_train, y_train)

# print("Accuracy:", model.score(x_test, y_test))

# print("*************")
