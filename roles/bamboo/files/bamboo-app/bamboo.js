var http = require('http');
var config = require('./config.json');
var dispatcher_class = require('httpdispatcher');
var dispatcher = new dispatcher_class();

function handleRequest(request, response){
    try {
        console.log("Requested URL: " + request.url);
        dispatcher.dispatch(request, response);
    } catch(err) {
        console.log(err);
    }
}

dispatcher.onGet("/", function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('I <3 Bamboo');
});

dispatcher.onPost("/", function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('I <3 Bamboo from post');
});

dispatcher.onError(function(req, res) {
        res.writeHead(404);
        res.end("404 - Page Does not exists");
});

http.createServer(handleRequest).listen(config.port, function(){
    console.log("Server listening on: http://localhost:%s", config.port);
});
