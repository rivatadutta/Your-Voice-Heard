function checkform(form) {
    // get all the inputs within the submitted form
    var inputs = form.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        // only validate the inputs that have the required attribute
        if(inputs[i].hasAttribute("required")){
            if(inputs[i].value == ""){
                // found an empty field that is required
                alert("Please fill all required fields");
                return false;
            }
        }
    }
    return true;
}

function generateMessage(form){
    // Initiate Variables With Form Content
	if (checkform(form) == true) {
		
		var user_name = document.getElementById("messageForm").elements.namedItem("inputName").value;
		var rep_name = document.getElementById("messageForm").elements.namedItem("repName").value;
		var rep_type = document.getElementById("messageForm").elements.namedItem("rep_type").value;
		
		var line1 = "Dear " + rep_type + " " + rep_name + ",<br /><br />";
		var body = "My name is " + user_name + " and Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.<br /><br />";
		var closer = "Sincerely,\n" + user_name;
		
		var complete_message = line1 + body + closer;
		
		document.getElementById("message").innerHTML = complete_message;
	}
}
