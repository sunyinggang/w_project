"use strict";app.factory("HomeService",["$http","HelperService",function(o,n){var e={updateToken:function(e){var t={method:"user.updateToken",token:e};return o.get(n.API+n.encode(t))},profile:function(e){var t={method:"operation.profile",data:"all",token:e};return o.get(n.API+n.encode(t))},travelSummary:function(e,t){var r={method:"travel.getHalfYearTravelSummary",calDate:t,token:e};return o.get(n.API+n.encode(r))},expenseProfile:function(e,t){var r={method:"expense.expenseHalfYearProfile",calDate:t,token:e};return o.get(n.API+n.encode(r))},showPromotion:function(e){var t={method:"productOrder.showPromotion",token:e};return o.get(n.API+n.encode(t))}};return e}]);