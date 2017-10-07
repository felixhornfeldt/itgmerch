simpleCart({
    checkout: { 
        type: "SendForm" , 
        url: "/cart/" ,
        // http method for form, "POST" or "GET", default is "POST"
        method: "POST" , 
        
        extra_data: {
          storename: "Bob's cool plumbing store",
          cartid: "12321321"
        }
    } 
});