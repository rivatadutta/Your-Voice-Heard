function checkform(form) {
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
		if(document.getElementById("messageForm01").elements.namedItem("reps_select").value == "disabledSelect") {
			alert("Please fill all required fields");
			return;
		}
		// Pull values of all of the fields
		var user_fname = document.getElementById("messageForm01").elements.namedItem("inputFirstName_01").value;
		var user_lname = document.getElementById("messageForm01").elements.namedItem("inputLastName_01").value;
		
		var rep_name = document.getElementById("messageForm01").elements.namedItem("reps_select").value;
		var rep_array = rep_name.split(", ");
		rep_name = rep_array[0];
		
		var optgroup = document.querySelector('#reps_select option:checked').parentElement.label;
		optgroup = optgroup.slice(0, -1);
        var source_text = document.getElementById("source-text").innerHTML;
		
		// Create message with user input values
		var line1 = "Dear " + optgroup + " " + rep_name + ",\n\n";
		var body = "My name is " + user_fname + " " + user_lname + " and I want you to listen to me about the following issue. " + source_text + "I urge you to take action.\n\n";
		var closer = "Sincerely,\n" + user_fname + " " + user_lname;
		
		var complete_message = line1 + body + closer;
		
		// Change innerHTML with generated message
		document.getElementById("message").value = complete_message;
	}
}

function generateEmail(form){
	if (checkform(form) == true) {
		if(document.getElementById("messageForm02").elements.namedItem("orgs").value == "disabledSelect") {
			alert("Please fill all required fields");
			return false;
		}
		// Pull values of all of the fields
		var user_fname = document.getElementById("messageForm02").elements.namedItem("inputFirstName_02").value;
		var user_lname = document.getElementById("messageForm02").elements.namedItem("inputLastName_02").value;
		var subject = "Black Lives Matter";
		var person = document.getElementById("messageForm02").elements.namedItem("orgs").value;
        var source_text = document.getElementById("source-text").innerHTML;
		var email;
		
		if (person == "Greg Fischer") {email = "Greg.Fischer@louisvilleky.gov";}
		else if (person == "Jacob Frey") {email = "Jacob.Frey@minneapolismn.gov";}
		
		// Create message with user input values
		var line1 = "Dear " + person + ",\n\n";
		var body = "My name is " + user_fname + " " + user_lname + " and I want you to listen to me about the following issue. " + source_text + " I urge you to take action.\n\n";
		var closer = "Sincerely,\n" + user_fname + " " + user_lname;
		
		var complete_message = line1 + body + closer;
		
		
		// Change innerHTML with generated message
		
		window.location.href = "mailto:" + email + "?subject="
        + encodeURIComponent(subject)
        + "&body=" + encodeURIComponent(complete_message);
	}
}
