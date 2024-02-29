from urllib.parse import urlparse

url = input("Enter a url: ")
print ( 'url: ' + url )
comp = urlparse(url)

print ('scheme  :' +  comp.scheme)
print ('netloc  :' +  comp.netloc)
print ('path    :' +  comp.path)
print ('params  :' +  comp.params)
print ('query   :' +  comp.query)
print ('fragment:' +  comp.fragment)
# print ('username:' +  comp.username)
# print ('password:' +  comp.password)
print ('hostname:' +  comp.hostname + '(netloc in lower case)')
# print ('port    :' +  comp.port)

NumDots = 0
for i in url: 
    if i == ".":
        NumDots += 1
# print ( NumDots )

# SubdomainLevel = 0 
# for i in url: 
#     if i == ".":
#         SubdomainLevel += 1
# if SubdomainLevel != 0:
#     SubdomainLevel -= 1
# print ( SubdomainLevel )



# PathLevel = 



UrlLength = 0
for i in url: 
    UrlLength += 1
# print ( UrlLength )

NumDash = 0
for i in url: 
    if i == "-":
        NumDash += 1
# print ( NumDash )



# NumDashInHostname = 



AtSymbol = 0 
for i in url: 
    if i == "@":
        AtSymbol += 1
# print ( AtSymbol )

TildeSymbol = 0
for i in url: 
    if i == "~":
        TildeSymbol += 1
# print ( TildeSymbol )

NumUnderscore = 0
for i in url: 
    if i == "_":
        NumUnderscore += 1
# print ( NumUnderscore )

NumPercent = 0 
for i in url: 
    if i == "%":
        NumPercent += 1
# print ( NumPercent )



# NumQueryComponents



NumAmpersand = 0 
for i in url: 
    if i == "&": 
        NumAmpersand += 1
# print ( NumAmpersand )

NumHash = 0 
for i in url: 
    if i == "#": 
        NumHash += 1
# print ( NumHash )

NumNumericChars = 0 
for i in url: 
    if i in "1234567890": 
        NumNumericChars += 1
# print ( NumNumericChars )

NoHttps = 0
if "https" in url: 
    NoHttps = 1
# print ( NoHttps )

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

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('Phishing_Legitimate_full.csv')

x = dataset[["NumDots", "UrlLength", "NumDash", "AtSymbol", "TildeSymbol", "NumUnderscore", "NumPercent", "NumAmpersand", "NumHash", "NumNumericChars"]].values
y = dataset["CLASS_LABEL"].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = linear_model.LogisticRegression().fit(x_train, y_train)


print("*************")
print("Accuracy:", model.score(x_test, y_test))
print("*************")

# Control: 
print("****CONTROL****")
# 2,53,0,0,0,0,0,0,0,4,1
y_cred=int(model.predict([[2,53,0,0,0,0,0,0,0,4]]))
if y_cred == 0:
    y_cred = "Not Phishing"
else:
    y_cred = "Phishing"
print("Control Predicted:" , y_cred)

print("****TEST*****")
y_pred=int(model.predict([[NumDots, UrlLength, NumDash, AtSymbol, TildeSymbol, NumUnderscore, NumPercent, NumAmpersand, NumHash, NumNumericChars]]))

if y_pred == 0:
    y_pred = "Not Phishing"
else:
    y_pred = "Phishing"

print("Predicted:" , y_pred)
print("")

