
class alertClass{
    
    constructor(type, message){
        this.type = type;
        this.message = message;
    }
    
    get_bootstrap_alert_class_type(){
        if(this.type.toLowerCase() == "success"){
            return "alert-success";
        }else if(this.type.toLowerCase() == "danger"){
            return "alert-danger";
        }else{
            console.error("unsupported alertclass type");
            return ""
        }
    }

    get_alert_html(){
        var htmlAlert = '<div class="alert '+ this.get_bootstrap_alert_class_type() +' alert-dismissible fade show" role="alert"><strong>'+this.type+'</strong> '+ this.message +'<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
        return htmlAlert; 
    }

    show_alert(html_wrapper){
        html_wrapper.append(this.get_alert_html());
        html_wrapper.find(".alert").first().hide().fadeIn(200).delay(2000).fadeOut(1000, function () { $(this).remove(); });
    }
}

// This is a repeating function must be done specifically for each different alert section
function SetActionProfile_Callback(resultStatus){
    alert_obj = new alertClass(resultStatus[0], resultStatus[1]);
    alert_obj.show_alert($(".alert-wrapper"));
    delete alert_obj;
}

function addActionToProfileJS_Callback(resultStatus){
    alert_obj = new alertClass(resultStatus[0], resultStatus[1]);
    alert_obj.show_alert($(".alert-wrapper-addAction"));
    delete alert_obj;
}