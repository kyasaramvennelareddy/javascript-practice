 //converting the data from one type to another 
//  let num=6
let num=String(6)
console.log(num,typeof num);    //6 string

let ooo=Number("123")
console.log(ooo,typeof ooo)     //123 number

let und
console.log(und,typeof und)     //undefined

//if we and to do any operation between different types of data we have to come to a conseses (both should be common data type)
//for the data which has numbers and string together to seperate it we use parseint 
let all="1234 veny"
console.log(parseInt(all))