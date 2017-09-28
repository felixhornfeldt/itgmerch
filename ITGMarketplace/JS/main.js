/*simpleCart({
    checkout: { 
        type: "SendForm" , 
        url: "/order/" ,
        // http method for form, "POST" or "GET", default is "POST"
        method: "POST" , 
        // url to return to on successful checkout, default is null
        success: "success.html" , 
        // url to return to on cancelled checkout, default is null
        cancel: "cancel.html" ,
        // an option list of extra name/value pairs that can
        // be sent along with the checkout data
        extra_data: {
          storename: "Bob's cool plumbing store",
          cartid: "12321321"
        }
    } 
});*/

simpleCart({
    checkout: { 
        type: "PayPal" , 
        email: "felix.hornfeldt@outlook.com" 
    } 
});