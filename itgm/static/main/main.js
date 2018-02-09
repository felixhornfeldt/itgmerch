simpleCart({
    checkout: {
        type: "SendForm" ,
        url: "/order/order/" ,
        // http method for form, "POST" or "GET", default is "POST"
        method: "POST" ,
        // an option list of extra name/value pairs that can
        // be sent along with the checkout data
        extra_data: {
          order: 'If somebody intercepts this, well done you!',
          // total: document.getElementById('simpleCart_grandTotal').value
        }
    }
});

function showDiv() {
    document.getElementById('show').style.display = "block";
}

function removeDiv() {
    document.getElementById('show').style.display = "none";
}