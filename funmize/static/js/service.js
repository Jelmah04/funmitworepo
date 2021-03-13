

 //<![CDATA[ 
 // array of possible countries in the same order as they appear in the country selection list MTN, 9MOBILE, GLO or AIRTEL
 var countryLists = new Array(4) 
 countryLists["empty"] = ["Select a Country"]; 
 countryLists["MTN"] = ["COPERATE GIFTING 1GB = N300","COPERATE GIFTING 2GB = N1000","COPERATE GIFTING 3GB = N1500", "COPERATE GIFTING 4GB = N1900","COPERATE GIFTING 5GB = N2400","COPERATE GIFTING 10GB = N2400","SME 1GB = N300","SME 2GB = N1000","SME 3GB = N1500", "SME 4GB = N1900","SME 5GB = N2400","SME 10GB = N2400","NORMAL GIFTING 1GB = N300","NORMAL GIFTING 2GB = N1000","NORMAL GIFTING 3GB = N1500", "NORMAL GIFTING 4GB = N1900","NORMAL GIFTING 5GB = N2400","NORMAL GIFTING 10GB = N2400" ]; 
 countryLists["GLO"] = ["1GB = N450","2GB = N850","4.5GB = N1700","7.2GB = N2125"]; 
 countryLists["ETISALAT"]= ["1GB = N700","2GB = N1400","3GB = N2000"]; 
countryLists["AIRTEL"]= ["1.5GB = N950","3.5GB = N1900","5GB = N2400"]; 
 /* CountryChange() is called from the onchange event of a select element. 
 * param selectObj - the select object which fired the on change event. 
 */ 
 function countryChange(selectObj) { 
 // get the index of the selected option 
 var idx = selectObj.selectedIndex; 
 // get the value of the selected option 
 var which = selectObj.options[idx].value; 
 // use the selected option value to retrieve the list of items from the countryLists array 
 cList = countryLists[which]; 
 // get the country select element via its known id 
 var cSelect = document.getElementById("country"); 
 // remove the current options from the country select 
 var len=cSelect.options.length; 
 while (cSelect.options.length > 0) { 
 cSelect.remove(0); 
 } 
 var newOption; 
 // create new options 
 for (var i=0; i<cList.length; i++) { 
 newOption = document.createElement("option"); 
 newOption.value = cList[i];  // assumes option string and value are the same 
 newOption.text=cList[i]; 
 // add the new option 
 try { 
 cSelect.add(newOption);  // this will fail in DOM browsers but is needed for IE 
 } 
 catch (e) { 
 cSelect.appendChild(newOption); 
 } 
 } 
 } 
//]]>


var countryListss = new Array(4) 
countryListss["empty"] = ["Select a Service"]; 
countryListss["GOTV"] = ["GOtv LITE (GOLITE) - N400","GOtv Value  (GOTV) - N1250","GOtv Plus  (GOTVPLS) - N1900","GOtv Max (GOTVMAX) - N3200" ]; 
countryListss["DSTV"]= ["DStv Access (ACSSE36) - N2000","DStv Family (COFAME36) - N4000","DStv Compact (COMPE36) - N6800","DStv Compact Plus (COMPLE36) - N10650","DStv Premium (PRWE36) - N15800","DStv Premium + HD/Exra View () - N18000"]; 
countryListss["STARTIMES"] = ["StarTimes nova (starn)- N900","StarTimes Basic (STARB)- N1300","StarTimes Smart (STARS)- N1900","StarTimes Classic (STARC) - N2600","StarTimes Unique (STARU) - N3800"]; 
countryListss["CONSAT"] = ["Consat nova (starn)- N900","Consat Basic (STARB)- N1300","Consat Smart (STARS)- N1900","Consat Classic (STARC) - N2600","Consat Unique (STARU) - N3800"]; 
function countryChanged(selectObj) { 
// get the index of the selected option 
var idxx = selectObj.selectedIndex; 
// get the value of the selected option 
var which = selectObj.options[idxx].value; 
// use the selected option value to retrieve the list of items from the countryListss array 
cList = countryListss[which]; 
// get the country select element via its known id 
var cSelect = document.getElementById("countrry"); 
// remove the current options from the country select 
var len=cSelect.options.length; 
while (cSelect.options.length > 0) { 
cSelect.remove(0); 
} 
var newOption; 
// create new options 
for (var i=0; i<cList.length; i++) { 
newOption = document.createElement("option"); 
newOption.value = cList[i];  // assumes option string and value are the same 
newOption.text=cList[i]; 
// add the new option 
try { 
cSelect.add(newOption);  // this will fail in DOM browsers but is needed for IE 
} 
catch (e) { 
cSelect.appendChild(newOption); 
} 
} 
} 
//]]>
