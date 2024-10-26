import React, { useEffect, useState } from 'react';
import "./Main.css";

import "./Message.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";

import io from 'socket.io-client';

const socket = io('http://localhost:5000');

const UserMessage =  ({text})=> {
      return (
        <section className="single-message-user">
          <div className="user-icon">
              <FontAwesomeIcon icon={faUser} size="2x" />
          </div>
          <div>
              <p className="single-message-text">{text}
              User
              </p>
          </div>
        </section>
      );
}
const BotMessage =  ({text})=> {
  return (
    <section className="single-message-bot">
      <div className="user-icon">
          <FontAwesomeIcon icon={faUser} size="2x" />
      </div>
      <div>
          <p className="single-message-text">{text}
          Bot
          </p>
      </div>
    </section>
  );
}


function Main(){
  const [messages, setMessages] = useState([])
  const [userInput, setUserInput] = useState("");
  
  const addMessage = () => {
    // Example of adding a new message
    // where we would put the response 
    const newMessage = {
      text: "New dynamic message at " + new Date().toLocaleTimeString()+" "+ (messages.length + 1),
      useUserStyle: messages.length % 2 === 0 // Alternate styles for odd/even
    };
    setMessages(prevMessages => [...prevMessages, newMessage]);
  };
  // Use useEffect to set up the socket listener
  
  useEffect(() => {
    // Function to handle incoming intent results
    const handleIncomingMessage = (result) => {
      console.log("Received result:", result); // Check what you're receiving

        // Extract event name and data from the result
      const eventName = result[0]; // Get the event name
      const data = result[1]; // Get the data object

      if (eventName === "receiveResponse") {
        const intent = data.intent; // Extract the intent
        const patientResults = data.results; // Extract the patient results

        // Prepare a message summarizing the intent and patient information
        if (patientResults.length > 0) {
            // If there are patient results, map through them
            const newMessages = patientResults.map(patient => ({
                text: `Patient: ${patient.name}\n
                      General Info: ${patient.generalInfo}\n
                      Appointments: ${patient.appointments}\n
                      Medication Info: ${patient.medicationInfo}`,
                useUserStyle: false // Assuming bot style for responses
            }));
            // Update the messages state with new patient messages
            setMessages((prevMessages) => [...prevMessages, ...newMessages]);
        } else {
            // If there are no results, provide a fallback message
            const noResultsMessage = {
                text: "No relevant patient information found for your request.",
                useUserStyle: false // Assuming bot style for responses
            };
            // Update the messages state with the fallback message
            setMessages((prevMessages) => [...prevMessages, noResultsMessage]);
        }
      }
    };

    // Listen for the "intentResult" event
    socket.on("intentResult", handleIncomingMessage);

    // Cleanup function to remove the listener on unmount
    return () => {
      socket.off("intentResult", handleIncomingMessage);
    };

  }, []); // Empty dependency array means this runs once on mount and cleanup on unmount

  const sendMessage = (event) => {
    event.preventDefault(); // Prevent default form submission
    if (userInput.trim()) { // Check for non-empty input
        //update the message list based on our user input!!!
        const newMessage = {
          text: new Date().toLocaleTimeString()+" "+ userInput,
          useUserStyle: true
        };
        setMessages((prevMessages) => [...prevMessages, newMessage])
        socket.emit("sendUserInput", userInput); // Send user input to the server
        setUserInput(""); // Clear the input field
    }
  };


    return (<>
        <main>
            <button onClick={addMessage}>Add Message</button>
            {messages.map((message, index) => (
                (message.useUserStyle)?
                (<UserMessage key={index} text={message.text} />):
                (<BotMessage key={index} text={message.text} />)
            ))}

            <form onSubmit={sendMessage}>
                <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)} // Update state on input change
                    placeholder="Type your message..."
                />
                <button type="submit">Send</button>
            </form>
        </main>
        
        </>
    );
}

export default Main;