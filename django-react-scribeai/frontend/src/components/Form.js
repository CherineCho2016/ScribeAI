import React, { useState, useRef } from "react";
import "./Form.css"; // Assuming you have a CSS file for styles

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane } from '@fortawesome/free-solid-svg-icons';

const Form = () => {
  const [text, setText] = useState("");
  const textareaRef = useRef(null);

  const handleInput = (e) => {
    const textarea = textareaRef.current;
    // Reset height to recalculate based on new content
    textarea.style.height = "auto";
    // Set height to scrollHeight to expand
    textarea.style.height = `${textarea.scrollHeight}px`;
    setText(e.target.value);
  };

  return (
    <form>
        <section className="user-input">
          <label for="query"></label>
          <textarea
            ref={textareaRef}
            value={text}
            onChange={handleInput}
            name="query"
            placeholder="Type here..."/>          
            <button className="submit-button"type="submit" value="Submit">
                <FontAwesomeIcon icon={faPaperPlane} style={{ width: '20px', height: '20px' }} />
            </button>
        </section>
      </form>
  );
};

export default Form;