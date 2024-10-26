import React, { useEffect, useState, useRef } from 'react';
import "./Main.css";
import "./Form.css";
import "./Message.css"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faPaperPlane, faRobot } from "@fortawesome/free-solid-svg-icons";

const UserMessage = ({ text }) => (
  <section className="single-message-user">
    <div className="user-icon">
      <FontAwesomeIcon icon={faUser} size="2x" />
    </div>
    <div>
      <p className="single-message-text">{text}</p>
    </div>
  </section>
);

const BotMessage = ({ text }) => (
  <section className="single-message-bot">
    <div className="user-icon">
      <FontAwesomeIcon icon={faRobot} size="2x" />
    </div>
    <div>
      <p className="single-message-text">{text}</p>
    </div>
  </section>
);

const ErrorMessage = ({ text }) => (
  <section className="single-message-error">
    <div>
      <p className="single-message-text error">Error: {text}</p>
    </div>
  </section>
);

function Main() {
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState("");
  const [isConnected, setIsConnected] = useState(false);
  const [isReconnecting, setIsReconnecting] = useState(false);
  const websocket = useRef(null);
  const reconnectAttempts = useRef(0);
  const maxReconnectAttempts = 5;

  const connectWebSocket = () => {
    try {
      websocket.current = new WebSocket('ws://localhost:8000/ws/chat/');

      websocket.current.onopen = () => {
        console.log('WebSocket Connected');
        setIsConnected(true);
        setIsReconnecting(false);
        reconnectAttempts.current = 0;
      };

      websocket.current.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          console.log('Received message:', data);
          
          if (data.error) {
            setMessages(prevMessages => [...prevMessages, {
              text: data.error,
              useUserStyle: false,
              isError: true
            }]);
          } else {
            setMessages(prevMessages => [...prevMessages, {
              text: data.message,
              useUserStyle: false,
              isError: false
            }]);
          }
        } catch (error) {
          console.error('Error parsing message:', error);
          setMessages(prevMessages => [...prevMessages, {
            text: 'Error processing response from server',
            useUserStyle: false,
            isError: true
          }]);
        }
      };

      websocket.current.onerror = (error) => {
        console.error('WebSocket Error:', error);
        setIsConnected(false);
        setMessages(prevMessages => [...prevMessages, {
          text: 'Connection error. Please try again.',
          useUserStyle: false,
          isError: true
        }]);
      };

      websocket.current.onclose = () => {
        console.log('WebSocket Disconnected');
        setIsConnected(false);
        
        // Attempt to reconnect if not at max attempts
        if (!isReconnecting && reconnectAttempts.current < maxReconnectAttempts) {
          setIsReconnecting(true);
          reconnectAttempts.current += 1;
          setTimeout(connectWebSocket, 3000); // Retry after 3 seconds
        } else if (reconnectAttempts.current >= maxReconnectAttempts) {
          setMessages(prevMessages => [...prevMessages, {
            text: 'Unable to establish connection. Please refresh the page.',
            useUserStyle: false,
            isError: true
          }]);
        }
      };
    } catch (error) {
      console.error('Error creating WebSocket:', error);
      setIsConnected(false);
    }
  };

  useEffect(() => {
    connectWebSocket();

    return () => {
      if (websocket.current) {
        websocket.current.close();
      }
    };
  }, []);

  const sendMessage = async (event) => {
    event.preventDefault();
    
    if (!text.trim()) return;

    // Add user message to chat
    const timestamp = new Date().toLocaleTimeString();
    const newMessage = {
      text: `${timestamp} ${text}`,
      useUserStyle: true,
      isError: false
    };
    setMessages(prevMessages => [...prevMessages, newMessage]);

    try {
      if (!isConnected) {
        throw new Error('Not connected to server');
      }

      if (websocket.current?.readyState === WebSocket.OPEN) {
        websocket.current.send(JSON.stringify({
          message: text
        }));
        setText("");
      } else {
        throw new Error('Connection not ready');
      }
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prevMessages => [...prevMessages, {
        text: `Failed to send message: ${error.message}`,
        useUserStyle: false,
        isError: true
      }]);
    }
  };

  const textareaRef = useRef(null);

  const handleInput = (e) => {
    const textarea = textareaRef.current;
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
    setText(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(e);
    }
  };

  return (
    <>
      <main>
        {messages.map((message, index) => {
          if (message.isError) {
            return <ErrorMessage key={index} text={message.text} />;
          }
          return message.useUserStyle ? 
            <UserMessage key={index} text={message.text} /> : 
            <BotMessage key={index} text={message.text} />;
        })}
      </main>

      <form onSubmit={sendMessage}>
        <section className="user-input">
          <textarea
            ref={textareaRef}
            value={text}
            onChange={handleInput}
            onKeyPress={handleKeyPress}
            name="query"
            placeholder={isConnected ? "Type here..." : "Connecting..."}
            disabled={!isConnected}
            style={{"background-color": "transparent"}}
          />          
          <button 
            className="submit-button" 
            type="submit" 
            disabled={!isConnected || !text.trim()}
          >
            <FontAwesomeIcon 
              icon={faPaperPlane} 
              style={{ 
                width: '20px', 
                height: '20px',
                opacity: isConnected ? 1 : 0.5 
              }} 
            />
          </button>
        </section>
      </form>
    </>
  );
}

export default Main;