var i = 0; /* Set Global Variable i */
function increment(){
i += 1; /* Function for automatic increment of field's "Name" attribute. */
}
/*
---------------------------------------------

Function to Remove Form Elements Dynamically
---------------------------------------------

*/
function removeElement(parentDiv, childDiv){
if (childDiv == parentDiv){
alert("The parent div cannot be removed.");
}
else if (document.getElementById(childDiv)){
var child = document.getElementById(childDiv);
var parent = document.getElementById(parentDiv);
parent.removeChild(child);
}
else{
alert("Child div has already been removed or does not exist.");
return false;
}
}
/*
----------------------------------------------------------------------------

Functions that will be called upon, when user click on the Name text field.

----------------------------------------------------------------------------
*/
function nameFunction(){
document.getElementById("customer_name").setAttribute("style", ""); 
}
function customerFunction(){
document.getElementById("customer_info").setAttribute("style", "");
document.getElementById("customer_info1").setAttribute("style", ""); 
document.getElementById("customer_info2").setAttribute("style", "");
document.getElementById("customer_info3").setAttribute("style", "");
document.getElementById("Company_info").setAttribute("style", "display:None");
document.getElementById("Company_info1").setAttribute("style", "display:None"); 
document.getElementById("Company_info2").setAttribute("style", "display:None");
document.getElementById("Company_info3").setAttribute("style", "display:None");  
}

function companyFunction(){
document.getElementById("Company_info").setAttribute("style", "");
document.getElementById("Company_info1").setAttribute("style", ""); 
document.getElementById("Company_info2").setAttribute("style", "");
document.getElementById("Company_info3").setAttribute("style", "");
document.getElementById("customer_info").setAttribute("style", "display:None");
document.getElementById("customer_info1").setAttribute("style", "display:None"); 
document.getElementById("customer_info2").setAttribute("style", "display:None");
document.getElementById("customer_info3").setAttribute("style", "display:None");
}

function CreateOrderFunction(){
document.getElementById("CreateOrder").setAttribute("style", "");
document.getElementById("DeleteOrder").setAttribute("style", "display:None");
document.getElementById("UpdateProfile").setAttribute("style", "display:None");
}
function DeleteOrderFunction(){
document.getElementById("DeleteOrder").setAttribute("style", "");
document.getElementById("CreateOrder").setAttribute("style", "display:None");
document.getElementById("UpdateProfile").setAttribute("style", "display:None");
}
function UpdateProfileFunction(){
document.getElementById("UpdateProfile").setAttribute("style", "");
document.getElementById("DeleteOrder").setAttribute("style", "display:None");
document.getElementById("CreateOrder").setAttribute("style", "display:None");
}
/*
-----------------------------------------------------------------------------

Functions that will be called upon, when user click on the E-mail text field.

------------------------------------------------------------------------------
*/
function emailFunction(){
var r = document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder", "Email");
var g = document.createElement("IMG");
g.setAttribute("src", "delete.png");
increment();
y.setAttribute("Name", "textelement_" + i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_" + i + "')");
r.appendChild(g);
r.setAttribute("id", "id_" + i);
document.getElementById("myForm").appendChild(r);
}
/*
-----------------------------------------------------------------------------

Functions that will be called upon, when user click on the Contact text field.

------------------------------------------------------------------------------
*/
function contactFunction(){
var r = document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder", "Contact");
var g = document.createElement("IMG");
g.setAttribute("src", "delete.png");
increment();
y.setAttribute("Name", "textelement_" + i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_" + i + "')");
r.appendChild(g);
r.setAttribute("id", "id_" + i);
document.getElementById("myForm").appendChild(r);
}
/*
-----------------------------------------------------------------------------

Functions that will be called upon, when user click on the Message textarea field.

------------------------------------------------------------------------------
*/
function textareaFunction(){
var r = document.createElement('span');
var y = document.createElement("TEXTAREA");
var g = document.createElement("IMG");
y.setAttribute("cols", "17");
y.setAttribute("placeholder", "message..");
g.setAttribute("src", "delete.png");
increment();
y.setAttribute("Name", "textelement_" + i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_" + i + "')");
r.appendChild(g);
r.setAttribute("id", "id_" + i);
document.getElementById("myForm").appendChild(r);
}
/*
-----------------------------------------------------------------------------

Functions that will be called upon, when user click on the Reset Button.

------------------------------------------------------------------------------
*/
function resetElements(){
document.getElementById('myForm').innerHTML = '';
}