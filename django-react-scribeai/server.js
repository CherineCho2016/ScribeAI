const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');
const fs = require('fs'); // To load JSON data

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
    cors: {
        origin: "http://localhost:3000", // Frontend origin
        methods: ["GET", "POST"]
    }
});

app.use(cors());
app.use(express.json());

// Load JSON patient data
const patientData = JSON.parse(fs.readFileSync('./dummyDataGeo/patients.json', 'utf-8'));

// Function to simulate an ML model for intent processing
function identifyIntent(userInput) {
    // Simulate intent identification based on keywords (replace with actual ML model in production)
    if (userInput.includes("medication")) return "medication";
    if (userInput.includes("appointment")) return "appointment";
    return "general";
}

// Middleware to handle intent processing
app.use((req, res, next) => {
    // for each req, check the body and userinput to see if there is stuff in it
    if (req.body && req.body.userInput) {
        // run the ML model to figure out intent on the userinput
        const intent = identifyIntent(req.body.userInput);
        req.intent = intent; // Attach identified intent to the request object
        next();                                                     // next box in the list
    } else {
        // if no stuff, then error
        res.status(400).send("User input is required.");
    }
});

// Route to handle intent and query JSON data
app.post('/process', (req, res) => {
    // if sent to the process endpt
    const { intent } = req;                     // grab the req
    const query = req.body.userInput;           // grab the og userinput and save as query

    let responseData;                           // set up response data
    if (intent === "medication") {
        // if the intent was medication, for example, filter the patient data, checking if certain data has query word
        responseData = patientData.filter(patient => patient.medicationInfo && patient.medicationInfo.includes(query));
    } else if (intent === "appointment") {
        responseData = patientData.filter(patient => patient.appointments && patient.appointments.includes(query));
    } else {
        responseData = patientData.filter(patient => patient.generalInfo && patient.generalInfo.includes(query));
    }
    // respond with json containing intent and response data
    res.json({ intent, results: responseData });
});

// Socket.IO connection
io.on('connection', (socket) => {
    console.log('New client connected');
    // socket.on('sendUserInput'...) listening for the "sendUserInput" event from the client, which
    // triggers when the client emits that event (e.g., socket.emit('sendUserInput', userMessage))
    socket.on('sendUserInput', async (message) => {
        // Sending message to middleware and JSON processor via the API route
        const response = await fetch('http://localhost:5000/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userInput: message })                // input is as json body
        });
        const data = await response.json();
        socket.emit('receiveResponse', data); // Send data back to frontend
    });

    socket.on('disconnect', () => {
        console.log('Client disconnected');
    });
});

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));