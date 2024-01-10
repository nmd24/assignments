import React, { useState } from 'react';

function App() {
    // State for the title
    const [title, setTitle] = useState('My name is Nikhil');

    // Function to update the title with a random number
    const changeTitle = () => {
        const randomNumber = Math.random();
        setTitle(`My name is ${randomNumber}`);
    };

    return (
        <div>
            <Header title={title} />
            <button onClick={changeTitle}>Change Title</button>
        </div>
    );
}

function Header({ title }) {
    return <div>{title}</div>;
}

export default App;
