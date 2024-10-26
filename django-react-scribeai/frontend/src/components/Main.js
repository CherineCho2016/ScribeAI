import React, { useState } from 'react';
import "./Main.css";

import "./Message.css"

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser } from "@fortawesome/free-solid-svg-icons";

const UserMessage =  ({text})=> {
      return (
        <section class="single-message-user">
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
    <section class="single-message-bot">
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
  
  const addMessage = () => {
    // Example of adding a new message
    // where we would put the response 
    const newMessage = {
      text: "New dynamic message at " + new Date().toLocaleTimeString() + (messages.length + 1),
      useUserStyle: messages.length % 2 == 0 // Alternate styles for odd/even
    };
    setMessages(prevMessages => [...prevMessages, newMessage]);
  };

    return (<>
        <main>
            <button onClick={addMessage}>Add Message</button>
            {messages.map((message, index) => (
                (message.useUserStyle)?
                (<UserMessage key={index} text={message.text} />):
                (<BotMessage key={index} text={message.text} />)

            ))}
        </main>
        
        </>
    );
}

export default Main;