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
        	var source_text = document.getElementById("source-text").innerHTML;
		
		// Create message with user input values
		var line1 = "Dear " + rep_type + " " + rep_name + ",\n\n";
		var body = "My name is " + user_name + " and I want you to listen to me about the following issue. " + source_text + "I urge you to take action.\n\n";
		var closer = "Sincerely,\n" + user_name;
		
		var complete_message = line1 + body + closer;
		
		// Change innerHTML with generated message
		document.getElementById("message").value = complete_message;
	}
}
