class resultStatus{
    constructor(results){
        if(length(results) != 3){
            console.error("Invalid Result Status");
            console.error(results);
        }
        this.code = results[0];
        this.error_msg = results[1];
        this.data = results[2];       
    }
}
