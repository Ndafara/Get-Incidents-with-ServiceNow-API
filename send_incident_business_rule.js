(function executeRule(current, previous /*null when async*/ ) {
    try {
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint("<INSERT YOUR WEBHOOK URL HERE>");
        r.setHttpMethod("post");

        var usr = new GlideRecord('sys_user');

        var number = current.getValue("number");
        var opened_at = current.getValue("opened_at");
        var impact = current.getValue("impact");
        var urgency = current.getValue("urgency");
        var short_description = current.getValue("short_description");
        var category = current.getValue("category");
        var priority = current.getValue("priority");
        var sys_id = current.getValue("sys_id");
		var state = current.getValue("state");

		var obj = {
            "number": number,
            "opened_at": opened_at,
            "impact": impact,
            "urgency": urgency,
            "short_description": short_description,
            "category": category,
            "priority": priority,
            "sys_id": sys_id,
			"state": state
        };

        var body = JSON.stringify(obj);
        gs.info("Webhook body: " + body);
        r.setRequestBody(body);

        var response = r.execute();
        var httpStatus = response.getStatusCode();
    } catch (ex) {
        var message = ex.message;
		gs.error("Error message: " + message);
    }

    gs.info("Webhook target HTTP status response: " + httpStatus);

})(current, previous);