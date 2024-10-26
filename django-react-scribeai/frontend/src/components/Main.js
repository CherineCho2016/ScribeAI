import React, { useEffect, useState, useRef } from 'react';
import "./Main.css";
import "./Form.css"; // Assuming you have a CSS file for styles
import "./Message.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faPaperPlane } from "@fortawesome/free-solid-svg-icons";

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
  
  const [text, setText] = useState("");
  // Use useEffect to set up the socket listener
  
  useEffect(() => {
    // Function to handle incoming intent results
    const handleIncomingMessage = (result) => {
      console.log("Received result:", result); // Check what you're receiving
      const { intent, results: patientResults } = result;

        // Prepare a message summarizing the intent and patient information
        if (patientResults && patientResults.length > 0 ) {

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
            console.log("no result")
            setMessages((prevMessages) => [...prevMessages, noResultsMessage]);
        }
      
    };

    // Listen for the "receiveResponse" event
    socket.on("receiveResponse", handleIncomingMessage);
  

    // Cleanup function to remove the listener on unmount
    return () => {
      socket.off("receiveResponse", handleIncomingMessage);
      socket.off("connect")
    };

  }, []); // Empty dependency array means this runs once on mount and cleanup on unmount

  // from the form componenet
  

  const sendMessage = (event) => {
    event.preventDefault(); // Prevent default form submission
    if (text.trim()) { // Check for non-empty input
        //update the message list based on our user input!!!
        const newMessage = {
          text: new Date().toLocaleTimeString()+" "+ text,
          useUserStyle: true
        };
        setMessages((prevMessages) => [...prevMessages, newMessage])
        socket.emit("sendUserInput", text); // Send user input to the server
        setText(""); // Clear the input field
    }
  };


  const textareaRef = useRef(null);

  const handleInput = (e) => {
    const textarea = textareaRef.current;
    // Reset height to recalculate based on new content
    textarea.style.height = "auto";
    // Set height to scrollHeight to expand
    textarea.style.height = `${textarea.scrollHeight}px`;
    setText(e.target.value);
  };

    return (<>
        <main>
            {messages.map((message, index) => (
                (message.useUserStyle)?
                (<UserMessage key={index} text={message.text} />):
                (<BotMessage key={index} text={message.text} />)
            ))}
        </main>

        {/* from the Form class*/}
        <form onSubmit={sendMessage}>
        <section className="user-input">
          <textarea
            ref={textareaRef}
            value={text}
            onChange={handleInput}
            name="query"
            placeholder="Type here..."/>          
            <button className="submit-button" type="submit" value="Submit">
                <FontAwesomeIcon icon={faPaperPlane} style={{ width: '20px', height: '20px' }} />
            </button>
        </section>
        </form>
        
        </>
    );
}

export default Main;