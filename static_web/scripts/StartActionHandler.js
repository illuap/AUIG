
    async function SetStartingAction(){
        var results = null;
        var alert_obj = null

        option = $('#startActionSelect').find(':selected')[0];

        if(option.value == ""){
            console.log("please select a valid starting action");

            alert_obj = new alertClass("Danger", "Please select a valid starting action.");
            SetStartingAction_Callback(alert_obj.type, alert_obj.message)
        }else{
            console.log("Starting to update the profile to: " + option.value);
            results = await eel.set_startingAction(option.value)(SetStartingAction_Callback); //TODO maybe a callback?
        }
    }

    // Possibly expose? tp update everytime the profile changes
    async function LoadAllStartingActions(){

        results = await eel.getAllActions()()
        startingAction = await eel.get_startingAction()()

        
        // TODO update the starting action.....
        $('#startActionSelect').find('selected').remove()
        for(var i in results){ 
            if(results[i] == startingAction){
                $('#startActionSelect').append('<option selected value="' + results[i] +'">'+ results[i] +'</option>');
            }else{
                $('#startActionSelect').append('<option value="' + results[i] +'">'+ results[i] +'</option>');
            }
        }
    }
$( document ).ready(function() {
    LoadAllStartingActions().then(function(msg) {
        console.log(msg);
        })
        .catch(function(error) {
        console.error(error);
        });
});
