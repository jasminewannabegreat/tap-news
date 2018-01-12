var jayson = require('jayson');

//create a client connected to backend server
var client = jayson.client.http({
   port: 4040,
   hostname: 'localhost'
});

// Test methid
function add(a, b, callback){
   client.request('add', [a,b], function (err, error, response){
	if (err) throw err;
	console.log(response);
	callback(response);
   });
}

function getNewsSummariesForUser(user_id, page_Num,callback){
    client.request('getNewsSummariesForUser',[user_id, page_Num],function(err,error,response){
        if (err) throw err;
        console.log(response);
        console.log("response is from rpc-client");
        callback(response);
    });
}

// LOg a news click event for user
function logNewsClickForUser(user_id,news_id){
    client.request('logNewsClickForUser',[user_id,news_id],function(err,error,response){
        if(err) throw err;
        console.log(response);
    })
}

module.exports = {
   add: add,
   getNewsSummariesForUser: getNewsSummariesForUser,
   logNewsClickForUser:logNewsClickForUser
}


