    //#region Backend Communications


    async function addActionToProfileJS(json){
        results = await eel.addActionToProfilePY(json)();
    }
    
    function addActionToProfileCallBackJS(error, results){
        if (error != null){
            // ERROR
            //TODO: ERROR MESSAGE
            console.error(results);
        }else{
            // SUCCESS
            //TODO: SUCCESS
            
        }
    }

    //#endregion
    
    
    // #region LOGIC
    class FormDataObj{
        name = "";
        actionType = "";
        edges = {};
        images = [];
        coordinates = [];
        pre_delay = 0;
        post_delay = 0;
    }
    async function selectImage(button){
        var imageDir = await eel.selectImageTK()();
        $(button.parentNode).find(".AddActionToProfileForm-image").val(imageDir);
    }
    function grabFormData(){
        var formDataObj = new FormDataObj();

        formDataObj.name = $('#AddActionToProfileForm').find('#AddActionToProfileForm-title').val(); 
        formDataObj.actionType = $('#AddActionToProfileForm').find('#AddActionToProfileForm-actionType').val(); 
        formDataObj.edges = grabEdgeFormData();
        formDataObj.images = grabImageFormData();
        formDataObj.coordinates = grabCoordinateFormData(); 
        formDataObj.pre_delay = $('#AddActionToProfileForm').find('#AddActionToProfileForm-predelay').val(); 
        formDataObj.post_delay = $('#AddActionToProfileForm').find('#AddActionToProfileForm-postdelay').val(); 
       
        var json = JSON.stringify(formDataObj);
        console.log(json);
        return json; 
    }
    function grabEdgeFormData(){
        var temp = {}
        $('#AddActionToProfileForm').find('.AddActionToProfileForm-edge-section:visible').each(function() { 
                                var status = $(this).find('.AddActionToProfileForm-edge-status').val();
                                var newNodeName = $(this).find('.AddActionToProfileForm-edge').val();

                                if(status == "" || newNodeName == ""){
                                    //TODO warnings..
                                }else{
                                    temp[status] = newNodeName;
                                }

                            });
        return temp;
    }

    function grabImageFormData(){
        var temp = []
        $('#AddActionToProfileForm').find('.AddActionToProfileForm-image-section:visible').each(function() {
                        temp.push($(this).find('.AddActionToProfileForm-image').val());
                    });
        return temp;
    }
    function grabCoordinateFormData(){
        var cords = [];
        $('#AddActionToProfileForm').find('.AddActionToProfileForm-coordinate-section:visible').each(function() {
                       cords[0] = $(this).find('.AddActionToProfileForm-coordinate-x').val();
                       cords[1] = $(this).find('.AddActionToProfileForm-coordinate-y').val();
                    });

        if(cords.length == 0) return [];
        return cords;

    }
    //#endregion

    //#region UI FUNCTIONS
    function addAnotherCoordinateSection(){
        result = $(".AddActionToProfileForm-coordinate-section-template")
                                .clone()
                                .removeClass("AddActionToProfileForm-coordinate-section-template")
                                .appendTo(".AddActionToProfileForm-coordinate-wrapper")
                                .fadeIn();
    }
    function addAnotherImageSection(){
        result = $(".AddActionToProfileForm-image-section-template")
                                .clone()
                                .removeClass("AddActionToProfileForm-image-section-template")
                                .appendTo(".AddActionToProfileForm-image-wrapper")
                                .fadeIn();
    }
    function addAnotherEdgeSection(){
        result = $(".AddActionToProfileForm-edge-section-template")
                                .clone()
                                .removeClass("AddActionToProfileForm-edge-section-template")
                                .appendTo(".AddActionToProfileForm-edge-wrapper")
                                .fadeIn();
    }
    function removeSection(section){
        $(section.parentNode).fadeOut();
    }

    addAnotherEdgeSection();
    //#endregion