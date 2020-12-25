
//#region Backend Communications
        
    async function setAvailableEdges(){
        edges = []
        await eel.getAllEdgesPY()((results) =>
            {
                console.log(results);
                generticAlertIfError(results);
                edges = results[2] ;
                
                $(".AddActionToProfileForm-edge-selecter").empty();
                edges.forEach(edge => {
                    console.log(edge);
                    $(".AddActionToProfileForm-edge-selecter")
                        .append('<button type="button" onclick="updateEdgeLabel(this, \''+ edge +'\')">'+
                                        edge+
                                   '</button>');
                });
                
            }
        )
    }

    function updateEdgeLabel(div, edgeName){
        $(div.parentNode).parent(".AddActionToProfileForm-edge-section").find(".AddActionToProfileForm-edge").val(edgeName)
    }

    async function countDown(div, seconds){
        div.text(seconds);
        var countdown = setInterval(function() {
            seconds--;
            div.text(seconds);
            if (seconds <= 0) clearInterval(countdown);
        }, 1000); 
    }

    function setCoordinates(sectionDiv, xVal, yVal){
        x = sectionDiv.find(".AddActionToProfileForm-coordinate-x");
        y = sectionDiv.find(".AddActionToProfileForm-coordinate-y");

        x.val(xVal);
        y.val(yVal);
    }

    var delayFunc = async function(sectionDiv){
        
        return await eel.populateCoordinatesPY()((results) => {
                generticAlertIfError(results);
                setCoordinates(sectionDiv, results[2][0], results[2][1]);
            });
     };

    function populateCoordinates(button){
        //trigger count down
    
        masterDiv = $(button).parent(".AddActionToProfileForm-coordinate-section");
        countDownTime = 3;
        countDown(masterDiv.find(".count-down"), countDownTime);

        // call python

        setTimeout(function() {
                delayFunc(masterDiv)//setCoordinates(masterDiv, results[0], results[1]));
            }, countDownTime * 1000 );
    }


    async function addActionToProfileJS(){
        var json = grabFormData()
        results = await eel.addActionToProfilePY(json)(addActionToProfileJS_Callback);
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

    //#region UI FUNCTIONS// This is a repeating function must be done specifically forrent ert sectionar each class
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
        setAvailableEdges();
    }
    function removeSection(section){
        $(section.parentNode).fadeOut();
    }

    addAnotherEdgeSection();
    //#endregion