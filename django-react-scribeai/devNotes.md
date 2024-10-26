# Middleware to log each request
```app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next(); // Move on to the next middleware
});```

# Parse JSON data for incoming requests
```app.use(express.json());```

# Route handler
```app.get('/', (req, res) => {
    res.send('Hello, world!');
});```

# Error-handling middleware
```app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
});```

__SOCKET PART__
```socket.on('sendUserInput', ...):```

This part is listening for the "sendUserInput" event from the client, which triggers when the client emits that event (e.g., socket.emit('sendUserInput', userMessage)).
socket.on is how you set up event listeners on the server side with socket.io.