function checkform(form) {
    // make sure forms arent empty
    var inputs = form.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        // only check forms that have the required attribute
        if(inputs[i].hasAttribute("required")){
            if(inputs[i].value == ""){
                // field is empty, send alert
                alert("Please fill all required fields");
                return false;
            }
        }
    }
    return true;
}

function generateMessage(form){
	if (checkform(form) == true) {
		
		// Pull values of all of the fields
		var user_name = document.getElementById("messageForm").elements.namedItem("inputName").value;
		var rep_name = document.getElementById("messageForm").elements.namedItem("repName").value;
		var rep_type = document.getElementById("messageForm").elements.namedItem("rep_type").value;
		
		// Create message with user input values
		var line1 = "Dear " + rep_type + " " + rep_name + ",<br /><br />";
		var body = "My name is " + user_name + " and Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.<br /><br />";
		var closer = "Sincerely,\n" + user_name;
		
		var complete_message = line1 + body + closer;
		
		// Change innerHTML with generated message
		document.getElementById("message").innerHTML = complete_message;
	}
}
