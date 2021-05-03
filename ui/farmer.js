import farmerSchema from "./schemas/farmer.json";
import {validate} from "jsonschema";
//accurate object
let farmer1 = {
    farmer_id:"AK/OT/0008",
    name:"Lubowa Ahmed"
}
//incorrect id length
let farmer2 = {
    farmer_id:"AK/OT/004",
    name:"Lubwama Ahmed"
}
//missing name
let farmer3 = {
    "farmer_id":"AK/OT/0009"
}
function submit_farmer(farmer){
    try{
        validate(farmer,farmerSchema,{throwError:true});
        console.log(farmer);
    }catch(e){
        console.log(e.path + ' ' + e.message);
    }
}
[farmer1,farmer2,farmer3].map(submit_farmer)
