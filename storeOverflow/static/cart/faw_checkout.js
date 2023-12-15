function getLastPart(url) {
    var parts = url.split("/");
    return (url.lastIndexOf('/') !== url.length - 1
            ? parts[parts.length - 1]
            : parts[parts.length - 2]);
}

    function checkout() {
        let lang = 'en';
        const configuration = {
            locale : locale,  //default en
            //divSelector : 'fawry-payments',  // required and you may change the div id as required
            mode: DISPLAY_MODE.SEPARATED,  //required, allowed values [POPUP, INSIDE_PAGE, SIDE_PAGE, SEPARATED]
            onSuccess : successCallBack,  // optional and not supported in SEPARATED display
            onFailure : failureCallBack,  // optional and not supported in SEPARATED display
        };
        FawryPay.checkout(buildChargeRequest(), configuration);
    }

    function successCallBack(data) {
        console.log('handle successful callback as desired, data', data);
        document.location.href = callBack;
    }
    function failureCallBack(data) {
        console.log('handle failure callback as desired, data', data);
        document.location.href = callBack;
    }
    function buildChargeRequest() {
        
        const chargeRequest = {
            merchantCode: merchant, // the merchant account number in Fawry
            merchantRefNum: merchantRefNum, // order refrence number from merchant side
            customerMobile: customer.customerMobile,
            customerEmail: customer.customerEmail,
            customerName: customer.customerName,
            chargeItems: productsJSON.orderItems,
            paymentExpiry: paymentExpiry,
            returnUrl: callBack,
            signature: signature
        };
        console.log(chargeRequest);
        return chargeRequest;
    }

(function ($) {
    'use strict';
    $(function () {
        //$("#faw_checkout").data()

        var mode = null
        var orderDesc = null;

        // console.log(productsJSON.orderItems)
        // console.log(merchant)
        //$("#faw_checkout").trigger('click');


        //checkout();

    }); //end $(function() {
})(jQuery);
