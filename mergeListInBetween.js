var mergeInBetween = function(list1, a, b, list2) {
   var start = list1
   var end = list1
    for(var i=0;i<b;i++){
        if(i<a-1) start = start.next
        if (i<b) end = end.next
    }
    var body = list2
    while(body.next!= null){
        body = body.next
    }
    start.next = list2
    body.next = end.next
    return list1
    return end
};